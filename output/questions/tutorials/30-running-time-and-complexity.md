# Day 25: Running Time and Complexity

---

| Field | Value |
|---|---|
| **Slug** | `30-running-time-and-complexity` |
| **Domain** | tutorials |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/30-running-time-and-complexity |

---

## Preview

Determine if a number is prime in optimal time!

## Problem Statement

**Objective**	
Today we will learn about running time, also known as time complexity. Check out the [Tutorial](/challenges/30-running-time-and-complexity/tutorial) tab for learning materials and an instructional video.	

**Task** 	
A *prime* is a natural number greater than $1$ that has no positive divisors other than $1$ and itself. Given a number, $n$, determine and print whether it is $\texttt{Prime}$ or $\texttt{Not prime}$. 

**Note:** If possible, try to come up with a $O(\sqrt{n})$ primality algorithm, or see what sort of optimizations you come up with for an $O(n)$ algorithm. Be sure to check out the *Editorial* after submitting your code.

## Input Format

The first line contains an integer, $T$, the number of test cases. 	
Each of the $T$ subsequent lines contains an integer, $n$, to be tested for primality.

## Output Format

For each test case, print whether $n$ is $\texttt{Prime}$ or $\texttt{Not prime}$ on a new line.

## Constraints

* $1 \le T \le 30$
* $1 \le n \le 2 \times 10^{9}$

## Sample Tests

### Test 1

```
3
12
5
7
```

### Test 2

```
Not prime
Prime
Prime
```
