# Megaprime Numbers

---

| Field | Value |
|---|---|
| **Slug** | `megaprime-numbers` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/megaprime-numbers |

---

## Preview

Count the number of primes in a given range that consist only of prime digits.

## Problem Statement

A [prime](https://en.wikipedia.org/wiki/Prime_number) number is an integer greater than $1$ that has no positive divisors other than $1$ and itself.

We call a number *megaprime* if it is prime and all of its individual digits are prime. For example, $53$ is megaprime because it is prime and all its digits ($5$ and $3$) are prime; however, $35$ is not megaprime because it is not prime (it's divisible by $5$ and $7$), and $13$ is not megaprime because it has a non-prime digit ($1$ is not prime).

Given two long integers, $first$ and $last$, find and print the total number of megaprime numbers in the inclusive range between $first$ and $last$.

## Input Format

Two space-separated long integers describing the respective values of $first$ and $last$.

## Output Format

Print a long integer denoting the total number of megaprimes in the inclusive interval between $first$ and $last$.

## Constraints

* $1 \le first \le last \le 10^{15}$
* $last - first \le 10^{9}$

## Sample Tests

### Test 1

```
1 100
```

### Test 2

```
8
```
