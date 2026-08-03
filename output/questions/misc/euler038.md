# Project Euler #38: Pandigital multiples

---

| Field | Value |
|---|---|
| **Slug** | `euler038` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 100 |
| **Contest** | projecteuler |
| **URL** | https://www.hackerrank.com/challenges/euler038 |

---

## Preview

Pandigital multiples

## Problem Statement

<sub>This problem is a programming version of [Problem 38](https://projecteuler.net/problem=38) from [projecteuler.net](https://projecteuler.net/)</sub> 


Take the number $192$ and multiply it by each of $1$, $2$, and $3$:

$$192 × 1 = 192 \\\
 192 × 2 = 384 \\\
 192 × 3 = 576$$

By concatenating each product we get the $1$ to $9$ pandigital, $192384576$. We will call $192384576$ the concatenated product of $192$ and $(1,2,3)$


The same can be achieved by starting with $9$ and multiplying by $1$, $2$, $3$, $4$, and $5$, giving the pandigital, $918273645$, which is the concatenated product of $9$ and $(1,2,3,4,5)$. Let's call 9 as the Multiplier $M$    


The similar process can be shown for $1$ to $8$ pandigital also. $18$ when multiplied by $1,2,3,4$ gives $18365472$ which is $1-8$ pandigital.


You are given $N$ and $K$ where $K$ = $8$ or $9$, find the multipliers for that given $K$ below $N$ and print them in ascending order.

## Input Format

Input contains two integer $N$ and $K$.

## Output Format

Print the answer corresponding to the test case.

## Constraints

$100 \le N \le 10^5$

$8 \le K \le 9$

$1 < M$

## Sample Tests

### Test 1

```
100 8
```

### Test 2

```
18
78
```
