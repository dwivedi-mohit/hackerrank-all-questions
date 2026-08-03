# Twisty Tuple

---

| Field | Value |
|---|---|
| **Slug** | `twisty-tuple` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 60 |
| **Contest** | 101hack24 |
| **URL** | https://www.hackerrank.com/challenges/twisty-tuple |

---

## Preview

Help Bidhan find the number of twisty tuples.

## Problem Statement

Bidhan is trying to find twisty tuples in an array $A$.


A twisty tuple is a tuple of three numbers $A_i$, $A_j$, and $A_k$ such that $A_k<A_i<A_j$ and $i<j<k$.

<img src="https://s3.amazonaws.com/hr-challenge-images/7782/1429959053-a7eb2623a5-UntitledDiagram1.jpg" title="Visualization of a twisty tuple." />

Given $A$, tell Bidhan how many twisty tuples exist in that array.

## Input Format

The first line of input contains $N$, the number of integers in array $A$.

The next line will contain $N$ space-separated integers, the $i^{th}$ of which denoting $A_i$.

**Constraints**


$1\le N \le 5 \times 10^3$

$1\le A_i \le 10^9$

## Output Format

Print the number of twisty tuples in a separate line.

## Sample Tests

### Test 1

```
6
1 6 3 4 7 4
```

### Test 2

```
1
```
