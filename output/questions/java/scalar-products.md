# Scalar Products

- **Domain:** java
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.7866004962779156
- **Total Submissions:** 403
- **Solved Count:** 317
- **URL:** https://www.hackerrank.com/challenges/scalar-products

## Problem Statement

Integer sequence $a$ having length $2n+2$ is defined as follows:

* $a_0 = 0$
* $a_1 = C$
* $a_{i + 2} = (a_{i + 1} + a_i) \ \% \ M$, where $0 \leq i \lt 2n $

Write a function generator, $gen$, to generate the remaining values for $a_2$ through $a_{2n+1}$. The values returned by $gen$ describe two-dimensional vectors $v_1 \dots v_n$, where each sequential pair of values describes the respective $x$ and $y$ coordinates for some vector $v$ in the form $x_1, y_1, x_2, y_2, \ldots, x_n, y_n$. In other words, $v_1 = (a_2, a_3), v_2 = (a_4, a_5), \dots , v_n = (a_{2n}, a_{2n+1})$.

Let $S$ be the set of scalar products of $v_i$ and $v_j$ for each $1 \le i, j \le n$, where $i \neq j$.
Determine the number of different [residues](http://mathworld.wolfram.com/Residue.html) in $S$ and print the resulting value modulo $M$.

## Input Format

A single line of three space-separated positive integers: $C$ (the value of $a_1$), $M$ (the modulus), and $n$ (the number of two-dimensional vectors), respectively.

**Constraints**

- $1 \le C \le 10^9$
- $1 \le M \le 10^9$ 
- $1 \le n \le 3 \times 10^5$

## Output Format

Print a single integer denoting the number of different residues $\% \ M$ in $S$.

## Constraints

-

-

-

## Sample Input

4 5 3

## Explanation

Sequence

.

This gives us our vectors: , , and .

Scalar product .

Scalar product .

Scalar product .

There are  residues  in  (i.e.:  and ), so we print the result of  (which is ).
