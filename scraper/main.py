import sys
import json
import time
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

from scraper.auth import login
from scraper.spider import crawl_all_domains, DOMAINS
from scraper.challenge import fetch_challenge
from scraper.dedup import (
    build_domain_map, save_per_domain_files, save_metadata,
)

OUTPUT_DIR = Path(__file__).parent.parent / "output"
CHECKPOINT_FILE = OUTPUT_DIR / "scrape_checkpoint.json"
WORKERS = 8
DELAY = 0.15


def load_checkpoint() -> dict:
    if CHECKPOINT_FILE.exists():
        return json.loads(CHECKPOINT_FILE.read_text(encoding="utf-8"))
    return {}


def save_checkpoint(state: dict):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    CHECKPOINT_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def scrape_domain_challenges(domain: str, slugs: list[str], session, checkpoint: dict) -> dict[str, dict]:
    challenges = {}
    done_slugs = set(checkpoint.get("done_slugs", []))
    remaining = [s for s in slugs if s not in done_slugs]
    print(f"\n[scrape] {domain}: {len(slugs)} total, {len(remaining)} remaining")

    def fetch_one(slug):
        return slug, fetch_challenge(slug, session)

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {}
        for slug in remaining:
            f = pool.submit(fetch_one, slug)
            futures[f] = slug
            time.sleep(DELAY / WORKERS)

        for i, future in enumerate(as_completed(futures), 1):
            slug, result = future.result()
            done_slugs.add(slug)
            if result:
                result.setdefault("domains", [])
                if domain not in result["domains"]:
                    result["domains"].append(domain)
                challenges[slug] = result

            if i % 50 == 0 or i == len(remaining):
                print(f"  [{domain}] {i}/{len(remaining)} fetched")
                save_checkpoint({"done_slugs": list(done_slugs), "domain": domain})

    return challenges


def merge_challenges(all_challenges: dict[str, dict], new_challenges: dict[str, dict], domain: str):
    for slug, info in new_challenges.items():
        if slug in all_challenges:
            if domain not in all_challenges[slug].get("domains", []):
                all_challenges[slug]["domains"].append(domain)
        else:
            all_challenges[slug] = info


def main():
    parser = argparse.ArgumentParser(description="HackerRank Scraper")
    parser.add_argument("--domains", nargs="*", help="Specific domains to scrape (default: all)")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("[main] Logging in...")
    session = login()

    print("[main] Crawling domain pages for challenge lists...")
    domain_slugs = crawl_all_domains(session)

    total_challenges = sum(len(v) for v in domain_slugs.values())
    print(f"\n[main] Total challenge slugs found: {total_challenges}")

    (OUTPUT_DIR / "domain-slugs.json").write_text(
        json.dumps(domain_slugs, indent=2), encoding="utf-8"
    )

    all_challenges = {}
    checkpoint = load_checkpoint() if args.resume else {}

    domains_to_scrape = args.domains if args.domains else DOMAINS
    for domain in domains_to_scrape:
        slugs = domain_slugs.get(domain, [])
        if not slugs:
            print(f"\n[main] Skipping {domain} (no challenges found)")
            continue
        domain_challenges = scrape_domain_challenges(domain, slugs, session, checkpoint)
        merge_challenges(all_challenges, domain_challenges, domain)
        print(f"  [main] {domain}: {len(domain_challenges)} challenges scraped")

    print(f"\n[main] Total unique challenges scraped: {len(all_challenges)}")

    print("[main] Building per-domain folder structure...")
    save_per_domain_files(domain_slugs, all_challenges)

    print("[main] Saving metadata...")
    save_metadata(domain_slugs, all_challenges)

    if CHECKPOINT_FILE.exists():
        CHECKPOINT_FILE.unlink()

    print(f"\n[main] Done! Output in {OUTPUT_DIR}")
    print(f"  Questions: {OUTPUT_DIR / 'questions'}")
    print(f"  Metadata: {OUTPUT_DIR / 'metadata'}")


if __name__ == "__main__":
    main()
