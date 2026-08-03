# Day 9: Recursion!

---

| Field | Value |
|---|---|
| **Slug** | `day-9-recursion` |
| **Contest** | 30-days-of-code |
| **Difficulty** | Easy |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/day-9-recursion |

---

## Problem Statement

Welcome to Day 9! Check out this [video on recursion](https://www.youtube.com/watch?v=glENxqtJzAQ&feature=youtu.be), or jump right into the problem.

**Euclid's Algorithm for Computing the GCD of two integers**  

Given two integers, $x$ and $y$, their $GCD$ (greatest common divisor) can be calculated recursively using [Euclid's Algorithm](http://people.cis.ksu.edu/~schmidt/301s12/Exercises/euclid_alg.html), which essentially says that if $x$ equals $y$, then $GCD(x,y) = x$; otherwise, $GCD(x,y) = GCD(x-y, y)$ if $x \gt y$. Note that this logic can be further optimized for a more efficient implementation.

Given the starter code in your editor, complete the function body so it returns the $GCD$ of two input integers, $x$ and $y$.

## Input Format

Two space-separated integers, $x$ and $y$.
 
 **Constraints**  
$1 \le x,y \le 10^{6}$

## Output Format

Print the $GCD$ of $x$ and $y$ as an integer.
