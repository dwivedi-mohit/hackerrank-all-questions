# Matrix Land

- **Domain:** mathematics
- **Difficulty:** Hard
- **Max Score:** 55
- **Success Ratio:** 0.8022998673153472
- **Total Submissions:** 2261
- **Solved Count:** 1814
- **URL:** https://www.hackerrank.com/challenges/matrix-land

## Problem Statement

You are playing a matrix-based game with the following setup and rules:   

- You are given a matrix $A$ with $n$ rows and $m$ columns. Each cell contains some points. When a player passes a cell their score increases by the number written in that cell and the number in the cell becomes $0$. (If the cell number is positive their score increases, otherwise it decreases.)
- The player starts from any cell in the _first_ row and can move _left_, _right_ or _down_.  
- The game is over when the player reaches the _last_ row and stops moving.  


![image](https://s3.amazonaws.com/hr-assets/0/1509009270-802e706561-1496382547-5dc79ddda5-matrixland.png)  

Print the maximum score that the player can get. 

## Input Format

The first line contains $n$ and $m$. The next $n$ lines contain $m$ numbers each, $j^{th}$ number in $i^{th}$ line denotes the number that is written on cell $A_{i,j}$.  


## Output Format

Print the maximum score that the player can get. 

## Constraints

- $ 1 \le n \times m \le 4 \times 10^6$
- $ -250 \le A_{i,j} \le 250$

**Subtasks**

* for $20\%$ tests $1 \le n,m \le 40$.
* for $20\%$ tests $40 < n,m \le 500$.


## Sample Input

4 5
1 2 3 -1 -2
-5 -8 -1 2 -150
1 2 3 -250 100
1 1 1 1 20

## Sample Output

37

## Explanation

Refer the image given in statement, the path followed is  summing upto .

Note that,  is traversed  times, but the second time it only contributes  to the sum.
