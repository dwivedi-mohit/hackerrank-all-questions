# 3D Surface Area

---

| Field | Value |
|---|---|
| **Slug** | `3d-surface-area` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/3d-surface-area |

---

## Preview

Find the surface area of a 3D Toy

## Problem Statement

Madison is a little girl who is fond of toys. Her friend Mason works in a toy manufacturing factory . Mason has a 2D board $A$ of size $H \times W$ with $H$ rows and $W$ columns. The board is divided into cells of size $1 \times 1$ with each cell indicated by its coordinate $(i, j)$. The cell $(i, j)$  has an integer $A_{ij}$ written on it. To create the toy Mason stacks $A_{ij}$ number of cubes of size $1 \times 1 \times 1$ on the cell $(i, j)$. 

Given the description of the board showing the values of $A_{ij}$ and that the price of the toy is equal to the 3d surface area find the price of the toy.

## Input Format

The first line contains two space-separated integers $H$ and $W$ the height and the width of the board respectively.

The next  $H$ lines contains $W$ space separated integers. The $j^{th}$ integer in $i^{th}$ line denotes $A_{ij}$.

## Output Format

Print the required answer, i.e the price of the toy, in one line.

## Constraints

- $1 \le H, W \le 100$
- $1 \le A_{i,j} \le 100$

## Sample Tests

### Test 1

```
1 1
1
```

### Test 2

```
6
```

### Test 3

```
3 3
1 3 4
2 2 3
1 2 4
```

### Test 4

```
60
```
