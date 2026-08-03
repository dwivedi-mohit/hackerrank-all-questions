# Baby Step, Giant Step

---

| Field | Value |
|---|---|
| **Slug** | `baby-step-giant-step` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/baby-step-giant-step |

---

## Preview

Find the minimum number of steps needed to get to point $(d, 0)$.

## Problem Statement

You are standing at point $(0, 0)$ on an infinite plane. In one step, you can move from some point $(x_{f}, y_{f})$ to any point $(x_{t}, y_{t})$ *as long as* the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance), $\sqrt{(x_{f}-x_{t})^2+(y_{f}-y_{t})^2}$, between the two points is either $a$ or $b$. In other words, each step you take must be exactly $a$ or $b$ in length.

You are given $q$ queries in the form of $a$, $b$, and $d$. For each query, print the minimum number of steps it takes to get from point $(0, 0)$ to point $(d, 0)$ on a new line.

## Input Format

The first line contains an integer, $q$, denoting the number of queries you must process.	
Each of the $q$ subsequent lines contains three space-separated integers describing the respective values of $a$, $b$, and $d$ for a query.

## Output Format

For each query, print the minimum number of steps necessary to get to point $(d, 0)$ on a new line.

## Constraints

- $1 \le q \le 10^5$
- $1 \le a < b \le 10^9$
- $0 \le d \le 10^9$

## Sample Tests

### Test 1

```
3
2 3 1
1 2 0
3 4 11
```

### Test 2

```
2
0
3
```
