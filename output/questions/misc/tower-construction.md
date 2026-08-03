# Tower Construction

---

| Field | Value |
|---|---|
| **Slug** | `tower-construction` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 45 |
| **Contest** | 101hack55 |
| **URL** | https://www.hackerrank.com/challenges/tower-construction |

---

## Preview

Construct additional towers so that the condition is satisfied.

## Problem Statement

Taang wants to build some new towers to strengthen his city's defense. The city can be considered as an infinite 2D grid. Initially, his city has $n$ towers, and the $i^\text{th}$ of them is in cell $(x_i, y_i)$. From any cell, one can only go towards the four cardinal directions.


- All cells containing towers are *simply connected*, i.e., every tower-containing cell is reachable from every other tower-containing cell by only passing through tower-containing cells. 
- All cells not containing towers are also simply connected, i.e., every non-tower-containing cell is reachable from every other non-tower-containing cell by only passing through non-tower-containing cells.


Taang wants towers to be as close as possible. Thus, he decides to build new towers such that for each pair of towers $(i, j)$ such that $1 \le i, j \le m$ (where $m$ is the number of towers after construction), the distance between tower $i$ and $j$ must be $|x_i - x_j| + |y_i - y_j|$. The *distance* between two towers $(i, j)$ is defined as the number of movements needed to go from $i$ to $j$ by only passing through tower-containing cells.


He wants your help to find the minimum number of towers that need to be constructed so that his condition is satisfied.

Complete the function `fewestTowers` which takes in two integers array $x$ and $y$ (denoting the x- and y-coordinates of the initial towers, respectively) and returns the minimum number of towers that need to be constructed so that the condition is satisfied.

## Input Format

The first line contains a single integer $n$.

The next line contains $n$ integers $x_1, x_2, \ldots, x_n$. $x_i$ is the $x$-coordinate of the $i^\text{th}$ tower.


The next line contains $n$ integers $y_1, y_2, \ldots, y_n$. $y_i$ is the $y$-coordinate of the $i^\text{th}$ tower.

## Output Format

Print a single line containing a single integer denoting the minimum number of towers that need to be constructed.

## Constraints

- $1 \leq n \leq 5\times10^5$
- $-10^9 \le x_i, y_i \le 10^9$ (but new towers can be placed in any integer coordinates)

## Sample Tests

### Test 1

```
10
-1 0 0 0 1 -1 -1 1 0 -2
2 0 2 3 3 3 1 0 1 2
```

### Test 2

```
2
```

### Test 3

```
6
1 1 2 3 3 3
2 1 1 1 2 3
```

### Test 4

```
1
```
