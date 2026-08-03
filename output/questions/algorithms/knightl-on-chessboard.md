# KnightL on a Chessboard

---

| Field | Value |
|---|---|
| **Slug** | `knightl-on-chessboard` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 35 |
| **URL** | https://www.hackerrank.com/challenges/knightl-on-chessboard |

---

## Preview

Find the shortest path from the top-left corner of a chessboard to the bottom-right corner for each KnightL(a, b).

## Problem Statement

$KnightL$ is a chess piece that moves in an `L` shape. We define the possible moves of $KnightL(a, b)$ as any movement from some position $(x_1, y_1)$ to some $(x_2, y_2)$ satisfying either of the following:

- $x_2 = x_1 \pm a$ and $y_2 = y_1 \pm b$, or

- $x_2 = x_1 \pm b$ and $y_2 = y_1 \pm a$


Note that $(a, b)$ and $(b, a)$ allow for the same exact set of movements. For example, the diagram below depicts the possible locations that $KnightL(1,2)$ or $KnightL(2,1)$ can move to from its current location at the center of a $5 \times 5$ chessboard:

![image](https://s3.amazonaws.com/hr-assets/0/1486410238-98ef4547f1-knightl-example-ps.png)

Observe that for each possible movement, the Knight moves $2$ units in one direction (i.e., horizontal or vertical) and $1$ unit in the perpendicular direction.

Given the value of $n$ for an $n \times n$ chessboard, answer the following question for each $(a, b)$ pair where $1 \le a, b \lt n$:

- What is the minimum number of moves it takes for $KnightL(a,b)$ to get from position $(0, 0)$ to position $(n-1, n-1)$? If it's not possible for the Knight to reach that destination, the answer is `-1` instead.

Then print the answer for each $KnightL(a, b)$ according to the *Output Format* specified below.

## Input Format

A single integer denoting $n$.

## Output Format

Print exactly $n-1$ lines of output in which each line $i$ (where $1 \le i \lt n$) contains $n - 1$ space-separated integers describing the minimum number of moves $KnightL(i,j)$ must make for each respective $j$ (where $1 \le j \lt n$). If some $KnightL(i,j)$ cannot reach position $(n-1, n-1)$, print `-1` instead.


For example, if $n = 3$, we organize the answers for all the $(i, j)$ pairs in our output like this:

    (1,1) (1,2)
    (2,1) (2,2)

## Constraints

+ $5 \leq n \leq 25$

## Sample Tests

### Test 1

```
(1,1) (1,2)
(2,1) (2,2)
```

### Test 2

```
5
```

### Test 3

```
4 4 2 8
4 2 4 4
2 4 -1 -1
8 4 -1 1
```
