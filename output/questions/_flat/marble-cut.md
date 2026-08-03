# Marble Cut

---

| Field | Value |
|---|---|
| **Slug** | `marble-cut` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 20 |
| **Contest** | 101hack22 |
| **URL** | https://www.hackerrank.com/challenges/marble-cut |

---

## Problem Statement

Given a marble piece of size $l \times b$, your task is to find out whether it can be cut into pieces of size $3 \times 1$ or not.

## Input Format

The first line will contain $T$, i.e. the number of test cases.<br>
The next $T$ lines will contain a pair of integers $l$ and $b$ each, separated by a single space.

**Constraints**<br>
$1 \le T \le 10^5$<br>
$1 \le l, b \le 10^9$

## Output Format

Print _YES_ if it is possible to cut the given marble piece without any remainder; else print _NO_ followed by the size of the remaining area.

## Sample Tests

### Test 1

```
3
6 3
4 2
3 1
```

### Test 2

```
YES
NO 2
YES
```
