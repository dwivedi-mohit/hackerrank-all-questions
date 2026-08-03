# Number of M-Coprime Arrays

---

| Field | Value |
|---|---|
| **Slug** | `number-of-m-coprime-arrays` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/number-of-m-coprime-arrays |

---

## Preview

Given n and m, find the number of m-coprime arrays of length n.

## Problem Statement

An array of integers is called $m$-coprime if the following conditions are both satisfied:

- All the integers in the array are positive divisors of $m$.
- Each pair of adjacent elements in the array is [coprime](https://en.wikipedia.org/wiki/Coprime_integers) (i.e., element $i$ is always coprime with element $i + 1$).

Two arrays, $A$ and $B$, of size $n$ are *different* if and only if there exists an index $i$ such that $A[i] \ne B[i]$.

You are given $q$ queries where each query consists of integers $n$ and $m$. For each query, find the number of $m$-coprime arrays of size $n$, modulo $10^9 + 7$, and print it on a new line.

## Input Format

The first line contains an integer, $q$, denoting the number of queries.  

Each of the $q$ subsequent lines contains two space-separated integers describing the respective values of $n$ (the size of the array) and $m$.

## Output Format

For each query, print the number of $m$-coprime arrays of size $n$ modulo $10^9 + 7$ on a new line.

## Constraints

- $1 \le q \le 100 $
- $1 \le n, m \le 10^{18}$

## Sample Tests

### Test 1

```
1
2 6
```

### Test 2

```
9
```
