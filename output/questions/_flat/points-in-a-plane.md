# Points in a Plane

---

| Field | Value |
|---|---|
| **Slug** | `points-in-a-plane` |
| **Domain** | algorithms |
| **Difficulty** | Advanced |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/points-in-a-plane |

---

## Preview

What's the minimum number of turns needed to remove collinear points in a plane?

## Problem Statement

There are N points on an XY plane. In one turn, you can select a set of collinear points on the plane and remove them. Your goal is to remove all the points in the least number of turns. Given the coordinates of the points, calculate two things:

- The minimum number of turns (T) needed to remove all the points.
- The number of ways to to remove them in T turns. Two ways are considered different if any point is removed in a different turn.

## Input Format

The first line contains the number of test cases T. T test cases follow. Each test case contains N on the first line, followed by N lines giving the coordinates of the points.

## Output Format

Output T lines, one for each test case, containing the least number of turns needed to remove all points and the number of ways to do so. As the answers can be large, output them modulo 1000000007.

## Constraints

1 <= T <= 50

1 <= N <= 16

0 <= xi,yi <= 100

No two points will have the same coordinates.

## Sample Tests

### Test 1

```
2 
3 
0 0 
0 1 
1 0 
4 
3 4 
3 5 
3 6 
5 5
```

### Test 2

```
2 6 
2 8
```
