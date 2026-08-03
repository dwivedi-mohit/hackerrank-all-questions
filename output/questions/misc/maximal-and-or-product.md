# Maximal And-Or Product

---

| Field | Value |
|---|---|
| **Slug** | `maximal-and-or-product` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 80 |
| **Contest** | 101hack43 |
| **URL** | https://www.hackerrank.com/challenges/maximal-and-or-product |

---

## Preview

Choose two numbers from an array such that the product of their bitwise AND and bitwise OR is maximal.

## Problem Statement

Consider $n$ integers, $a_0, a_1, \ldots, a_{n-1}$. Let $f(i,j)=(a_i \texttt{ & } a_j) \times (a_i \texttt{ | } a_j)$, where $\texttt{&}$ is the [bitwise AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND) operator and $\texttt{|}$ is the [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR) operator.

Choose two *different* indices, $i$ and $j$, such that $f(i,j)$ is maximal. Then print the value of the maximal $f(i,j)$.

## Input Format

The first line contains a single integer denoting $n$.		
The second line contains $n$ space-separated integers describing the respective values of $a_0, a_1, \ldots, a_{n-1}$.

## Output Format

Print the maximal $f(i, j)$.

## Constraints

- For $30\%$ of the test cases:
	- $2\leq n\leq 1000$
- For $100\%$ of the test cases:
	- $2\leq n\leq 10^5$
    - $0\leq a_i\leq 2^{28}$

## Sample Tests

### Test 1

```
5
1 2 3 4 5
```

### Test 2

```
20
```
