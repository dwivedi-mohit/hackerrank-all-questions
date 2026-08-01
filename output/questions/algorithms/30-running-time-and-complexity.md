# Day 25: Running Time and Complexity

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.9226830010652869
- **Total Submissions:** 131420
- **Solved Count:** 121259
- **URL:** https://www.hackerrank.com/challenges/30-running-time-and-complexity

## Problem Statement

**Objective**	
Today we will learn about running time, also known as time complexity. Check out the [Tutorial](/challenges/30-running-time-and-complexity/tutorial) tab for learning materials and an instructional video.	

**Task** 	
A *prime* is a natural number greater than $1$ that has no positive divisors other than $1$ and itself. Given a number, $n$, determine and print whether it is $\texttt{Prime}$ or $\texttt{Not prime}$. 

**Note:** If possible, try to come up with a $O(\sqrt{n})$ primality algorithm, or see what sort of optimizations you come up with for an $O(n)$ algorithm. Be sure to check out the *Editorial* after submitting your code.


## Input Format

The first line contains an integer, $T$, the number of test cases. 	
Each of the $T$ subsequent lines contains an integer, $n$, to be tested for primality.

## Output Format

For each test case, print whether $n$ is $\texttt{Prime}$ or $\texttt{Not prime}$ on a new line.

## Constraints

* $1 \le T \le 30$
* $1 \le n \le 2 \times 10^{9}$

## Sample Input

12
5
7

## Sample Output

Not prime
Prime
Prime

## Explanation

Test Case 0: .

 is divisible by numbers other than  and itself (i.e.: , , , ), so we print  on a new line.

Test Case 1: .

 is only divisible  and itself, so we print  on a new line.

Test Case 2: .

 is only divisible  and itself, so we print  on a new line.
