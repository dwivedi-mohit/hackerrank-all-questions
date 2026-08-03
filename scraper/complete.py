import sys
import json
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, str(Path(__file__).parent.parent))
from scraper.auth import login
from scraper.challenge import fetch_challenge
from scraper.dedup import format_challenge_md

OUTPUT_DIR = Path(__file__).parent.parent / "output"
FULL_SLUGS_FILE = OUTPUT_DIR / "full-slugs.json"
WORKERS = 8

KNOWN_DOMAINS = {
    "algorithms", "data-structures", "python", "java", "c", "cpp",
    "mathematics", "sql", "databases", "shell", "regex", "fp",
    "ai", "ruby", "distributed-systems", "security", "react",
}


def enumerate_all_slugs(session) -> list[str]:
    slugs = []
    offset = 0
    while True:
        r = session.get(
            "https://www.hackerrank.com/rest/contests/master/challenges",
            params={"limit": 50, "offset": offset},
            timeout=40,
        )
        r.raise_for_status()
        models = r.json().get("models") or []
        for m in models:
            if m.get("slug"):
                slugs.append(m["slug"])
        print(f"  [enumerate] offset={offset} got={len(models)} total={len(slugs)}")
        if len(models) < 50:
            break
        offset += 50
        time.sleep(0.15)
    slugs = list(dict.fromkeys(slugs))
    FULL_SLUGS_FILE.write_text(json.dumps(slugs, indent=2), encoding="utf-8")
    return slugs


def load_existing_slugs() -> set[str]:
    slugs = set()
    flat = OUTPUT_DIR / "questions" / "_flat"
    if flat.exists():
        slugs.update(p.stem for p in flat.glob("*.md"))
    return slugs


def classify(info: dict) -> str:
    domain = info.get("domain") or ""
    subdomain = info.get("subdomain") or ""
    kind = info.get("kind", "")
    if domain in KNOWN_DOMAINS:
        return domain
    if kind == "game":
        return "misc"
    if domain == "tutorials" or subdomain:
        if subdomain and "days" in subdomain:
            return f"tutorials"
        return f"tutorials" if subdomain else "misc"
    return "misc"


def enrich_from_detail(slug: str, session) -> dict | None:
    try:
        resp = session.get(
            f"https://www.hackerrank.com/rest/contests/master/challenges/{slug}",
            timeout=30,
        )
        if resp.status_code != 200:
            return None
        ch = resp.json().get("model") or {}
        tr = ch.get("track") or {}
        return {
            "slug": ch.get("slug", slug),
            "name": ch.get("name", slug),
            "domain": tr.get("track_slug", tr.get("slug", "")),
            "subdomain": tr.get("slug", ""),
            "difficulty": ch.get("difficulty_name", ""),
            "score": ch.get("max_score") or ch.get("score") or 0,
            "kind": ch.get("kind") or "",
            "preview": ch.get("preview") or "",
            "problem_statement": (ch.get("problem_statement") or "").strip(),
            "input_format": (ch.get("input_format") or "").strip(),
            "output_format": (ch.get("output_format") or "").strip(),
            "constraints": (ch.get("constraints") or "").strip(),
            "body_html": ch.get("body_html") or "",
            "pre_blocks": [],
            "url": f"https://www.hackerrank.com/challenges/{slug}",
        }
    except Exception:
        return None


def extract_pre_blocks(html: str) -> list[str]:
    from bs4 import BeautifulSoup
    import re
    if not html:
        return []
    soup = BeautifulSoup(html, "html.parser")
    blocks = []
    for pre in soup.find_all("pre"):
        text = pre.get_text("\n")
        text = re.sub(r"[\u00a0\u2009\u200a\u202f]", " ", text)
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n\s*\n+", "\n", text)
        blocks.append(text.strip())
    return [b for b in blocks if b]


def main():
    session = login()

    print("[1/4] Enumerating full challenge list from generic endpoint...")
    all_slugs = enumerate_all_slugs(session)
    print(f"  TOTAL: {len(all_slugs)}")

    print("[2/4] Diffing against existing _flat...")
    existing = load_existing_slugs()
    missing = [s for s in all_slugs if s not in existing]
    print(f"  existing={len(existing)}  missing={len(missing)}")

    if not missing:
        print("  Nothing missing. Done.")
        return

    print(f"[3/4] Fetching full detail for {len(missing)} missing challenges...")
    all_challenges = {}
    done = 0

    def fetch_one(slug):
        info = enrich_from_detail(slug, session)
        if info:
            info["pre_blocks"] = extract_pre_blocks(info.get("body_html") or "")
        return slug, info

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {pool.submit(fetch_one, s): s for s in missing}
        for i, fut in enumerate(as_completed(futures), 1):
            slug, info = fut.result()
            done += 1
            if info:
                all_challenges[slug] = info
            if i % 25 == 0 or i == len(missing):
                print(f"  {i}/{len(missing)} fetched  saved={len(all_challenges)}")

    print(f"[4/4] Writing {len(all_challenges)} new files...")
    files_written = 0
    folder_counts = {}
    for slug, info in all_challenges.items():
        folder = classify(info)
        folder_counts[folder] = folder_counts.get(folder, 0) + 1
        if folder.startswith("tutorials"):
            d = OUTPUT_DIR / "questions" / folder
        elif folder == "misc":
            d = OUTPUT_DIR / "questions" / "misc"
        else:
            d = OUTPUT_DIR / "questions" / folder
        d.mkdir(parents=True, exist_ok=True)
        md = format_challenge_md(slug, info)
        (d / f"{slug}.md").write_text(md, encoding="utf-8")
        files_written += 1

    print(f"  Files written: {files_written}")
    print(f"  Folder breakdown:")
    for f, c in sorted(folder_counts.items()):
        print(f"    {f}: {c}")

    # Update domain-slugs.json
    ds_file = OUTPUT_DIR / "domain-slugs.json"
    ds = json.loads(ds_file.read_text(encoding="utf-8")) if ds_file.exists() else {}
    for slug, info in all_challenges.items():
        folder = classify(info)
        ds.setdefault(folder, [])
        if slug not in ds[folder]:
            ds[folder].append(slug)
    ds_file.write_text(json.dumps(ds, indent=2), encoding="utf-8")

    print("\n  Done. Run rebuild_flat_metadata() next.")


def rebuild_flat_metadata():
    questions_dir = OUTPUT_DIR / "questions"
    flat_dir = questions_dir / "_flat"
    flat_dir.mkdir(exist_ok=True)

    all_slugs = []
    for domain_dir in sorted(questions_dir.iterdir()):
        if not domain_dir.is_dir() or domain_dir.name.startswith("_"):
            continue
        for md_file in domain_dir.glob("*.md"):
            slug = md_file.stem
            all_slugs.append(slug)
            flat_file = flat_dir / md_file.name
            if not flat_file.exists():
                flat_file.write_text(md_file.read_text(encoding="utf-8"), encoding="utf-8")
            else:
                import shutil
                shutil.copy2(str(md_file), str(flat_file))

    # also write any in _flat that aren't in any domain folder
    for md_file in flat_dir.glob("*.md"):
        slug = md_file.stem
        if slug not in all_slugs:
            all_slugs.append(slug)

    all_slugs = sorted(set(all_slugs))
    print(f"[rebuild] _flat total: {len(all_slugs)}")

    # rebuild challenges.json
    challenges = []
    for slug in all_slugs:
        md = (flat_dir / f"{slug}.md").read_text(encoding="utf-8", errors="ignore")
        name_line = md.split("\n")[0].lstrip("# ").strip() if md else slug
        challenges.append({"slug": slug, "name": name_line})

    (OUTPUT_DIR / "challenges.json").write_text(
        json.dumps(challenges, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # rebuild domain-index.json
    ds = json.loads((OUTPUT_DIR / "domain-slugs.json").read_text(encoding="utf-8"))
    idx = {}
    for domain, slugs in ds.items():
        idx[domain] = {"count": len(slugs), "slugs": sorted(slugs)}
    (OUTPUT_DIR / "domain-index.json").write_text(
        json.dumps(idx, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # rebuild metadata/all.json
    meta_dir = OUTPUT_DIR / "metadata"
    meta_dir.mkdir(exist_ok=True)
    (meta_dir / "all.json").write_text(
        json.dumps(challenges, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"[rebuild] challenges.json: {len(challenges)}")
    print(f"[rebuild] domain-index.json: {len(idx)} domains")


if __name__ == "__main__":
    main()
    rebuild_flat_metadata()
