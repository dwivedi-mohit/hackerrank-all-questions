# The Chosen One

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.756596060943887
- **Total Submissions:** 2691
- **Solved Count:** 2036
- **URL:** https://www.hackerrank.com/challenges/the-chosen-one

## Problem Statement

You are given a sequence of $n$ integers, $a_0, a_1, \ldots, a_{n-1}$. Find and print any integer $x$ such that $x$ is divisor of every $a_i$ except for exactly one element.

## Input Format

The first line contains an integer, $n$, denoting the length of the sequence.		
The second line contains $n$ positive space-separated integers describing $a_0, a_1, \ldots, a_{n-1}$.

## Output Format

Print any positive integer denoting $x$ such that $x$ is a divisor of exactly $n-1$ of the sequence's elements. $x$ must be between $1$ and $2 \cdot 10^{18}$

## Constraints

- $1 \le n \le 10^5$
- $1 \le a_i \le 10^{18}$
- It is guaranteed that a solution exists.

## Sample Input

4
3 6 18 12

## Sample Output

6

## Explanation

We are given the array . There are two possible answers:

-  is a divisor of , , and  but not a divisor of .

-  is a divisor of , , and  but not a divisor of .

Thus, we can print either  or  as our answer.
