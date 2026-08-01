# Divisible Numbers

- **Domain:** cpp
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.36555806087936865
- **Total Submissions:** 3548
- **Solved Count:** 1297
- **URL:** https://www.hackerrank.com/challenges/divisible-numbers

## Problem Statement

Given an integer, $n$, find the smallest integer $m$ such that $m$ is divisible by $n$ (i.e., $n$ is a factor of $m$) and satisfies the following properties:

+ $m$ must not contain zeroes in its decimal representation. 
+ The sum of $m$'s digits must be *greater than or equal to* the product of $m$'s digits. 

Given $n$, find $m$ and print *the number of digits* in $m$'s decimal representation. 

## Input Format

A single integer denoting $n$.

## Output Format

Print the *number of digits* in the decimal representation of the smallest possible $m$.

## Constraints

- $1 \le n \le 3 \times 10^4$
- $n$ is not divisible by $10$.

**Time Limits**

- The time limits for this challenge are available [here](http://hr-testcases.s3.amazonaws.com/1361/limits.json).

## Sample Input

1

## Sample Output

1

## Explanation

is evenly divided by , doesn't contain any zeroes in its decimal representation, and the sum of its digits is not less than the product of its digits. Thus, we print the number of digits in  (which also happens to be ) as our answer.
