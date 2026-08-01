# Fibonacci Finding (easy)

- **Domain:** python
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.37005287614164395
- **Total Submissions:** 12482
- **Solved Count:** 4619
- **URL:** https://www.hackerrank.com/challenges/fibonacci-finding-easy

## Problem Statement

You're given three numbers: $A$, $B$, and $N$, and all you have to do is to find the number $F_N$ where  
$$F_0=A \\\
F_1=B \\\
F_i=F_{i-1}+F_{i-2} ~for ~i \geq 2$$  

As the number can be very large, output it modulo $10^9+7$.  

Consider the following link: http://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form


## Input Format

First line contains a single integer $T$ - the number of tests.
$T$ lines follow, each containing three integers: $A$, $B$ and $N$.


## Output Format

For each test case output a single integer $-$ $F_N$.  

## Constraints

$1 \le T \le 1000$  
$1 \le A,B,N \le 10^9$  


## Sample Input

2 3 1
9 1 7
9 8 3
2 4 9
1 7 2
1 8 1
4 3 1
3 7 5

## Sample Output

85
25
178
8
8
3
44

## Explanation

First test case is obvious.

Let's look through the second one:
