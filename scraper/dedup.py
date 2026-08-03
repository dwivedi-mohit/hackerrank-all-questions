import json
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent / "output"


def build_domain_map(domain_slugs: dict[str, list[str]]) -> dict[str, list[str]]:
    slug_to_domains: dict[str, list[str]] = {}
    for domain, slugs in domain_slugs.items():
        for slug in slugs:
            slug_to_domains.setdefault(slug, []).append(domain)
    return slug_to_domains


def save_per_domain_files(domain_slugs: dict[str, list[str]], challenges: dict[str, dict]):
    questions_dir = OUTPUT_DIR / "questions"
    questions_dir.mkdir(parents=True, exist_ok=True)

    flat_dir = questions_dir / "_flat"
    flat_dir.mkdir(exist_ok=True)

    for slug, info in challenges.items():
        domains = info.get("domains", []) or [info.get("domain", "unknown")]
        md = format_challenge_md(slug, info)
        filename = f"{slug}.md"

        flat_file = flat_dir / filename
        flat_file.write_text(md, encoding="utf-8")

        for domain in domains:
            domain_dir = questions_dir / domain
            domain_dir.mkdir(exist_ok=True)
            (domain_dir / filename).write_text(md, encoding="utf-8")


def section_or_missing(data: str) -> bool:
    return bool(data and data.strip() and data.strip() != "(None)")


def format_challenge_md(slug: str, info: dict) -> str:
    name = info.get("name", slug)
    domains = info.get("domains", [])
    domain_str = ", ".join(domains) if domains else info.get("domain", "unknown")
    difficulty = info.get("difficulty", "N/A")
    score = info.get("score", 0)
    preview = info.get("preview", "").strip()
    problem_statement = info.get("problem_statement", "").strip()
    input_format = info.get("input_format", "").strip()
    output_format = info.get("output_format", "").strip()
    constraints = info.get("constraints", "").strip()
    pre_blocks = info.get("pre_blocks") or []
    url = info.get("url", f"https://www.hackerrank.com/challenges/{slug}")

    lines = []
    lines.append(f"# {name}\n")
    lines.append("---\n")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append(f"| **Slug** | `{slug}` |")
    lines.append(f"| **Domain** | {domain_str} |")
    lines.append(f"| **Difficulty** | {difficulty} |")
    lines.append(f"| **Score** | {score} |")
    lines.append(f"| **URL** | {url} |")
    lines.append("\n---\n")

    if preview and preview != "(None)":
        lines.append("## Preview\n")
        lines.append(preview + "\n")

    if section_or_missing(problem_statement):
        lines.append("## Problem Statement\n")
        body = problem_statement.replace("  \n", "\n\n")
        lines.append(body + "\n")

    if section_or_missing(input_format):
        lines.append("## Input Format\n")
        lines.append(input_format.replace("  \n", "\n\n") + "\n")

    if section_or_missing(output_format):
        lines.append("## Output Format\n")
        lines.append(output_format.replace("  \n", "\n\n") + "\n")

    if section_or_missing(constraints):
        lines.append("## Constraints\n")
        lines.append(constraints.replace("  \n", "\n\n") + "\n")

    if pre_blocks:
        lines.append("## Sample Tests\n")
        for i, block in enumerate(pre_blocks, 1):
            lines.append(f"### Test {i}\n")
            lines.append("```\n" + block + "\n```\n")

    if not (section_or_missing(problem_statement) or pre_blocks):
        lines.append("*Full problem statement only available on HackerRank.*\n")

    return "\n".join(lines)


def save_metadata(domain_slugs: dict[str, list[str]], challenges: dict[str, dict]):
    meta_dir = OUTPUT_DIR / "metadata"
    meta_dir.mkdir(parents=True, exist_ok=True)

    all_challenges = []
    for slug, info in challenges.items():
        all_challenges.append({
            "slug": slug,
            "name": info.get("name", slug),
            "domains": info.get("domains", []) or [info.get("domain", "unknown")],
            "difficulty": info.get("difficulty", ""),
            "score": info.get("score", 0),
            "url": info.get("url", ""),
        })

    (meta_dir / "all.json").write_text(
        json.dumps(all_challenges, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    domain_index = {}
    for domain, slugs in domain_slugs.items():
        domain_index[domain] = {
            "count": len(slugs),
            "slugs": sorted(slugs),
        }
    (OUTPUT_DIR / "domain-index.json").write_text(
        json.dumps(domain_index, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    (OUTPUT_DIR / "challenges.json").write_text(
        json.dumps(
            [{"slug": s, "name": challenges[s].get("name", s), "domains": challenges[s].get("domains", []) or [challenges[s].get("domain", "unknown")]} for s in sorted(challenges.keys())],
            indent=2, ensure_ascii=False
        ), encoding="utf-8"
    )