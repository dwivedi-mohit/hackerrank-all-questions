import json
with open('output/challenges.json') as f:
    c = json.load(f)
print(f'challenges.json: {len(c)} entries')
first = c[0]
print(f'First entry: {first["name"]} - domains: {first.get("domains")}')
with open('output/domain-index.json') as f:
    d = json.load(f)
print(f'domain-index.json: {len(d)} domains')
for k, v in sorted(d.items()):
    print(f'  {k}: {len(v)} slugs')