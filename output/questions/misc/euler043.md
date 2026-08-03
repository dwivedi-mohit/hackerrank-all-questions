# Project Euler #43: Sub-string divisibility

---

| Field | Value |
|---|---|
| **Slug** | `euler043` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 100 |
| **Contest** | projecteuler |
| **URL** | https://www.hackerrank.com/challenges/euler043 |

---

## Preview

Sub-string divisibility

## Problem Statement

<sub>This problem is a programming version of [Problem 43](https://projecteuler.net/problem=43) from [projecteuler.net](https://projecteuler.net/)</sub>


The number, $1406357289$, is a $0$ to $9$ pandigital number because it is made up of each of the digits $0$ to $9$ in some order, but it also has a rather interesting sub-string divisibility property.


Let $d_1$ be the $1^{st}$ digit, $d_2$ be the $2^{nd}$ digit, and so on. In this way, we note the following:

$$\begin{align*} 
& d_2d_3d_4 \text{ is divisible by 2}	\\\
& d_3d_4d_5 \text{ is divisible by 3}	\\\
& d_4d_5d_6 \text{ is divisible by 5}	\\\
& d_5d_6d_7 \text{ is divisible by 7}	\\\
& d_6d_7d_8 \text{ is divisible by 11} \\\
& d_7d_8d_9 \text{ is divisible by 13} \\\
& d_8d_9d_{10} \text{ is divisible by 17}
\end{align*}$$

Find the sum of all $0$ to $N$ pandigital numbers with this property.

## Input Format

Input contains an integer $N$

## Output Format

Print the answer corresponding to the test case.

## Constraints

$3 \le N \le 9$

## Sample Tests

### Test 1

```
3
```

### Test 2

```
22212
```
