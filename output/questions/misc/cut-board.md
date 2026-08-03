# Cut Board

---

| Field | Value |
|---|---|
| **Slug** | `cut-board` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 30 |
| **Contest** | 101hack53 |
| **URL** | https://www.hackerrank.com/challenges/cut-board |

---

## Preview

Fill the cut board with dominoes.

## Problem Statement

A rectangular board of size $n \times m$ has $1 \times 1$ cells. $x$ consecutive cells from the first row starting from the top-left and $y$ consecutive cells from the last row starting from the bottom-right are cut off. Can you fill all the cells of the remaining board using some $2 \times 1$ dominoes such that none overlap or hang off the edge? 
![image](https://s3.amazonaws.com/hr-assets/0/1519386226-90f43b2331-cutboard1.png)

Complete the function `fillBoard` which takes in four integers $n$, $m$, $x$ and $y$ and prints whether the remaining board can be filled with dominoes, and if yes, prints one way to place the dominoes.

## Input Format

The input consists of a single line containing four space-separated integers $n, m, x$ and $y$.

## Output Format

Print `NO` in a single line if you cannot fill all the cells of the cut board using dominoes.


Otherwise, print `YES` in the first line, and a single integer $k$ in the second line denoting the number of dominoes required. 


In the next $k$ lines, print four space-separated integers $x_{i_1}, y_{i_1}, x_{i_2}, y_{i_2}$ denoting the location of the $i^\text{th}$ domino. The x-coordinate corresponds to the row number and the y-coordinate corresponds to the column number.

**Note:**


- If the location of domino is $x_{i_1}, y_{i_1}, x_{i_2}, y_{i_2}$, then it is present at cells $(x_{i_1}, y_{i_1})$ and $(x_{i_2}, y_{i_2})$.

- You can fill the board by placing each domino either vertically or horizontally.

- If there are multiple solutions, you can output any of them.

## Constraints

- $3 \le n, m \le 100$
- $1 \le x, y \lt m$

## Sample Tests

### Test 1

```
3 4 1 3
```

### Test 2

```
YES
4
2 1 3 1
2 2 2 3
1 2 1 3
1 4 2 4
```

### Test 3

```
3 3 2 2
```

### Test 4

```
NO
```
