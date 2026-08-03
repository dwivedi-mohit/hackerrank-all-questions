# Concave Polygon

---

| Field | Value |
|---|---|
| **Slug** | `lambda-march-concave-polygon` |
| **Domain** | fp |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/lambda-march-concave-polygon |

---

## Preview

Determine if P is a concave polygon.

## Problem Statement

You are given the cartesian coordinates of a set of points in a $\text{2D}$ plane (in no particular order). Each of these points is a corner point of some Polygon, $P$, which is not self-intersecting in nature. Can you determine whether or not $P$ is a [concave polygon](https://en.wikipedia.org/wiki/Concave_polygon)?

## Input Format

The first line contains an integer, $N$, denoting the number of points.		
The $N$ subsequent lines each contain $2$ space-separated integers denoting the respective $x$ and $y$ coordinates of a point.

## Output Format

Print $\scriptsize{\texttt{YES}}$ if $P$ is a concave polygon; otherwise, print $\scriptsize{\texttt{NO}}$.

## Constraints

- $3 \le N \le 1000$
- $0 \le x,y \le 1000$

## Sample Tests

### Test 1

```
4
0 0
0 1 
1 1 
1 0
```

### Test 2

```
NO
```

### Test 3

```
100 - 2*(percentage of tests which you solve incorrectly)
```
