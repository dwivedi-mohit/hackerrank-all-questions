# Project Euler #21: Amicable numbers

---

| Field | Value |
|---|---|
| **Slug** | `euler021` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 100 |
| **Contest** | projecteuler |
| **URL** | https://www.hackerrank.com/challenges/euler021 |

---

## Preview

Proper and improper divisions.

## Problem Statement

<sub>This problem is a programming version of [Problem 21](https://projecteuler.net/problem=21) from [projecteuler.net](https://projecteuler.net/)</sub>


Let $d(n)$ be defined as the sum of proper divisors of $n$ (numbers less than $n$ which divide evenly into $n$).

If $d(a) = b$ and $d(b) = a$, where $a \ne b$, then $a$ and $b$ are an amicable pair and each of $a$ and $b$ are called amicable numbers.


For example, the proper divisors of $220$ are $1, 2, 4, 5, 10, 11, 20, 22, 44, 55 \text{ and } 110$ therefore $d(220) = 284$. The proper divisors of $284$ are $1, 2, 4, 71 \text{ and } 142$ so $d(284) = 220$.

Evaluate the sum of all the amicable numbers under $N$.

## Input Format

The first line contains an integer $T$, i.e., number of test cases.

Next $T$ lines will contain an integer $N$.

## Output Format

Print the values corresponding to each test case.

## Constraints

+ $1 \leqslant T \leqslant 1000$

+ $1 \leqslant N \leqslant 10^5$

## Sample Tests

### Test 1

```
1
300
```

### Test 2

```
504
```
