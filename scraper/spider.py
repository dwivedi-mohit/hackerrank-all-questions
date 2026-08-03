import re
import json
import time
from pathlib import Path

DOMAINS = [
    "algorithms", "data-structures", "python", "java", "c", "cpp",
    "mathematics", "sql", "databases", "shell", "regex", "fp",
    "ai", "ruby", "distributed-systems", "security", "react",
]

CHALLENGE_LIST_API = "https://www.hackerrank.com/rest/contests/master/tracks/{domain}/challenges?limit=50&offset={offset}"


def get_all_tracks(session) -> list[dict]:
    r = session.get("https://www.hackerrank.com/rest/contests/master/tracks", timeout=30)
    r.raise_for_status()
    data = r.json()
    return data.get("models") or []


def get_challenge_count(domain: str, session) -> int:
    r = session.get(
        CHALLENGE_LIST_API.format(domain=domain, offset=0),
        timeout=30,
    )
    return r.json().get("total", 0)


def get_challenges_for_domain(domain: str, session) -> list[str]:
    slugs = []
    offset = 0
    while True:
        url = CHALLENGE_LIST_API.format(domain=domain, offset=offset)
        try:
            resp = session.get(url, timeout=30)
            data = resp.json()
            challenges = data.get("models") or []
            if not challenges:
                break
            for ch in challenges:
                slug = ch.get("slug", "")
                if slug:
                    slugs.append(slug)
            if len(challenges) < 50:
                break
            offset += 50
            time.sleep(0.15)
        except Exception as e:
            print(f"  [spider] API error for {domain} offset={offset}: {e}")
            break
    return slugs


def crawl_all_domains(session) -> dict[str, list[str]]:
    domain_slugs = {}
    for domain in DOMAINS:
        print(f"\n[spider] Crawling domain: {domain}")
        slugs = get_challenges_for_domain(domain, session)
        print(f"  [spider] Found {len(slugs)} challenges for {domain}")
        domain_slugs[domain] = slugs
    return domain_slugs
