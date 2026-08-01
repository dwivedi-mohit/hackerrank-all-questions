# Fibonacci Modified

- **Domain:** data-structures
- **Difficulty:** Medium
- **Max Score:** 45
- **Success Ratio:** 0.7955719624798476
- **Total Submissions:** 109168
- **Solved Count:** 86851
- **URL:** https://www.hackerrank.com/challenges/fibonacci-modified

## Problem Statement

Implement a *modified* [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using the following definition:

> Given terms $t[i]$ and $t[i+1]$ where $i \in (1, \infty)$, term $t[i+2]$ is computed as:
$$t_{i+2} = t_i + (t_{i+1})^2$$      

Given three integers, $t1$, $t2$, and $n$, compute and print the $n^{th}$ term of a *modified Fibonacci sequence*.

**Example**   
$t1 = 0$   
$t2 = 1$  
$n = 6$

- $t3 = 0 + 1^2 = 1$  
- $t4 = 1 + 1^2 = 2$  
- $t5 = 1 + 2^2 = 5$  
- $t6 = 2 + 5^2 = 27$  

Return $27$.  

**Function Description**  

Complete the *fibonacciModified* function in the editor below.  It must return the $n^{th}$ number in the sequence.  

fibonacciModified has the following parameter(s):  

- *int t1*: an integer  
- *int t2*: an integer  
- *int n*: the iteration to report  

**Returns**  

- *int:* the $n^{th}$ number in the sequence  

**Note:** The value of $t[n]$ may far exceed the range of a $64$-bit integer. Many submission languages have libraries that can handle such large results but, for those that don't (e.g., C++), you will need to compensate for the size of the result.  

## Input Format

A single line of three space-separated integers, the values of $t1$, $t2$, and $n$.

## Constraints

- $0 \le t1, t2 \le 2$
- $3 \le n \le 20$  
- $t_n$ may far exceed the range of a $64$-bit integer. 

## Sample Input

0 1 5

## Explanation

The first two terms of the sequence are  and , which gives us a modified Fibonacci sequence of .  The  term is .
