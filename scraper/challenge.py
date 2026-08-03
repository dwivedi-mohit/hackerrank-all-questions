import re
import time
import requests
from bs4 import BeautifulSoup

CHALLENGE_API = "https://www.hackerrank.com/rest/contests/master/challenges/{slug}"
RETRIES = 3


def fetch_challenge(slug: str, session: requests.Session) -> dict | None:
    url = CHALLENGE_API.format(slug=slug)
    for attempt in range(1, RETRIES + 1):
        try:
            resp = session.get(url, timeout=30)
            if resp.status_code == 200:
                data = resp.json()
                ch = data.get("model") or data.get("challenge")
                if ch:
                    track = ch.get("track") or {}
                    body_html = ch.get("body_html") or ""
                    return {
                        "slug": ch.get("slug", slug),
                        "name": ch.get("name", slug),
                        "domain": track.get("track_slug", track.get("slug", "")),
                        "subdomain": track.get("slug", ""),
                        "difficulty": ch.get("difficulty_name", ""),
                        "score": ch.get("max_score") or ch.get("score") or 0,
                        "preview": ch.get("preview") or "",
                        "problem_statement": (ch.get("problem_statement") or "").strip(),
                        "input_format": (ch.get("input_format") or "").strip(),
                        "output_format": (ch.get("output_format") or "").strip(),
                        "constraints": (ch.get("constraints") or "").strip(),
                        "body_html": body_html,
                        "pre_blocks": extract_pre_blocks(body_html),
                        "url": f"https://www.hackerrank.com/challenges/{slug}",
                    }
            if resp.status_code == 429:
                time.sleep(min(2 ** attempt, 30))
                continue
            if resp.status_code == 404:
                return None
        except requests.RequestException:
            if attempt == RETRIES:
                return None
            time.sleep(1)
    return None


def extract_pre_blocks(html: str) -> list[str]:
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
    if not blocks:
        for code in soup.find_all("code"):
            text = code.get_text("\n")
            text = re.sub(r"[\u00a0\u2009\u200a\u202f]", " ", text)
            text = re.sub(r"\n\s*\n+", "\n", text)
            blocks.append(text.strip())
    return [b for b in blocks if b]