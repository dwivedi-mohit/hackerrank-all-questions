# Number of M-Coprime Arrays

- **Domain:** cpp
- **Difficulty:** Hard
- **Max Score:** 70
- **Success Ratio:** 0.2894736842105263
- **Total Submissions:** 228
- **Solved Count:** 66
- **URL:** https://www.hackerrank.com/challenges/number-of-m-coprime-arrays

## Problem Statement

An array of integers is called $m$-coprime if the following conditions are both satisfied:

- All the integers in the array are positive divisors of $m$.
- Each pair of adjacent elements in the array is [coprime](https://en.wikipedia.org/wiki/Coprime_integers) (i.e., element $i$ is always coprime with element $i + 1$).

Two arrays, $A$ and $B$, of size $n$ are *different* if and only if there exists an index $i$ such that $A[i] \ne B[i]$.

You are given $q$ queries where each query consists of integers $n$ and $m$. For each query, find the number of $m$-coprime arrays of size $n$, modulo $10^9 + 7$, and print it on a new line.      

## Input Format

The first line contains an integer, $q$, denoting the number of queries.    
Each of the $q$ subsequent lines contains two space-separated integers describing the respective values of $n$ (the size of the array) and $m$.

## Output Format

For each query, print the number of $m$-coprime arrays of size $n$ modulo $10^9 + 7$ on a new line.

## Constraints

- $1 \le q \le 100 $
- $1 \le n, m \le 10^{18}$

## Sample Input

1
2 6

## Sample Output

9

## Explanation

Given  and , we want to find the possible -coprime arrays of length . The elements of each array must be taken from the set of divisors of , which is  for the given value of . We then assemble all possible -coprime arrays of size :

-

-

-

-

-

-

-

-

-

As there are nine such arrays, we print the value of  on a new line.
