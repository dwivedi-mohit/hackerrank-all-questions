import requests, json

s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0"
tracks = ["angular", "spring-boot", "devops", "git", "docker", "kubernetes", "ci-cd"]

for t in tracks:
    try:
        r = s.get(
            "https://www.hackerrank.com/rest/contests/master/challenges",
            params={"offset": 0, "limit": 1, "track": t},
            timeout=15,
        )
        if r.status_code == 200:
            d = r.json()
            total = d.get("total", 0)
            print(f"{t}: OK - total={total}")
        else:
            print(f"{t}: HTTP {r.status_code}")
    except Exception as e:
        print(f"{t}: ERROR - {e}")
