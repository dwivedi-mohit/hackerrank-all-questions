# Divisor Exploration II

---

| Field | Value |
|---|---|
| **Slug** | `divisor-exploration-2` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/divisor-exploration-2 |

---

## Preview

Find the product of a sequence and then calculate the summation of its divisors.

## Problem Statement

You are given $q$ queries where each query is in the form of two integers, $m$ and $a$, such that:
$$n = \prod\limits_{i = 1}^{m} p_i^{a+i} \text{, where } p_i \text{ is the } i^{th} \text{ prime.}$$

For each query, find the following value: 

$$result = \sum\limits_{x|n} \sigma_{1}(x)$$


where $x|n$ denotes that each $x$ is a [divisor](https://en.wikipedia.org/wiki/Divisor) of $n$ and $\sigma_{1}(x)$ is the *sum of the divisors* of $x$. Then print the value of $result \bmod (10^9 + 7)$ on a new line.

## Input Format

The first line contains an integer, $q$, denoting the number of queries. 		
Each line $i$ of the $q$ subsequent lines contains two space-separated integers describing the respective values of $m_i$ and $a_i$ for query $i$.

## Output Format

For each query, print a single integer denoting the value of $result \bmod (10^9 + 7)$ on a new line.

## Constraints

+ $1 \le q \le 50$

+ $1 \le m \le 10^5$

+ $0 \le a \le 10^5$

## Sample Tests

### Test 1

```
3
2 0
3 0
2 4
```

### Test 2

```
72
13968
196320
```
