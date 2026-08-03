# Project Euler #46: Goldbach's other conjecture

---

| Field | Value |
|---|---|
| **Slug** | `euler046` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 100 |
| **Contest** | projecteuler |
| **URL** | https://www.hackerrank.com/challenges/euler046 |

---

## Preview

Disproving a Conjecture

## Problem Statement

<sub>This problem is a programming version of [Problem 46](https://projecteuler.net/problem=46) from [projecteuler.net](https://projecteuler.net/)</sub>


It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
$$\begin{align*}
 9 &= 7 + 2\times1^2 \\\
 15 &= 7 + 2 \times 2^2 \\\
 21 &= 3 + 2 \times 3^2 \\\
 25 &= 7 + 2 \times 3^2 \\\
 27 &= 19 + 2 \times 2^2 \\\
 33 &= 31 + 2 \times 1^2
\end{align*}$$
 
It turns out that the conjecture was false as you'll discover some values can't be represented as a sum of prime and twice a square.

You are given $N$, print the number of ways N can be represented as a sum of prime and twice a square.

Example $15$ can be represented in two ways as $15 = 7 + 2 \times 2^2$ and $15 = 13 + 2 \times 1^2$

## Input Format

The first line contains an integer $T$ , i.e., number of test cases.

Next $T$ lines will contain an integer $N$.

## Output Format

Print the values corresponding to each test case.

## Constraints

$1 \le T \le 100$

$9 \le N < 5 \times 10^5$

$N \in \{\text {odd composite number}\}$

## Sample Tests

### Test 1

```
2
9
15
```

### Test 2

```
1
2
```
