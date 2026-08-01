# Coprime Conundrum

- **Domain:** mathematics
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.5257936507936508
- **Total Submissions:** 504
- **Solved Count:** 265
- **URL:** https://www.hackerrank.com/challenges/arthur-and-coprimes

## Problem Statement

Arthur defines a function, $f(k)$, to be the number of $(p, q)$ pairs such that:

* $1 \lt p \le q \le k$
* $p$ and $q$ are [coprime](https://en.wikipedia.org/wiki/Coprime_integers).
* $p \cdot q = k$


Given an integer, $n$, help Arthur find and print the result of: 
$$\sum_{k = 1}^{n} f(k)$$

## Input Format

The first line contains a single integer denoting $n$.

## Output Format

Print the result of $\sum_{k = 1}^{n} f(k)$ on a new line.

## Constraints

* $ 1 \le n \le 10^9$

**Subtasks**

* $ 1 \le n \le 150$ for $\text{30%}$ of the maximum score.
* $ 1 \le n \le 10^6$ for $\text{60%}$ of the maximum score.

## Explanation

The value of  for  is:

- For , there is only  valid pair, , so .

- For , there is only  valid pair, , so

- For , there is only  valid pair, , so

- For all other , the function returns .

Thus, our final sum is the result of .
