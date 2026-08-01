# Requirement

- **Domain:** regex
- **Difficulty:** Advanced
- **Max Score:** 80
- **Success Ratio:** 0.7035766780989711
- **Total Submissions:** 2041
- **Solved Count:** 1436
- **URL:** https://www.hackerrank.com/challenges/requirement

## Problem Statement

There are $n$ variables and $m$ requirements. Requirements are represented as $(x \le y)$, meaning that the $x^{th}$ variable must be less than or equal to the $y^{th}$ variable. 

Your task is to assign non-negative numbers smaller than $10$ to each variable and then calculate the number of different assignments satisfying all requirements. Two assignments are different if and only if at least one variable is assigned to a different number in both assignments. Print your answer modulo $10^3+7$.

## Input Format

The first line contains $2$ space-separated integers, $n$ and $m$, respectively.
Each of the $m$ subsequent lines contains $2$ space-seperated integers describing the respective $x$ and $y$ values for an $(x \le y)$ requirement.

## Output Format

Print your answer modulo $10^3+7$.

## Constraints

- $0 \lt n \lt 14$
- $0 \lt m \lt 200$
- $0 \le x, y \lt n$

## Sample Input

6 7
1 3
0 1
2 4
0 4
2 5
3 4
0 2

## Sample Output

1000

## Explanation

There are  variables and  requirements.

Let the variables be in the array .

Requirements are -

One of the assignments is -

Similarly there are  assignments possible.

Result = .
