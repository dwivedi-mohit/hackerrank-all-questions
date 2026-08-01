# Recursion: Fibonacci Numbers

- **Domain:** python
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9840302837331069
- **Total Submissions:** 141330
- **Solved Count:** 139073
- **URL:** https://www.hackerrank.com/challenges/ctci-fibonacci-numbers

## Problem Statement

*The Fibonacci Sequence*  		

The Fibonacci sequence appears in nature all around us, in the arrangement of seeds in a sunflower and the spiral of a nautilus for example.  

The Fibonacci sequence begins with $fibonacci(0) = 0$ and $fibonacci(1) = 1$ as its first and second terms. After these first two elements, each subsequent element is equal to the sum of the previous two elements. 

Programmatically:
	
- $fibonacci(0) = 0$
- $fibonacci(1) = 1$
- $fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)$

		
Given $n$, return the $n^{th}$ number in the sequence.

**Example**   
$n = 5$   

The Fibonacci sequence to $6$ is $fs = [0,1,1,2,3,5,8]$.  With zero-based indexing, $fs[5] = 5$.

**Function Description**

Complete the recursive function $fibonacci$ in the editor below.   

fibonacci has the following parameter(s):

- *int n:* the index of the sequence to return   

**Returns**   
- *int:* the $n^{th}$ element in the Fibonacci sequence

## Input Format

The integer $n$.

## Output Format

   

## Constraints

- $0 \lt n \le 30$  

## Sample Input

STDIN   Function
-----   --------
3       n = 3

## Explanation

The Fibonacci sequence begins as follows:

...

In the sequence above,  is .
