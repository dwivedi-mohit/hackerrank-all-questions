# Down to Zero II

- **Domain:** shell
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.6172154795065659
- **Total Submissions:** 40208
- **Solved Count:** 24817
- **URL:** https://www.hackerrank.com/challenges/down-to-zero-ii

## Problem Statement

You are given $Q$ queries. Each query consists of a single number $N$. You can perform any of the $2$ operations on $N$ in each move:

1: If we take 2 integers $a$ and $b$ where $N = a\times b$$(a \ne 1$, $b \ne 1)$, then we can change $N=max(a,b)$

2: Decrease the value of $N$ by $1$. 

Determine the minimum number of moves required to reduce the value of $N$ to $0$.

## Input Format

The first line contains the integer $Q$. <br>
The next $Q$ lines each contain an integer, $N$.  



## Output Format

Output $Q$ lines. Each line containing the minimum number of moves required to reduce the value of $N$ to $0$.

## Constraints

$1 \le Q \le 10^3$  
$0 \le N \le 10^6$  

## Sample Input

3
4

## Sample Output

3

## Explanation

For test case 1, We only have one option that gives the minimum number of moves.

Follow  ->  ->  -> . Hence,  moves.

For the case 2, we can either go  ->  ->  ->  ->  or  ->  ->  -> . The 2nd option is more optimal. Hence,  moves.
