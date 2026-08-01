# Best Divisor

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.8512960436562074
- **Total Submissions:** 24922
- **Solved Count:** 21216
- **URL:** https://www.hackerrank.com/challenges/best-divisor

## Problem Statement

Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is *better* than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is *better*. For example, Kristen thinks that $13$ is better than $31$ and that $12$ is better than $11$.

Given an integer, $n$, can you find the divisor of $n$ that Kristin will consider to be the best?

## Input Format

A single integer denoting $n$.

## Output Format

Print an integer denoting the best divisor of $n$.  

## Constraints

* $0 \lt n \le 10^5$

## Sample Input

12

## Sample Output

6

## Explanation

The set of divisors of  can be expressed as . The divisor whose digits sum to the largest number is  (which, having only one digit, sums to itself). Thus, we print  as our answer.
