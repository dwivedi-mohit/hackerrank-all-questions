# Compute the Area of a Polygon

---

| Field | Value |
|---|---|
| **Slug** | `lambda-march-compute-the-area-of-a-polygon` |
| **Domain** | fp |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/lambda-march-compute-the-area-of-a-polygon |

---

## Preview

Given the coordinates of a polygon, compute its area.

## Problem Statement

You are given the cartesian coordinates of a set of points in a $\text{2D}$ plane. When traversed sequentially, these points form a Polygon, $P$, which is not self-intersecting in nature. Can you compute the area of polygon $P$?

## Input Format

The first line contains an integer, $N$, denoting the number of points.		
The $N$ subsequent lines each contain $2$ space-separated integers denoting the respective $x$ and $y$ coordinates of a point.

## Output Format

For each test case, print the area of $P$ (correct to a scale of one decimal place). 

**Note:** Do not add any leading/trailing spaces or units; it is assumed that your result is in square units.

## Constraints

- No $2$ points are *coincident*, and polygon $P$ is obtained by traversing the points in a counter-clockwise direction.
- $4 \le N \le 1000$  

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
1
```
