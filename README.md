<div align="center">

<img src="assets/matrix-banner.svg" width="100%"/>

<br/>

[![GitHub stars](https://img.shields.io/github/stars/dwivedi-mohit/hackerrank-all-questions?style=for-the-badge&logo=github&color=00FF41&labelColor=0a0a0a)](https://github.com/dwivedi-mohit/hackerrank-all-questions/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/dwivedi-mohit/hackerrank-all-questions?style=for-the-badge&logo=github&color=00FF41&labelColor=0a0a0a)](https://github.com/dwivedi-mohit/hackerrank-all-questions/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-00FF41?style=for-the-badge&labelColor=0a0a0a)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.14-00FF41?style=for-the-badge&logo=python&logoColor=0a0a0a&labelColor=0a0a0a)](https://python.org)
[![Questions](https://img.shields.io/badge/3%2C401-Unique%20Questions-00FF41?style=for-the-badge&labelColor=0a0a0a)](output/questions)

<br/>

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=24&duration=3000&pause=1000&color=00FF41&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=80&lines=Every+HackerRank+Question+Offline%3BPer+Domain+Organization" alt="Typing SVG" />

</div>

---

<br/>

<div align="center">

```
 ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
 ██╔════╝ ██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
 ██║  ███╗███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
 ██║   ██║██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
 ╚██████╔╝██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
```

</div>

---

<br/>

## System Status

```
┌─────────────────────────────────────────────────────────┐
│  $ ./hackerrank-dumper --status                         │
├─────────────────────────────────────────────────────────┤
│  [OK] Total Questions    : 3,401 (unique)               │
│  [OK] Public Questions   : 2,468 (per-domain + contests)│
│  [OK] Enterprise Qs      : 933 (HR Work Library)        │
│  [OK] Domains            : 20 (per-domain folders)      │
│  [OK] File Format        : Markdown (.md)               │
│  [OK] Status             : OPERATIONAL                  │
└─────────────────────────────────────────────────────────┘
```

---

<br/>

## Directory Structure

```
┌─────────────────────────────────────────────────────────┐
│  $ ls output/questions/                                 │
├─────────────────────────────────────────────────────────┤
│  ai/                     105 questions                  │
│  algorithms/             442 questions                  │
│  c/                       25 questions                  │
│  cpp/                     44 questions                  │
│  data-structures/        121 questions                  │
│  databases/               52 questions                  │
│  distributed-systems/     21 questions                  │
│  enterprise/             933 questions (HR Work)        │
│  fp/                      93 questions                  │
│  java/                    64 questions                  │
│  mathematics/            283 questions                  │
│  misc/                   778 questions                  │
│  python/                 115 questions                  │
│  react/                   10 questions                  │
│  regex/                   47 questions                  │
│  ruby/                    41 questions                  │
│  security/                12 questions                  │
│  shell/                   65 questions                  │
│  sql/                     58 questions                  │
│  tutorials/               92 questions                  │
├─────────────────────────────────────────────────────────┤
│  TOTAL: 3,401 unique questions | 20 DOMAINS             │
└─────────────────────────────────────────────────────────┘
```

---

<br/>

## Statistics

```
┌─────────────────────────────────────────────────────────┐
│  DOMAIN                QUESTIONS                        │
│  ────────────────────  ─────────                        │
│  Enterprise             933                             │
│  Misc                   778                             │
│  Algorithms             442                             │
│  Mathematics            283                             │
│  Data Structures        121                             │
│  Python                 115                             │
│  AI                     105                             │
│  Functional Programming  93                             │
│  Tutorials               92                             │
│  Shell                   65                             │
│  Java                    64                             │
│  SQL                     58                             │
│  Databases               52                             │
│  Regex                   47                             │
│  C++                     44                             │
│  Ruby                    41                             │
│  C                       25                             │
│  Distributed Systems     21                             │
│  Security                12                             │
│  React                   10                             │
│  ────────────────────  ─────────                        │
│  TOTAL               3,401 unique questions             │
└─────────────────────────────────────────────────────────┘
```

---

<br/>

## Quick Start

```bash
# Clone the repo
git clone https://github.com/dwivedi-mohit/hackerrank-all-questions.git
cd hackerrank-all-questions

# Read a question
cat output/questions/algorithms/solve-me-first.md

# Search
grep -rl "binary search" output/questions/

# List domain
ls output/questions/python/

# Query index
python3 -c "import json; d=json.load(open('output/challenges.json')); print(len(d))"
```

---

<br/>

## Query Examples

```python
import json

with open("output/challenges.json") as f:
    challenges = json.load(f)

# Find all algorithm problems
algo_problems = [
    c for c in challenges
    if c.get("domain") == "algorithms"
]
print(f"Found {len(algo_problems)} algorithm problems")

# Count by domain
from collections import Counter
domain_counts = Counter()
for c in challenges:
    domain_counts[c.get("domain", "unknown")] += 1
for d, count in domain_counts.most_common():
    print(f"  {d}: {count}")
```

---

<br/>

## Features

- **3,401 unique questions** across 20 domains
- **2,468 public + 933 enterprise questions**
- Per-domain folder organization
- Problem metadata (difficulty, score, URL)
- Clean Markdown format
- Master JSON index
- Flat copy in `_flat/` for bulk operations
- All difficulty levels

---

<br/>

## Enterprise Library

The enterprise questions are sourced from HackerRank's Work Library API. These include:
- **Coding challenges** (165)
- **Full-stack projects** (114)
- **MCQs** (493 single + 77 multi-select)
- **Database queries** (42)
- **System design** (5)
- **And more** (sudorank, approx, whiteboard, etc.)

> **Note:** The full HackerRank enterprise library contains 9,514 questions (4,431 hands-on + 5,083 MCQs). Accessing the complete library requires a paid subscription (Starter $165/mo, Pro $375/mo, or Enterprise $800+/mo). The 933 enterprise questions in this repo represent the maximum available on a free trial.

---

<br/>

## Contest Sources

This repo includes challenges from the following HackerRank contest series:
- **101 Hack** (18–55)
- **30 Days of Code**
- **Project Euler** (1–50+)
- **Week of Code** (w1–w38)
- **World CodeSprint** (5–13)
- **University CodeSprint** (2–5)
- **Ad Infinitum** (8–18)
- **HourRank** (26–31)
- **Hack the Interview** (6 variants)
- **Adobe Hackathon**, **CodeAgon**, **Indeed Prime**, **Regular Expresso**

---

<br/>

## Author

```
┌─────────────────────────────────────────────────────────┐
│  $ whoami                                               │
│  Mohit Dwivedi                                          │
│                                                         │
│  $ cat github.txt                                       │
│  https://github.com/dwivedi-mohit                       │
│                                                         │
│  $ echo "Built with ❤ for the coding community"        │
│  Built with ❤ for the coding community                  │
└─────────────────────────────────────────────────────────┘
```

---

<br/>

## License

```
MIT License — 2026 Mohit Dwivedi
```

---

<br/>

<div align="center">

```
█──█ █── █─ █─── ██─█ ██▀▀ ██▀▀ █── █▀▀▄ ▀█▀ █▀▀▄ █▀▀█ █── █▀▀▄ █▀▀█
█▀▀█ █── █  █▄▄ ██▀  █▀▀  █▀▀  █▄▄ █▀▀█  █  █▀▀▄ █▄▄▀ █▄▄ █▀▀▄ █▄▄▀
█──█ ▀▀▀ ▀─ ▀─── ▀─▀─ ▀▀▀▀ ▀─── ▀── ▀──▀  ▀  ▀──▀ ▀──▀ ▀── ▀▀▀  ▀──▀
```

**Made by [Mohit Dwivedi](https://github.com/dwivedi-mohit)**

[⬆ Back to Top](#hackerrank-dumper)

</div>
