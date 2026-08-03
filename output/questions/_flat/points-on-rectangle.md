# Points on a Rectangle

---

| Field | Value |
|---|---|
| **Slug** | `points-on-rectangle` |
| **Domain** | mathematics |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/points-on-rectangle |

---

## Preview

Determine if a set of points coincides with the edges of a non-degenerate rectangle.

## Problem Statement

You are given $q$ queries where each query consists of a set of $n$ points on a two-dimensional plane (i.e., $(x, y)$). For each set of points, print `YES` on a new line if all the points fall on the edges (i.e., sides and/or corners) of a [non-degenerate rectangle](https://en.wikipedia.org/wiki/Degeneracy_(mathematics)#Rectangle) which is axis parallel; otherwise, print `NO` instead.

## Input Format

The first line contains a single positive integer, $q$, denoting the number of queries. The subsequent lines describe each query in the following format:

1. The first line contains a single positive integer, $n$, denoting the number of points in the query.		
2. Each line $i$ of the $n$ subsequent lines contains two space-separated integers describing the respective values of $x_i$ and $y_i$ for the point at coordinate $(x_i, y_i)$.

## Output Format

For each query, print `YES` on a new line if all $n$ points lie on the edges of some non-degenerate rectangle which is axis parallel; otherwise, print `NO` instead.

## Constraints

- $1 \le q \le 10$
- $1 \le n \le 10$
- $-10^4 \le x, y \le 10^4$

## Sample Tests

### Test 1

```
2
3
0 0
0 1
1 0
4
0 0
0 2
2 0
1 1
```

### Test 2

```
YES
NO
```
