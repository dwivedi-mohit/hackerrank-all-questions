# Leonardo's Prime Factors

---

| Field | Value |
|---|---|
| **Slug** | `leonardo-and-prime` |
| **Domain** | mathematics |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/leonardo-and-prime |

---

## Preview

Find the maximum number of prime factors for any number in the inclusive range from 1 to n.

## Problem Statement

Leonardo loves primes and created $q$ queries where each query takes the form of an integer, $n$. For each $n$, count the maximum number of distinct prime factors of any number in the inclusive range $[1, n]$.

**Note:** Recall that a prime number is only divisible by $1$ and itself, and $1$ is *not* a prime number.


**Example**

$n = 100$


The maximum number of distinct prime factors for values less than or equal to $100$ is $3$.  One value with $3$ distinct prime factors is $30$. Another is $42$.  


**Function Description**


Complete the *primeCount* function in the editor below.


*primeCount* has the following parameters:


- *int n:* the inclusive limit of the range to check


**Returns**


- *int:* the maximum number of distinct prime factors of any number in the inclusive range $[0 - n]$.

## Input Format

The first line contains an integer, $q$, the number of queries. 	
Each of the next $q$ lines contains a single integer, $n$.

## Constraints

+ $1 \le q \le 10^{5}$

+ $1 \le n \le 10^{18}$

## Sample Tests

### Test 1

```
6
1
2
3
500
5000
10000000000
```

### Test 2

```
0
1
1
4
5
10
```
