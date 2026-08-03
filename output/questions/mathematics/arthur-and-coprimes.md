# Coprime Conundrum

---

| Field | Value |
|---|---|
| **Slug** | `arthur-and-coprimes` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/arthur-and-coprimes |

---

## Preview

Count the number of (p, q) pairs such that gcd(p,q) =1 and p &times; q &le; n;

## Problem Statement

Arthur defines a function, $f(k)$, to be the number of $(p, q)$ pairs such that:

* $1 \lt p \le q \le k$
* $p$ and $q$ are [coprime](https://en.wikipedia.org/wiki/Coprime_integers).
* $p \cdot q = k$


Given an integer, $n$, help Arthur find and print the result of: 
$$\sum_{k = 1}^{n} f(k)$$

## Input Format

The first line contains a single integer denoting $n$.

## Output Format

Print the result of $\sum_{k = 1}^{n} f(k)$ on a new line.

## Constraints

* $ 1 \le n \le 10^9$

**Subtasks**

* $ 1 \le n \le 150$ for $\text{30%}$ of the maximum score.
* $ 1 \le n \le 10^6$ for $\text{60%}$ of the maximum score.

## Sample Tests

### Test 1

```
12
```

### Test 2

```
3
```
