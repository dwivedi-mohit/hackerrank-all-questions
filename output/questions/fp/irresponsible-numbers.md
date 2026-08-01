# Irresponsible Numbers

- **Domain:** fp
- **Difficulty:** Hard
- **Max Score:** 75
- **Success Ratio:** 0.7037037037037037
- **Total Submissions:** 108
- **Solved Count:** 76
- **URL:** https://www.hackerrank.com/challenges/irresponsible-numbers

## Problem Statement

A number, $x$, is called *irresponsible* when adding $x$ to $x+1$ requires a *[carry](https://en.wikipedia.org/wiki/Carry_(arithmetic))* operation. For example, $5$, $17$, and $91$ are irresponsible numbers because adding them to $6$, $18$, and $92$ (respectively) requires a carry operation:

- In $5 + (5 + 1) = 5 + 6 = 11$, a $1$ is carried over into the $10$'s place. 
- In $17 + (17 + 1) = 17 + 18 = 35$, a $2$ is carried over into the $10$'s place.
- In $91 + (91 + 1) = 91 + 92 = 183$, a $1$ is carried over into the $100$'s place.

You have two integers, $x$ and $n$. Construct a new number, $s$, by repeating $x$ a total of $n$ times. For example, if $x = 3121$ and $n = 4$, then $s = 3121312131213121$.

Given $x$ and $n$, construct $s$ and find all the irreponsible numbers between $1$ and $s$. Then print the number of irresponsible numbers in the aforementioned range; as this number can be quite large, your answer must be modulo $10^9+7$.

## Input Format

A single line with two space-separated integers denoting the respective values of $x$ and $n$.

## Output Format

Print a single integer denoting the number of irresponsible numbers between $1$ and $s$, modulo $10^9+7$.

## Constraints

* $1 \leq x \leq 10^{1,000,000}$
* $1 \leq n \leq 10^{18}$

**Subtasks**

For $15\%$ of the maximum score: 

* $1 \leq x \leq 10^6$
* $n = 1$

For $40\%$ of the maximum score: 

* $1 \leq x \leq 10^{1,000,000}$
* $n = 1$

## Sample Input

1 2

## Explanation

When we repeat  a total of  times we get . The irresponsible numbers between  and  are , , , and . Because there are four irresponsible numbers, we print  on a new line.
