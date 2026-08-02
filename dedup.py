import json, os, shutil, re

OUTPUT_DIR = "output"
METADATA_DIR = os.path.join(OUTPUT_DIR, "metadata")
QUESTIONS_DIR = os.path.join(OUTPUT_DIR, "questions")

# Step 1: Read all domain metadata files and collect slugs per domain
print("=== Step 1: Reading metadata ===")
domain_slugs = {}
domain_metadata = {}

for f in sorted(os.listdir(METADATA_DIR)):
    if not f.endswith(".json"):
        continue
    domain = f.replace(".json", "")
    with open(os.path.join(METADATA_DIR, f), "r", encoding="utf-8") as fh:
        challenges = json.load(fh)
        slugs = [c["slug"] for c in challenges]
        domain_slugs[domain] = set(slugs)
        domain_metadata[domain] = {c["slug"]: c for c in challenges}
        print(f"  {domain}: {len(slugs)} slugs")

all_domains = sorted(domain_slugs.keys())
print(f"\nTotal domains: {len(all_domains)}")

# Find unique slugs
all_slugs_set = set()
for slugs in domain_slugs.values():
    all_slugs_set.update(slugs)
unique_slugs = sorted(all_slugs_set)
print(f"Unique slugs: {len(unique_slugs)}")

# Step 2: Build consolidated metadata with domain tags
print("\n=== Step 2: Building consolidated metadata ===")
consolidated = []
domain_index = {}

for slug in unique_slugs:
    domains_for_slug = sorted([d for d in all_domains if slug in domain_slugs[d]])
    # Use metadata from first available domain
    meta = None
    for d in all_domains:
        if slug in domain_metadata[d]:
            meta = domain_metadata[d][slug]
            break

    entry = dict(meta) if meta else {"slug": slug, "name": slug}
    entry["domains"] = domains_for_slug
    entry["domain_count"] = len(domains_for_slug)
    consolidated.append(entry)

    for d in domains_for_slug:
        domain_index.setdefault(d, []).append(slug)

print(f"Consolidated entries: {len(consolidated)}")

# Save consolidated metadata
os.makedirs(os.path.join(METADATA_DIR), exist_ok=True)
with open(os.path.join(METADATA_DIR, "all.json"), "w", encoding="utf-8") as fh:
    json.dump(consolidated, fh, indent=2, ensure_ascii=False)
print(f"Saved: {METADATA_DIR}/all.json")

# Save domain index
with open(os.path.join(OUTPUT_DIR, "domain-index.json"), "w", encoding="utf-8") as fh:
    json.dump(domain_index, fh, indent=2, ensure_ascii=False)
print(f"Saved: {OUTPUT_DIR}/domain-index.json")

# Step 3: Deduplicate question files
print("\n=== Step 3: Deduplicating question files ===")

# Collect all existing question files and their domain sources
existing_files = {}
for d in all_domains:
    qdir = os.path.join(QUESTIONS_DIR, d)
    if not os.path.isdir(qdir):
        continue
    for fname in os.listdir(qdir):
        if fname.endswith(".md"):
            slug = fname[:-3]
            if slug not in existing_files:
                existing_files[slug] = os.path.join(qdir, fname)

print(f"Found {len(existing_files)} unique question files")

# Create new unified questions directory
NEW_QUESTIONS_DIR = os.path.join(OUTPUT_DIR, "questions")
temp_dir = os.path.join(OUTPUT_DIR, "_questions_new")
os.makedirs(temp_dir, exist_ok=True)

moved = 0
for slug, src_path in existing_files.items():
    # Read the file content
    with open(src_path, "r", encoding="utf-8") as fh:
        content = fh.read()

    # Get domains for this slug
    domains_for_slug = sorted([d for d in all_domains if slug in domain_slugs[d]])
    domain_line = ", ".join(domains_for_slug)

    # Check if content already has a Domains section
    if "## Domains" not in content:
        # Add Domains section before the last section or at the end
        domain_section = f"\n## Domains\n\n{domain_line}\n"
        # Insert before the last line or append
        content = content.rstrip() + "\n" + domain_section

    # Write to new location
    dst_path = os.path.join(temp_dir, f"{slug}.md")
    with open(dst_path, "w", encoding="utf-8") as fh:
        fh.write(content)
    moved += 1

    if moved % 500 == 0:
        print(f"  Processed {moved}/{len(existing_files)}")

print(f"Processed {moved} files to temp directory")

# Step 4: Replace old questions directory with new deduplicated one
print("\n=== Step 4: Replacing questions directory ===")
# Remove old domain subdirectories
for d in all_domains:
    qdir = os.path.join(QUESTIONS_DIR, d)
    if os.path.isdir(qdir):
        shutil.rmtree(qdir)
        print(f"  Removed: {qdir}")

# Move temp directory contents to questions directory
for fname in os.listdir(temp_dir):
    src = os.path.join(temp_dir, fname)
    dst = os.path.join(QUESTIONS_DIR, fname)
    shutil.move(src, dst)

os.rmdir(temp_dir)
print(f"  Moved {moved} files to {QUESTIONS_DIR}/")

# Step 5: Rebuild challenges.json
print("\n=== Step 5: Rebuilding challenges.json ===")
challenges_list = []
for entry in consolidated:
    slug = entry["slug"]
    challenges_list.append({
        "name": entry.get("name", slug),
        "slug": slug,
        "domains": entry.get("domains", []),
        "difficulty": entry.get("difficulty_name"),
        "max_score": entry.get("max_score"),
        "success_ratio": entry.get("success_ratio"),
        "total_count": entry.get("total_count"),
        "solved_count": entry.get("solved_count"),
        "tags": entry.get("tag_names", []),
        "url": f"https://www.hackerrank.com/challenges/{slug}",
        "problem_file": f"questions/{slug}.md"
    })

with open(os.path.join(OUTPUT_DIR, "challenges.json"), "w", encoding="utf-8") as fh:
    json.dump(challenges_list, fh, indent=2, ensure_ascii=False)
print(f"Saved: {OUTPUT_DIR}/challenges.json ({len(challenges_list)} entries)")

# Step 6: Remove old per-domain metadata files (keep all.json)
print("\n=== Step 6: Cleaning up old metadata ===")
for f in os.listdir(METADATA_DIR):
    if f.endswith(".json") and f != "all.json":
        os.remove(os.path.join(METADATA_DIR, f))
        print(f"  Removed: {f}")

print("\n=== Deduplication complete! ===")
print(f"Unique questions: {len(consolidated)}")
print(f"Domains: {len(all_domains)}")
print(f"Total domain tags: {sum(len(v) for v in domain_index.values())}")
