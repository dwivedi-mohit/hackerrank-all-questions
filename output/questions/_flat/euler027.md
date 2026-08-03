# Project Euler #27: Quadratic primes

---

| Field | Value |
|---|---|
| **Slug** | `euler027` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 100 |
| **Contest** | projecteuler |
| **URL** | https://www.hackerrank.com/challenges/euler027 |

---

## Preview

More primes. Quadratic primes.

## Problem Statement

<sub>This problem is a programming version of [Problem 27](https://projecteuler.net/problem=27) from [projecteuler.net](https://projecteuler.net/)</sub>


Euler published the remarkable quadratic formula:

$$n^2 + n + 41$$


It turns out that the formula will produce 40 primes for the consecutive values $n = 0$ to $39$. However, when $n = 40$, $40^2 + 40 + 41 = 40(40 + 1) + 41$ is divisible by $41$, and certainly when $n = 41$, $41^2 + 41 + 41$ is clearly divisible by $41$.
 
Using computers, the incredible formula $n^2 − 79n + 1601$ was discovered, which produces $80$ primes for the consecutive values $n
 = 0$ to $79$. The product of the coefficients, $−79$ and $1601$, is $−126479$.

 
Considering quadratics of the form: 

$$n^2 + an + b, \text{ where } |a| \le N \text{ and } |b| \le N$$


where $|n|$ is the modulus/absolute value of $n$

e.g. $|11| = 11$ and $|−4| = 4$


Find the coefficients, $a$ and $b$, for the quadratic expression that produces the maximum number of primes for consecutive values of $n$, starting with $n = 0$.



**Note** For this challenge you can assume solution to be unique.

## Input Format

The first line contains an integer $N$.

## Output Format

Print the value of $a$ and $b$ separated by space.



**Constraints**

$42 \le N \le 2000$

## Sample Tests

### Test 1

```
42
```

### Test 2

```
-1 41
```
