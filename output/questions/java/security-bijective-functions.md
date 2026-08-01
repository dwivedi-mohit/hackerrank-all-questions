# Security Bijective Functions

- **Domain:** java
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.7963236711870942
- **Total Submissions:** 15559
- **Solved Count:** 12390
- **URL:** https://www.hackerrank.com/challenges/security-bijective-functions

## Problem Statement

Now that we know about one-to-one functions, let's talk about *onto* functions and *bijective* functions. 

A function $f: X\rightarrow Y$ is *onto* if and only if each element in the co-domain $Y$ is the image of, at least, one element in the domain $X$. That is:

$Im(f) = Y$

If the function $f$ is both *one-to-one* and *onto* then $f$ is a *bijection* from $X$ to $Y$ or, equivalently, $f: X\rightarrow Y$ is a bijective function.

In this task, you'll be given an integer $n$ and a function $f: X\rightarrow X$ where $X = \{1, 2, 3, ..., n\}$. Determine whether the given function is a bijective function or not.

**Constraints**

$1 \le n \le 20$

## Input Format

There are $2$ lines in the input. <br>
The first line contains a single positive integer $n$. <br>
The second line contains $n$ space separated integers, the values of $f(1),\ f(2),\ f(3),\ ...,\ f(n)\ $, respectively.

## Output Format

On a single line, output "*YES*" if $f$ is bijective. Otherwise, output "*NO*".

## Sample Input

1 2 3

## Sample Output

YES

## Explanation

Basically, this is the function .
