# Unique Colors

---

| Field | Value |
|---|---|
| **Slug** | `unique-colors` |
| **Domain** | data-structures |
| **Difficulty** | Advanced |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/unique-colors |

---

## Preview

Count the number of different colors between all pair of nodes.

## Problem Statement

You are given an unrooted tree of $n$ nodes numbered from $1$ to $n$. Each node $i$ has a color, $c_{i}$. 

Let $d(i, j)$ be the number of different colors in the path between node $i$ and node $j$. For each node $i$, calculate the value of $sum_i$, defined as follows:

$$sum_i= \sum_{j=1}^n d( i, j ) $$

Your task is to print the value of $sum_i$ for each node $1 \le i \le n$.

## Input Format

The first line contains a single integer, $n$, denoting the number of nodes.		
The second line contains $n$ space-separated integers, $c_1, c_2, \ldots, c_n$, where each $c_i$ describes the color of node $i$.		
Each of the $n-1$ subsequent lines contains $2$ space-separated integers, $a$ and $b$, defining an undirected edge between nodes $a$ and $b$.

## Output Format

Print $n$ lines, where the $i^{th}$ line contains a single integer denoting $sum_{i}$.

## Constraints

* $	1 \leq n \leq  10^5 $
* $	1 \leq c_{i} \leq 10^5$

## Sample Tests

### Test 1

```
5
1 2 3 2 3
1 2
2 3
2 4
1 5
```

### Test 2

```
10
9
11
9
12
```
