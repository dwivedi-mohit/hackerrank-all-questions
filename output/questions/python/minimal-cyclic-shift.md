# Minimal Cyclic Shift

- **Domain:** python
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.7959183673469388
- **Total Submissions:** 98
- **Solved Count:** 78
- **URL:** https://www.hackerrank.com/challenges/minimal-cyclic-shift

## Problem Statement

We consider two sequences of integers, $a_0, a_1, \ldots, a_{n-1}$ and $b_0, b_1, \ldots, b_{n-1}$, to be _similar_ if there exists a polynomial, $P(x)$, with integer coefficients of a degree $\le k$ such that $P(i) = (a_i - b_i ) \bmod m$ (where $m = 998244353$) for $0 \le i \lt n$. 

Given sequences $a$ and $b$, find and print the minimal integer $x$ (where $0 \le x \lt n$) such that a [cyclic shift](https://en.wikipedia.org/wiki/Circular_shift) of $b$ on $x$ elements (sequence $b_{x\ \text{mod}\ n}, b_{(x+1)\ \text{mod}\ n}, \dots b_{(x+n-1)\ \text{mod}\ n}$) is _similar_ to $a$; if no such $x$ exists, print $-1$ instead.


## Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the length of the sequences) and $k$ (the maximum degree of polynomial).		
The second line contains $n$ space-separated integers describing the respective values of $a_0, a_1, \ldots, a_{n-1}$.			
The third line contains $n$ space-separated integers describing the respective values of $b_0, b_1, \ldots, b_{n-1}$.	


## Output Format

Print an integer, $x$, denoting the minimal appropriate cyclic shift. If no such value exists, print $-1$ instead.

## Constraints

- $1 \le n \le 10^5$
- $0 \le k \le 10^9$
- $0 \le a_i, b_i < m$

## Sample Input

6 0
1 2 1 2 1 2
4 3 4 3 4 3

## Sample Output

1

## Explanation

After a cyclic shift of , sequence  is  and . Thus, we print .
