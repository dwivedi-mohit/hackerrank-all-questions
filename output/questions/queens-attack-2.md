# Queen's Attack II

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.7209621993127148
- **Total Submissions:** 112035
- **Solved Count:** 80773
- **URL:** https://www.hackerrank.com/challenges/queens-attack-2

## Problem Statement

You will be given a square chess board with one queen and a number of obstacles placed on it.  Determine how many squares the queen can attack.  

A [queen](https://en.wikipedia.org/wiki/Queen_%28chess%29) is standing on an $n \times n$ [chessboard](https://en.wikipedia.org/wiki/Chess). The chess board's rows are numbered from $1$ to $n$, going from bottom to top.  Its columns are numbered from $1$ to $n$, going from left to right. Each square is referenced by a tuple, $(r, c)$, describing the row, $r$, and column, $c$, where the square is located.

The queen is standing at position $(r_q, c_q)$.  In a single move, she can attack any square in any of the eight directions (left, right, up, down, and the four diagonals). In the diagram below, the green circles denote all the cells the queen can attack from $(4, 4)$: 

![image](https://s3.amazonaws.com/hr-challenge-images/0/1485426500-a4039ebb00-chess1.png)

There are obstacles on the chessboard, each preventing the queen from attacking any square beyond it on that path. For example, an obstacle at location $(3, 5)$ in the diagram above prevents the queen from attacking cells $(3, 5)$, $(2, 6)$, and $(1, 7)$:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1485459132-3fdc1f1ca3-chess_4_.png)

Given the queen's position and the locations of all the obstacles, find and print the number of squares the queen can attack from her position at $(r_q, c_q)$.  In the board above, there are $24$ such squares.

**Function Description**  

Complete the *queensAttack* function in the editor below.   

queensAttack has the following parameters:  
- *int n:* the number of rows and columns in the board  
- *nt k:* the number of obstacles on the board  
- *int r_q:* the row number of the queen's position  
- *int c_q:* the column number of the queen's position  
- *int obstacles[k][2]:* each element is an array of $2$ integers, the row and column of an obstacle  

**Returns**    
- *int:* the number of squares the queen can attack   

## Input Format

The first line contains two space-separated integers $n$ and $k$, the length of the board's sides and the number of obstacles.		
The next line contains two space-separated integers $r_q$ and $c_q$, the queen's row and column position.  		
Each of the next $k$ lines contains two space-separated integers $r[i]$ and $c[i]$, the row and column position of $obstacle[i]$.		

## Constraints

- $0 \lt n \leq 10^5$
- $0 \leq k \leq 10^5$
- A single cell may contain more than one obstacle.
- There will never be an obstacle at the position where the queen is located.

**Subtasks**

For $30\%$ of the maximum score: 

- $0 \lt n \leq 100$
- $0 \leq k \leq 100$

For $55\%$ of the maximum score: 

- $0 \lt n \leq 1000$
- $0 \leq k \leq 10^5$

## Sample Input

4 0
4 4

## Sample Output

9

## Explanation

The queen is standing at position  on a  chessboard with no obstacles:

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
