# Twins

---

| Field | Value |
|---|---|
| **Slug** | `twins` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/twins |

---

## Preview

How many pairs of twins can you find?

## Problem Statement

Lia is fascinated by anything she considers to be a *twin*. She calls a pairs of positive integers, $i$ and $j$, twins if:

* They are both prime. A [prime](https://en.wikipedia.org/wiki/Prime_number) number is an integer greater than $1$ that has no positive divisors other than $1$ and itself.

* Their absolute difference is exactly equal to $2$ (i.e., $|j - i| = 2$).

Given an inclusive interval of integers from $n$ to $m$, can you help Lia find the number of pairs of twins there are in the interval (i.e., $[n, m]$)? Note that pairs $(i, j)$ and $(j, i)$ are considered to be the same pair.

## Input Format

Two space-separated integers describing the respective values of $n$ and $m$.

## Output Format

Print a single integer denoting the number of pairs of twins.

## Constraints

* $1 \leq n \leq m \leq 10^9$

* $m - n \leq 10^6$

## Sample Tests

### Test 1

```
3 13
```

### Test 2

```
3
```
