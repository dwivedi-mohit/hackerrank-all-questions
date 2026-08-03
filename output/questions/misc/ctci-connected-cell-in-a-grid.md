# DFS: Connected Cell in a Grid

---

| Field | Value |
|---|---|
| **Slug** | `ctci-connected-cell-in-a-grid` |
| **Domain** |  |
| **Difficulty** | Hard |
| **Score** | 45 |
| **URL** | https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid |

---

## Preview

Find the largest connected region in a 2D Matrix.

## Problem Statement

Consider a matrix where each cell contains either a $0$ or a $1$ and any cell containing a $1$ is called a *filled* cell. Two cells are said to be *connected* if they are adjacent to each other horizontally, vertically, or diagonally.  In the diagram below, the two colored regions show cells connected to the filled cells.  Black on white are not connected.

Cells adjacent to filled cells:  ![image](https://s3.amazonaws.com/hr-assets/0/1528204809-ea89cbdef6-connected.png)


If one or more filled cells are also connected, they form a *region*. Note that each cell in a region is connected to at least one other cell in the region but is not necessarily directly connected to all the other cells in the region.

Regions:  ![image](https://s3.amazonaws.com/hr-assets/0/1528205314-6fa4d1c8c7-connected2.png)


Given an $n \times m$ matrix, find and print the number of cells in the largest *region* in the matrix.


**Function Description**

Complete the function *maxRegion* in the editor below.  It must return an integer value, the size of the largest region.

maxRegion has the following parameter(s):


- *grid*: a two dimensional array of integers

## Input Format

The first line contains an integer, $n$, the number of rows in the matrix, $grid$.		
The second line contains an integer, $m$, the number of columns in the matrix.	

Each of the following $n$ lines contains a row of $m$ space-separated integers, $grid[i][j]$.

## Output Format

Print the number of cells in the largest *region* in the given matrix.

## Constraints

- $0 \lt n, m \lt 10$

- $grid[i][j] \in \{0,1\}$

## Sample Tests

### Test 1

```
4
4
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0
```

### Test 2

```
5
```
