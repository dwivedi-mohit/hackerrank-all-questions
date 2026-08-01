# 3D Surface Area

- **Domain:** regex
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.9347510690287111
- **Total Submissions:** 52384
- **Solved Count:** 48966
- **URL:** https://www.hackerrank.com/challenges/3d-surface-area

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


## Sample Input

1 1
1

## Sample Output

6

## Explanation

The surface area of  cube is 6.
