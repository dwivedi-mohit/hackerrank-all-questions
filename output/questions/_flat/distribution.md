# Special Set Pairs

---

| Field | Value |
|---|---|
| **Slug** | `distribution` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 65 |
| **Contest** | 101hack55 |
| **URL** | https://www.hackerrank.com/challenges/distribution |

---

## Preview

Find the number of pairs of special sets.

## Problem Statement

Toph has an integer array $a$ with $n$ elements, indexed from $1$ to $n$. The function $f(x, y)$ is defined as follows:


$$f(x, y) = \begin{cases} \max(0, a_x) &\text{if }x = y \\ \max(0, f(x, y - 1) + a_y) &\text{otherwise} \end{cases}$$

A pair of sets $(X, Y)$ is called *special* if it satisfies the following conditions:

  

- $X$ and $Y$ are nonempty and contain only elements in range $[1\ldots n]$.
- Every number is contained in at most one of the sets $X$ and $Y$.
- Every element of set $X$ is smaller than every element of set $Y$.

- For every element $x$ of $X$ and every element $y$ of $Y$, $f(x, y) = 0$.

  

Toph wants to find the number of special pairs of sets. Since this number can be very large, you have to give Toph the answer modulo $10^9 + 7$.

Two pairs $(X, Y)$ and $(X', Y')$ are different if $X$ and $X'$ are different sets or $Y$ and $Y'$ are different sets (or both).


Complete the function `specialSetPairs` which takes in an integer array $a$ and returns the number of special pairs of sets modulo $10^9 + 7$.

## Input Format

The first line contains a single integer $n$. The second line contains $n$ space-separated integers $a_1, a_2, \ldots, a_n$.

## Output Format

Print a single line containing a single integer denoting the number of special set pairs modulo $10^9 + 7$.

## Constraints

- $2 \leq n \leq 10^6$
- $-2\cdot 10^9 \le a_i \le 2\cdot 10^9$

## Sample Tests

### Test 1

```
6
5 -2 -4 2 5 -6
```

### Test 2

```
4
```
