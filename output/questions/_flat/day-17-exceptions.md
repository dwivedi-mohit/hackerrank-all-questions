# Day 17: Exceptions!

---

| Field | Value |
|---|---|
| **Slug** | `day-17-exceptions` |
| **Contest** | 30-days-of-code |
| **Difficulty** | Easy |
| **Score** | 75 |
| **URL** | https://www.hackerrank.com/challenges/day-17-exceptions |

---

## Problem Statement

Welcome to Day 17! Learn how to use [try-catch blocks in Day 16](https://youtu.be/2foOQ1Uxb6s) and how to [create your own exceptions in Day 17](https://youtu.be/9TuoE16Tlac) or just jump right into the problem.

Create a class *Calculator* which consists of a single method *power(int,int)*. This method takes two integers, $n$ and $p$, as parameters and finds $n^p$. If either $n$ or $p$ is negative, then the method must throw an exception which says *"n and p should be non-negative"*. 


Code for handling Input/Output is already provided in the editor. Please read the partially completed code in the editor and complete it. 

*Note:* The class *Calculator* mustn't be public.


No need to worry about constraints, there won't be any overflow if your code is correct.

If you enjoyed this challenge, here's a [java only Exception Challenge](https://www.hackerrank.com/challenges/java-exception-handling-try-catch)

## Input Format

First line contains *T*, the number of test cases. Next *T* lines contain two integers *n* and *p* separated by a space.

## Output Format

Output T lines. For each test case if n and p are positive then print $n^p$ else  print *"n and p should be non-negative"* without quotes.
