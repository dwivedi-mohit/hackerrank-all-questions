# XOR Point Weights in Circles

---

| Field | Value |
|---|---|
| **Slug** | `xor-point-weights-in-circles` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 50 |
| **Contest** | 101hack43 |
| **URL** | https://www.hackerrank.com/challenges/xor-point-weights-in-circles |

---

## Preview

Given a set of points, XOR the sum weights of all the points that are inside all the possible circles.

## Problem Statement

Consider $n \cdot m$ points, where each point $(x, y)$ has a weight, $w_{x,y}$.

Let $f(x,y,r)$ denote the sum weight of every point in circle $(x, y, r)$. Point $(a, b)$ is in circle $(x, y, r)$ if and only if $(a - x)^2 + (b - y)^2 \le r^2$

Given the set of points, calculate $f(x, y, r)$ for every point $(x, y)$ where $x \in [0, n)$ and $y \in [0, m)$. Then print an integer denoting the [XOR](https://en.wikipedia.org/wiki/Exclusive_or) of all the $f(x, y, r)$ values.

## Input Format

The first line contains three space-separated integers describing the respective values of $n$, $m$, and $r$. 		
Each line $i$ of the $n$ subsequent lines contains $m$ space-separated integers describing the respective values of $w_{i - 1, 0} \ldots w_{i - 1, m - 1}$.

## Output Format

Print an integer denoting the XOR of all $f(x, y, r)$.

## Constraints

- For $40\%$ of the test cases:
	- $1\leq n, m \leq 10$.
- For $100\%$ of the test cases:
	- $1\leq n, m \leq 300$
    - $0\leq r \leq 1000$
    - $0 \leq w_{i,j} \leq 10^4$.

## Sample Tests

### Test 1

```
2 2 1
1 2
3 4
```

### Test 2

```
0
```
