# Find the Seed

- **Domain:** databases
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.7307490832896805
- **Total Submissions:** 1909
- **Solved Count:** 1395
- **URL:** https://www.hackerrank.com/challenges/find-the-seed

## Problem Statement

A company needs random numbers for its operation. $N$ random numbers have been generated using $N$ numbers as seeds and the following recurrence formula:

$$F(K) = ( C(1) \times F(K-1) + C(2) \times F(K-2) + \cdots + \\C(N-1) \times F(K-N+1) +  C(N) \times F(K-N) )\  \% \ (10^9 + 7)$$

The numbers used as seeds are $F(N-1), F(N-2), \ldots, F(1), F(0)$. $F(K)$ is the $K^{th}$ term of the recurrence.

Due to a failure on the servers, the company lost its seed numbers. Now they just have the recurrence formula and the previously generated $N$ random numbers.

The company wants to recover the numbers used as seeds, so they have hired you for doing this task.

## Input Format

The first line contains two space-separated integers, $N$ and $K$, respectively.	
The second line contains the space-separated integers describing $F(K), F(K-1), \ldots, F(K-N+2), F(K-N+1)$ (all these numbers are non-negative integers $\lt 10^9$).		
The third line contains the space-separated coefficients of the recurrence formula, $C(1), C(2), \ldots, C(N-1), C(N)$. All of these coefficients are positive integers $\lt 10^9$.

## Output Format

The output must be one line containing the space-separated seeds of the random numbers - $F(N-1), F(N-2), \ldots, F(1), F(0)$.

## Constraints

- $1 \le N \le 50$
- $1 \le K \le 10^9$
- $0 \le K - N + 1$

## Sample Input

2 6
13 8
1 1

## Sample Output

1 1

## Explanation

This is the classic Fibonacci recurrence. We have the  and  terms, and, of course, the seeds are the numbers  and .
