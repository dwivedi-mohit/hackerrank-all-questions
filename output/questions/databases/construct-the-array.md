# Construct the Array

- **Domain:** databases
- **Difficulty:** Medium
- **Max Score:** 35
- **Success Ratio:** 0.6917031751050088
- **Total Submissions:** 22141
- **Solved Count:** 15315
- **URL:** https://www.hackerrank.com/challenges/construct-the-array

## Problem Statement

Your goal is to find the number of ways to construct an array such that consecutive positions contain different values.

Specifically, we want to construct an array with $n$ elements such that each element between $1$ and $k$, inclusive. We also want the first and last elements of the array to be $1$ and $x$.  

Given $n$, $k$ and $x$, find the number of ways to construct such an array. Since the answer may be large, only find it modulo $10^9 + 7$. 

For example, for $n = 4$, $k = 3$, $x = 2$, there are $3$ ways, as shown here:

![image](https://s3.amazonaws.com/hr-assets/0/1511427084-cd3fbbf0e1-FILLARRAY.png)

Complete the function `countArray` which takes input $n$, $k$ and $x$. Return the number of ways to construct the array such that consecutive elements are distinct. 

## Input Format

  

## Output Format

  

## Constraints

- $3 \le n \le 10^5$  
- $2 \le k \le 10^5$  
- $1 \le x \le k$  

**Subtasks**

- For $20\%$ of the maximum score, $n \le 10^3$ and $k \le 10^2$  

## Sample Input

, ,

## Explanation

Refer to the diagram in the challenge statement.
