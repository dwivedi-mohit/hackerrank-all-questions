# Down to Zero II

---

| Field | Value |
|---|---|
| **Slug** | `down-to-zero-ii` |
| **Domain** | data-structures |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/down-to-zero-ii |

---

## Preview

Find the minimum number of moves to reduce N to zero using the constraints given.

## Problem Statement

You are given $Q$ queries. Each query consists of a single number $N$. You can perform any of the $2$ operations on $N$ in each move:

1: If we take 2 integers $a$ and $b$ where $N = a\times b$$(a \ne 1$, $b \ne 1)$, then we can change $N=max(a,b)$

2: Decrease the value of $N$ by $1$. 

Determine the minimum number of moves required to reduce the value of $N$ to $0$.

## Input Format

The first line contains the integer $Q$. <br>
The next $Q$ lines each contain an integer, $N$.

## Output Format

Output $Q$ lines. Each line containing the minimum number of moves required to reduce the value of $N$ to $0$.

## Constraints

$1 \le Q \le 10^3$

$0 \le N \le 10^6$

## Sample Tests

### Test 1

```
2
3
4
```

### Test 2

```
3
3
```
