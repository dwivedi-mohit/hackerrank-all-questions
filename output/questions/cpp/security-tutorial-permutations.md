# Security Permutations

- **Domain:** cpp
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9656694458067681
- **Total Submissions:** 8156
- **Solved Count:** 7876
- **URL:** https://www.hackerrank.com/challenges/security-tutorial-permutations

## Problem Statement

Consider a function $f : X\rightarrow X$ where $X$ is any set. <br>
If $f$ is a bijection, then $f$ is a permutation function of $X$. There is nothing special about the set $X$. It can be replaced by the set $\{1, 2, 3, ..., n\}$ where $n = |X|$.

Consider a permutation $f$ given by $(2, 3, 1)$. This means that $f(1) = 2$, $f(2) = 3$ and $f(3) = 1$.

In this task, you're given a permutation $f : \{1, 2, 3, ..., n\} \rightarrow \{1, 2, 3, ..., n\}$. 

Output $f(f(x))$ for all $x \in \{1, 2, 3, ..., n\}$.

**Constraints**

$1 \le n \le 20$

## Input Format

There are $2$ lines in the input.<br>
The first line contains a single positive integer $n$.<br>
The second line contains $n$ space separated integers, the values of $f(1),\ f(2),\ f(3),\ ...,\ f(n)\ $, respectively.

## Output Format

On separate lines, output the values of $f(f(1)),\ f(f(2)),\ f(f(3)),\ ...,\ f(f(n))\ $, respectively. 

## Sample Input

2 3 1

## Sample Output

1
2

## Explanation

and so on.
