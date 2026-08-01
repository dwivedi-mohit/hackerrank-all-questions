# Grid Walking

- **Domain:** regex
- **Difficulty:** Medium
- **Max Score:** 55
- **Success Ratio:** 0.6147925661723297
- **Total Submissions:** 5327
- **Solved Count:** 3275
- **URL:** https://www.hackerrank.com/challenges/grid-walking

## Problem Statement

You are situated in an $n$ dimensional grid at position $(x[1],x[2],...,x[n])$. The dimensions of the grid are $(D[1],D[2],...D[n])$. In one step, you can walk one step ahead or behind in any one of the $n$ dimensions. This implies that there are always $2\times n$ possible moves if movements are unconstrained by grid boundaries. How many ways can you take $m$ steps without leaving the grid at any point? You leave the grid if at any point $x[i]$, either $x[i] \le 0$ or $x[i] > D[i]$.

For example, you start off in a 3 dimensional grid at position $x = [2, 2, 2]$.  The dimensions of the grid are $D = [3,3,3]$, so each of your axes will be numbered from $1$ to $3$.  If you want to move $m = 1$ step, you can move to the following coordinates: $\{[1,2,2],[2,1,2],[2,2,1],[3,2,2],[2,3,2],[2,2,3]\}$.    


![image](https://s3.amazonaws.com/hr-assets/0/1526327938-afa87cb1a0-multidimension.png)  
 

If we started at $x=[1, 1, 1]$ in the same grid, our new paths would lead to $\{[1,1,2],[1,2,1],[2,1,1]\}$.  Other moves are constrained by $x[i] \nleq 0$.

**Function Description**

Complete the *gridWalking* function in the editor below.  It should return an integer that represents the number of possible moves, modulo $(10^9+7)$.

gridWalking has the following parameter(s):

- *m*: an integer that represents the number of steps  
- *x*: an integer array where each $x[i]$ represents a coordinate in the $i^{th}$ dimension where $1 \leq i \leq n$
- *D*: an integer array where each $D[i]$ represents the upper limit of the axis in the $i^{th}$ dimension  

## Input Format

The first line contains an integer $t$, the number of test cases.

Each of the next $t$ sets of lines is as follows:

-  The first line contains two space-separated integers, $n$ and $m$.  
-  The next line contains $n$ space-separated integers $x[i]$.  
-  The third line of each test contains $n$ space-separated integers $D[i]$.  


## Output Format

Output one line for each test case. Since the answer can be really huge, output it modulo $10^9+7$.  


## Constraints

- $1 \le t \le 10$
- $1 \le n \le 10$  
- $1 \le m \le 300$  
- $1 \le D[i] \le 100$  
- $1 \le x[i] \le D[i]$  


## Sample Input

2 3
1 1
2 3

## Explanation

We are starting from (1, 1) in a  2-D grid, and need to count the number of possible paths with length equal to .

Here are the  paths:
