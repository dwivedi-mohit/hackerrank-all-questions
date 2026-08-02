# Flipping the Matrix

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.9199701659518926
- **Total Submissions:** 26815
- **Solved Count:** 24669
- **URL:** https://www.hackerrank.com/challenges/flipping-the-matrix

## Problem Statement

Sean invented a game involving a $2n \times 2n$ matrix where each cell of the matrix contains an integer. He can reverse any of its rows or columns any number of times.  The goal of the game is to maximize the sum of the elements in the $n \times n$ submatrix located in the upper-left quadrant of the matrix.

Given the initial configurations for $q$ matrices, help Sean reverse the rows and columns of each matrix in the best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.  

**Example**  
$matrix = [[1, 2], [3, 4]]$  

```
1 2
3 4
```
It is $2 \times 2$ and we want to maximize the top left quadrant, a $1 \times 1$ matrix.  Reverse row $1$:
```
1 2
4 3
```
And now reverse column $0$:
```
4 2
1 3
```
The maximal sum is $4$.

**Function Description**  

Complete the *flippingMatrix* function in the editor below.  

flippingMatrix has the following parameters:  
- *int matrix[2n][2n]:* a 2-dimensional array of integers  

**Returns**  
- *int:* the maximum sum possible.   

## Input Format

The first line contains an integer $q$, the number of queries.   

The next $q$ sets of lines are in the following format:

- The first line of each query contains an integer, $n$. 
- Each of the next $2n$ lines contains $2n$ space-separated integers $matrix[i][j]$ in row $i$ of the matrix.  

## Constraints

+ $1 \le q \le 16$  
+ $1 \le n \le 128$  
+ $0 \le matrix[i][j] \le 4096$, where $0 \le i, j \lt 2n$.

## Sample Input

STDIN           Function
-----           --------
1               q = 1
2               n = 2
112 42 83 119   matrix = [[112, 42, 83, 119], [56, 125, 56, 49], \
56 125 56 49              [15, 78, 101, 43], [62, 98, 114, 108]]
15 78 101 43
62 98 114 108

## Explanation

Start out with the following  matrix:

Perform the following operations to maximize the sum of the  submatrix in the upper-left quadrant:

- Reverse column  (), resulting in the matrix:

- Reverse row  (), resulting in the matrix:

The sum of values in the  submatrix in the upper-left quadrant is .

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
