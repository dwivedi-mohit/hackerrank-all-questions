# Security Involution

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9614911921343712
- **Total Submissions:** 7323
- **Solved Count:** 7041
- **URL:** https://www.hackerrank.com/challenges/security-involution

## Problem Statement

Consider a function $f : X\rightarrow X$ where $X$ is any set, and $f$ is a bijection. 

Now, if $f = f^{-1}$ then $f$ is called an *involution*. In other words, a function $f$ is called an involution if $f(f(x)) = x$

In this task you're given a permutation $f : \{1, 2, 3, ..., n\} \rightarrow \{1, 2, 3, ..., n\}$. 

Determine whether $f$ is an involution or not.

**Constraints**

$1 \le n \le 20$

## Input Format

There are $2$ lines in the input. <br>
The first line contains a single positive integer $n$. <br>
The second line contains $n$ space separated integers, the values of $f(1),\ f(2),\ f(3),\ ...,\ f(n)\ $, respectively.

## Output Format

Output "*YES*" if $f$ is an involution. Otherwise, output "*NO*".

## Sample Input

2 1

## Sample Output

YES

## Explanation

Since,  and  and .

Hence,  is an involution.
