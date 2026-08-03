# Washing Plates

---

| Field | Value |
|---|---|
| **Slug** | `washing-plates` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 30 |
| **Contest** | 101hack41 |
| **URL** | https://www.hackerrank.com/challenges/washing-plates |

---

## Preview

Determine the maximum number of plates that will be washed

## Problem Statement

Harold is a dishwasher at a restaurant with $n$ dirty plates. Each plate $i$ has  two integers associated with it:

1. $p_i$ denotes the amount of money Harold is *paid* if he washes the plate.
2. $d_i$ denotes the amount of money *deducted* from Harold's paycheck if he doesn't wash the plate.

Harold only has time to wash *at most* $k$ plates, so he wants to *maximize* the amount of money he earns during his shift. Given $n$, $k$, and arrays $P = [p_0, p_1, \ldots, p_{n - 1}]$ and $D = [d_0, d_1, \ldots, d_{n - 1}]$ of $n$ non-negative integers, find and print the maximum amount of money Harold can earn. If his income is negative, print $0$ instead.

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of dirty plates) and $k$ (the number of plates Harold has time to wash.		
Each line $i$ of the $n$ subsequent lines contains two space-separated integers denoting the respective values of $p_i$ and $d_i$.

## Output Format

Print a single integer denoting the maximum amount of money Harold can earn by washing *at most* $k$ plates; if his income is negative, print $0$ instead.

## Constraints

- $1 \le n, k \le 2 \times 10^5$
- $0 \le p_i, d_i \le 10^9$
- For $\text{40%}$ of the maximum score, $n \le 2000$.

## Sample Tests

### Test 1

```
2 1
10 5
3 1
```

### Test 2

```
9
```
