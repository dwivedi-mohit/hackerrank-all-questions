# Project Euler #26: Reciprocal cycles

---

| Field | Value |
|---|---|
| **Slug** | `euler026` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 100 |
| **Contest** | projecteuler |
| **URL** | https://www.hackerrank.com/challenges/euler026 |

---

## Preview

Recurring cycles in decimals.

## Problem Statement

<sub>This problem is a programming version of [Problem 26](https://projecteuler.net/problem=26) from [projecteuler.net](https://projecteuler.net/)</sub>


A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:


$$\begin{align*}
\frac{1}{2} &= 0.5 \\\
\frac{1}{3} &= 0.(3) \\\
\frac{1}{4} &= 0.25 \\\
\frac{1}{5} &= 0.2 \\\
\frac{1}{6} &= 0.1(6) \\\
\frac{1}{7} &= 0.(142857) \\\
\frac{1}{8} &= 0.125 \\\
\frac{1}{9} &= 0.(1) \\\
\frac{1}{10} &= 0.1 
\end{align*}$$

Where $0.1(6)$ means $0.166666...$, and has a 1-digit recurring cycle. It can be seen that $\frac{1}{7}$ has a 6-digit recurring cycle.


Find the value of smallest $d \lt N$ for which $\frac{1}{d}$ contains the longest recurring cycle in its decimal fraction part.

## Input Format

The first line contains an integer $T$ , i.e., number of test cases.

Next $T$ lines will contain an integer $N$.

## Output Format

Print the values corresponding to each test case.

## Constraints

$1 \le T \le 1000$

$4 \le N \le 10000$

## Sample Tests

### Test 1

```
2
5
10
```

### Test 2

```
3
7
```
