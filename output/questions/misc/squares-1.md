# Squares and Points

---

| Field | Value |
|---|---|
| **Slug** | `squares-1` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 80 |
| **Contest** | 101hack28 |
| **URL** | https://www.hackerrank.com/challenges/squares-1 |

---

## Preview

You are given N squares and M points. Each square has the same length size L. Find the maximum value of function f, where the f(P) is equal to the number of given squares that contain point P, and P is one of the given points.

## Problem Statement

Our friends are tired, so you need to solve another easy task for them.

You are given $n$ squares. Each square is described with coordinates of its bottom left corner and the length of its side; the  $i$<sup>$th$</sup> square has bottom left corner with coordinates $(x_i, y_i)$ and side with length exactly $l$ (all squares have the same side length). No two squares will have the same bottom left corner.

Let's define function $f$ as follows: $f(A)$ is equal to the number of squares from given set that contain the point $A$. A square contains the point $A$ if $A$ is located inside the square or on the square borders.

You are also given a set of $m$ points. Find the maximum value of function $f(P)$, where $P$ is some point from the given set. No two points will have the same coordinates.

**Input Format**<br>

The first line of input contains three numbers $n$, $m$, and $l$ ($1 \leq n, m \leq 10^5$, $1 \leq l \leq 10^9$), the number of squares, the number of points, and the side length of each square.

The next $n$ lines contain two numbers $x_i$, $y_i$ ($0 \leq x_i, y_i \leq 10^9$) - $x$ and $y$ coordinates of bottom left corner of the $i$<sup>$th$</sup> square.

The next $m$ lines contain two numbers $a_i$, $b_i$ ($0 \leq a_i, b_i \leq 10^9$) - $x$ and $y$ coordinates of each point.

It is guaranteed that no two of the given squares will have the same bottom left corner and no two of the given points will have the same coordinates.


**Output Format**<br>

In a single line print one integer number, the maximum value of function $f$ for given set of $m$ points.

**Sample Input 1:**<br>

    3 2 2
    2 3
    2 2
    4 0
    3 3
    5 1

**Sample Output 1:**<br>

	2

**Sample Input 2:**<br>

    2 3 1
    0 0
    1 1
    2 3
    3 0
    0 4

**Sample Output 2:**<br>

	0

## Sample Tests

### Test 1

```
3 2 2
2 3
2 2
4 0
3 3
5 1
```

### Test 2

```
2
```

### Test 3

```
2 3 1
0 0
1 1
2 3
3 0
0 4
```

### Test 4

```
0
```
