# Number of integers

---

| Field | Value |
|---|---|
| **Slug** | `maximum-or-1` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 40 |
| **Contest** | hack-the-interview-iv |
| **URL** | https://www.hackerrank.com/challenges/maximum-or-1 |

---

## Preview

dp

## Problem Statement

Given two large integers, L and R, find the number of integers greater than L and less than or equal to R exactly K non-zero digits.

For example, consider the two integers to be, $L = 2$ and $R = 15$ and $K = 1$, the integers [3, 4, 5, 6, 7, 8, 9, 10] contain exactly 1 non-zero digit. 

As the answer can be rather large, print it modulo $10^{9}+7$.

## Input Format

The input contains three lines, each containing a single integer denoting L, R and K respectively.

## Output Format

Print a single integer, denoting the number of integers.

## Constraints

- $1 \le L \le R \le 10^{100}$
- $1 \le K \le 100$

## Sample Tests

### Test 1

```
1
100
1
```

### Test 2

```
18
```

### Test 3

```
10
55
2
```

### Test 4

```
41
```
