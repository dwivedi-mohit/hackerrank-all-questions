# Points On a Line

---

| Field | Value |
|---|---|
| **Slug** | `points-on-a-line` |
| **Domain** | mathematics |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/points-on-a-line |

---

## Preview

Given a set of coordinates, determine if they fall in an horizontal or vertical line.

## Problem Statement

Given $n$ two-dimensional points in space, determine whether they lie on some vertical or horizontal line. If yes, print *YES*; otherwise, print *NO*.

## Input Format

The first line contains a single positive integer, $n$, denoting the number of points.		
Each line $i$ of $n$ subsequent lines contain two space-separated integers detailing the respective values of $x_i$ and $y_i$ (i.e., the coordinates of the $i^{th}$ point).

## Output Format

Print *YES* if all points lie on some horizontal or vertical line; otherwise, print *NO*.

## Constraints

- $2 \le n \le 10$
- $-10 \le x_i, y_i \le 10$

## Sample Tests

### Test 1

```
5
0 1
0 2
0 3
0 4
0 5
```

### Test 2

```
YES
```

### Test 3

```
5
0 1
0 2
1 3
0 4
0 5
```

### Test 4

```
NO
```
