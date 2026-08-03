# Customized Chess Board

---

| Field | Value |
|---|---|
| **Slug** | `customized-chess-board` |
| **Contest** | hourrank-29 |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/customized-chess-board |

---

## Problem Statement

Since all chess boards available in the market are $8 \times 8$ boards, Alex decides to paint a customised $N \times N$ board. Given the painted chess board, can you tell if it is painted correctly or not ? A chess board is considered valid if every $2$ adjacent cells are painted with different color. Two cells are considered adjacent if they share a boundary e.g.

![image](https://s3.amazonaws.com/hr-assets/0/1532892831-f7e500d878-UntitledDiagram.png)

Chess board in figure I is painted correctly though chess board in figure II is not.

## Input Format

First line of input contains a single integer $T$ denoting the number of test cases.  
First line of each test contains a single integer $N$ denoting the size of the board.   
Next $N$ lines of each test case contains $N$ space separated integers. 
If the $j^{th}$ integer in $i^{th}$ line is $0$, it means that cell is painted in black color otherwise it is painted in white color and is represented with $1$.

## Output Format

For each test case, Print `Yes` if the chess board is painted correctly, Print `No` otherwise in a new line.

## Constraints

- $1 \le T \le 5$  
-  $1 \le N \le 100$  
-  $C_{i, j} \in {0, 1}$
