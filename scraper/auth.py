import json
import requests
from pathlib import Path

COOKIES_FILE = Path(__file__).parent.parent / "cookies.json"
LOGIN_URL = "https://www.hackerrank.com/rest/auth/login"
EMAIL = "mohit0064900@gmail.com"
PASSWORD = "Mohit@7509193904"


def login() -> requests.Session:
    if COOKIES_FILE.exists():
        session = requests.Session()
        data = json.loads(COOKIES_FILE.read_text(encoding="utf-8"))
        session.cookies.update(data.get("cookies", {}))
        if data.get("csrf_token"):
            session.headers["X-Csrf-Token"] = data["csrf_token"]
        try:
            resp = session.get("https://www.hackerrank.com/dashboard", timeout=30, allow_redirects=False)
            if resp.status_code == 200:
                print("[auth] Session restored from cookies.json")
                return session
        except Exception:
            pass
        print("[auth] Saved session expired, logging in again...")

    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Referer": "https://www.hackerrank.com/auth/login",
    })

    payload = {
        "login": EMAIL,
        "password": PASSWORD,
        "fallback": True,
        "request_json": True,
    }

    resp = session.post(LOGIN_URL, json=payload, timeout=30)
    resp.raise_for_status()
    body = resp.json()

    if not body.get("status"):
        raise RuntimeError(f"Login failed: {body.get('error', 'unknown')}")

    csrf = body.get("csrf_token", "")
    if csrf:
        session.headers["X-Csrf-Token"] = csrf

    print("[auth] Login successful")
    COOKIES_FILE.write_text(
        json.dumps({"cookies": dict(session.cookies), "csrf_token": csrf}, indent=2),
        encoding="utf-8",
    )
    return session
