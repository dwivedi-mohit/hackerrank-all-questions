# Possible Path

---

| Field | Value |
|---|---|
| **Slug** | `possible-path` |
| **Domain** | mathematics |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/possible-path |

---

## Preview

Help Adam in reaching at aa particular point.

## Problem Statement

Adam is standing at point $(a, b)$ in an infinite 2D grid. He wants to know if he can reach point $(x, y)$ or not. The only operation he can do is to move to point $(a + b, b), (a, a + b), (a - b, b), \text{or} (a, b - a)$ from some point $(a, b)$. It is given that he can move to any point on this 2D grid, i.e., the points having positive or negative $X$(or $Y$) co-ordinates.


Tell Adam whether he can reach $(x, y)$ or not.

## Input Format

The first line contains an integer, $T$, followed by $T$ lines, each containing $4$ space-separated integers i.e. $a$, $b$, $x$ and $y$.

## Output Format

For each test case, display `YES` or `NO` that indicates if Adam can reach $(x,y)$ or not.

## Constraints

- $1 \le T \le 1000$

- $1 \le a,b,x,y \le 10^{18}$

## Sample Tests

### Test 1

```
3
1 1 2 3
2 1 2 3
3 3 1 1
```

### Test 2

```
YES
YES
NO
```
