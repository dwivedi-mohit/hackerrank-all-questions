# Small Triangles, Large Triangles

---

| Field | Value |
|---|---|
| **Slug** | `small-triangles-large-triangles` |
| **Domain** | c |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/small-triangles-large-triangles |

---

## Preview

Sort triangles by area

## Problem Statement

You are given $n$ triangles, specifically, their sides $a_i$, $b_i$ and $c_i$. Print them in the same style but sorted by their areas from the smallest one to the largest one. It is guaranteed that all the areas are different.

The best way to calculate a area of a triangle with sides $a$, $b$ and $c$ is Heron's formula:

$S = \sqrt{p \times (p-a) \times (p-b) \times (p-c)}$ where $p={\frac {a+b+c} 2}$.

## Input Format

The first line of each test file contains a single integer $n$. $n$ lines follow with three space-separated integers, $a_i$, $b_i$ and $c_i$.

## Output Format

Print exactly $n$ lines. On each line print $3$ space-separated integers, the $a_i$, $b_i$ and $c_i$ of the corresponding triangle.

## Constraints

+ $1 \leq n \leq 100$
+ $1 \leq a_i,b_i,c_i \leq 70$
+ $a_i+b_i>c_i$,$a_i+c_i>b_i$ and $b_i+c_i>a_i$

## Sample Tests

### Test 1

```
3
7 24 25
5 12 13
3 4 5
```

### Test 2

```
3 4 5
5 12 13
7 24 25
```
