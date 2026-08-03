# Project Euler #15: Lattice paths

---

| Field | Value |
|---|---|
| **Slug** | `euler015` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 100 |
| **Contest** | projecteuler |
| **URL** | https://www.hackerrank.com/challenges/euler015 |

---

## Preview

Walking on grids. And not slipping.

## Problem Statement

<sub>This problem is a programming version of [Problem 15](https://projecteuler.net/problem=15) from [projecteuler.net](https://projecteuler.net/)</sub>


Starting in the top left corner of a $2 \times 2$ grid, and only being able to move to the right and down, there are exactly $6$ routes to the bottom right corner.

![](https://hr-challenge-images.s3.amazonaws.com/2641/2641.gif)


How many such routes are there through a $N \times M$  grid? As number of ways can be very large, print it modulo $(10^9+7)$.

## Input Format

The first line contains an integer $T$ , i.e., number of test cases.

Next $T$ lines will contain integers $N$ and $M$.

## Output Format

Print the values corresponding to each test case.

## Constraints

+ $1 \leqslant T  \leqslant 10^3$

+ $1 \leqslant N  \leqslant 500$

+ $1 \leqslant M  \leqslant 500$

## Sample Tests

### Test 1

```
2
2 2
3 2
```

### Test 2

```
6
10
```
