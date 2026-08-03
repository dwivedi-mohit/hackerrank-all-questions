# Minimize the Sum

---

| Field | Value |
|---|---|
| **Slug** | `minimize-the-sum` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 30 |
| **Contest** | 101hack55 |
| **URL** | https://www.hackerrank.com/challenges/minimize-the-sum |

---

## Preview

You have to create an array under certain constraints while minimizing a certain sum.

## Problem Statement

Kokka and Satara are playing a game. In this game, Kokka gives Satara a number $n$ and $n$ pairs of integers, the $i^\text{th}$ of which is $(l_i, r_i)$. Kokka wants Satara to create an array $a$ with length $n$ such that for each $i$ ($1 \le i \le n$), $l_i \le a_i \le r_i$. He also wants Satara to minimize the sum $$\sum\limits_{i=2}^n |a_i - a_{i-1}|.$$ Since Satara is very busy helping Taang save the world, she wants your help to find the minimum sum among all arrays that satisfy Kokka's condition.


Complete the function `minimumSum` which takes in two integer arrays $l$ and $r$ and returns the minimum sum among all arrays that satisfy Kokka's condition.

## Input Format

The first line contains a single integer $n$.

The second line contains $n$ space-separated integers $l_1, l_2, \ldots, l_n$.


The third line contains $n$ space-separated integers $r_1, r_2, \ldots, r_n$.

## Output Format

Print a single integer denoting the minimum sum.

## Constraints

- $2 \leq n \leq 10^5$
- $1 \le l_i \le r_i \le 10^9$

## Sample Tests

### Test 1

```
5
1 2 6 1 2
3 5 8 2 3
```

### Test 2

```
7
```
