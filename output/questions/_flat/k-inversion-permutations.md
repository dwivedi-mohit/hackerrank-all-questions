# K-Inversion Permutations

---

| Field | Value |
|---|---|
| **Slug** | `k-inversion-permutations` |
| **Domain** | misc |
| **Difficulty** | Expert |
| **Score** | 100 |
| **Contest** | 101hack43 |
| **URL** | https://www.hackerrank.com/challenges/k-inversion-permutations |

---

## Preview

Find the number of permutations satisfying some conditions.

## Problem Statement

Let $f(P)$ denote the number of [inversions](https://en.wikipedia.org/wiki/Permutation#Inversions) in some permutation, $P$. Calculate the number of permutations satisfying the following conditions:

1. $P$ is a permutation of $\{1, 2, \ldots, n\}$.
2. $f(P) = k$

Given $n$ and $k$, find and print the number of permutations of $\{1, 2, \ldots, n\}$ having $k$ inversions. As this value can be quite large, your answer must be modulo $10^9+7$.

## Input Format

A single line of two space-separated integers describing the respective values of $n$ and $k$.

## Output Format

Print a single integer denoting the number of permutations having $k$ inversions, modulo $10^9+7$.

## Constraints

- For $\text{100%}$ of the test cases:
    - $1\leq n \leq 10^5$
    - $0\leq k \leq min(C_{n}^{2}, 10^5)$
- For $\text{50%}$ of the test cases:
    - $1\leq n \leq 1000$
    - $0\leq k\leq 1000$

## Sample Tests

### Test 1

```
3 2
```

### Test 2

```
2
```
