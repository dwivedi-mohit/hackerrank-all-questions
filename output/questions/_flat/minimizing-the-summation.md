# Minimizing the Summation

---

| Field | Value |
|---|---|
| **Slug** | `minimizing-the-summation` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 30 |
| **Contest** | 101hack43 |
| **URL** | https://www.hackerrank.com/challenges/minimizing-the-summation |

---

## Preview

Choose $k$ numbers such that the result of the summation is minimal.

## Problem Statement

Given $n$ numbers, $a_0, a_1, \ldots, a_{n-1}$, choose exactly $k$ numbers, $b_0, b_1, \ldots, b_{k-1}$, such that the value of $ans$ below is minimal:
$$ans = \sum\limits_{i=0}^{k-1}\sum_{j=0}^{k-1}(b_i-b_j)^2$$

Find and print the minimal value of $ans$.

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ and $k$. 		
The second line contains $n$ space-separated integers describing the respective values of $a_0, a_1, \ldots, a_{n-1}$.

## Output Format

Print the minimal value of $ans$ on a new line.

## Constraints

- For $50\%$ of the test cases, $1\leq k\leq n\leq 1000$.
- For $100\%$ of the test cases, $1\leq k\leq n\leq 10^5$, $0\leq a_i\leq 10^3$.

## Sample Tests

### Test 1

```
4 2
2 0 9 5
```

### Test 2

```
8
```
