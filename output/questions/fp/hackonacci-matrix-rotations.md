# Hackonacci Matrix Rotations

- **Domain:** fp
- **Difficulty:** Medium
- **Max Score:** 35
- **Success Ratio:** 0.7569230769230769
- **Total Submissions:** 325
- **Solved Count:** 246
- **URL:** https://www.hackerrank.com/challenges/hackonacci-matrix-rotations

## Problem Statement

We define a $hackonacci$ series as follows:

- $hackonacci(n) = 1 \cdot hackonacci(n-1) + 2 \cdot hackonacci(n-2) + 3 \cdot hackonacci(n - 3)$   
- $hackonacci(1) = 1$  
- $hackonacci(2) = 2$  
- $hackonacci(3) = 3$  

We define a *Hackonacci Matrix* to be an $n \times n$ matrix where the rows and columns are indexed from $1$ to $n$, and the top-left cell is $(1, 1)$. Each cell $(i, j)$ must contains either the character `X` or the character `Y`. If $hackonacci((i \cdot j)^2)$ is *even*, it's `X`; otherwise, it's `Y`.

Next, we want to perform $q$ queries where each query $i$ consists of an integer, $angle_i$. Each $angle_i$ is a multiple of $90$ degrees and describes the angle by which you must rotate the matrix in the *clockwise* direction. For each $angle_i$, we want to count the number of cells that are different after the rotation. For example, the diagram below depicts the $270°$ rotation of a Hackonacci Matrix when $n = 2$: 

![image](https://s3.amazonaws.com/hr-challenge-images/0/1482182705-de67dcb0f0-hackonacci-matrix-ps.png)

As you can see, there are two cells whose values change after the rotation. Note that we filled each initial cell using the Hackonacci formula given above:

- $(1, 1)$: $hackonacci((1 \cdot 1)^2) = hackonacci(1) = 1$			
	Because this is an odd number, we mark this cell with a `Y`.
- $(1, 2)$: $hackonacci((1 \cdot 2)^2) = hackonacci(4) \\ \Rightarrow 1 \cdot hackonacci(3) + 2 \cdot hackonacci(2) + 3 \cdot hackonacci(1) \\ \Rightarrow 1 \cdot 3 + 2 \cdot 2 + 3 \cdot 1 = 3 + 4 + 3 = 10$	
	Because this is an even number, we mark this cell with an `X`.
- $(2, 1)$: $hackonacci((2 \cdot 1)^2) = hackonacci(4) \Rightarrow 10$	
	Because this is an even number, we mark this cell with an `X`.
- $(2, 2)$: $hackonacci((2 \cdot 2)^2) = hackonacci(16) \Rightarrow 296578$			
	Because this is an even number, we mark this cell with an `X`.
    
Given the value of $n$ and $q$ queries, construct a Hackonacci Matrix and answer the queries. For each query $i$, print an integer on a new line denoting the number of cells whose values differ from the initial Hackonacci Matrix when it's rotated by $angle_i$ degrees in the clockwise direction. 

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ and $q$.  
Each line $i$ of the $q$ subsequent lines contains an integer denoting $angle_i$.

## Output Format

For each $angle_i$, print a single integer on a new line denoting the number of different cells that differ between the initial matrix and the matrix rotated by $angle_i$ degrees.

## Constraints

+ $1 \le n \le 2000$  
+ $1 \le q \le 10^4$  
+ $0 \le angle_i \le 10^5$  
+ It is guaranteed that each $angle_i$ is multiple of $90$ degrees.

## Sample Input

4 3
90
180
270

## Sample Output

10
6
10

## Explanation

Because , we must build a  Hackonacci matrix and then perform  queries, shown below. The following diagrams depict each query rotation, and cells whose values changed after performing a rotation are highlighted in orange:

- When we perform a  rotation on the matrix, there are  cells whose  values change:

Thus, we print  on a new line.

- When we perform a  rotation on the matrix, there are  cells whose  values change:

Thus, we print  on a new line.

- When we perform a  rotation on the matrix, there are  cells whose  values change:

Thus, we print  on a new line.
