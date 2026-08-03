# Prime Digit Sums

---

| Field | Value |
|---|---|
| **Slug** | `prime-digit-sums` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/prime-digit-sums |

---

## Preview

Count the number of n-digit numbers where every substring of 3, 4, and 5 digits sums to a prime number.

## Problem Statement

Chloe is fascinated by prime numbers. She came across the number $283002$ on a sign and, though the number is not prime, found some primes hiding in it by using the following rules:


- Every three consecutive digits sum to a prime:
	$$\begin{array}{cccc} \! \underbrace{283}\!002 & 2\! \underbrace{830}\!02 & 28\! \underbrace{300}\!2 & 283\! \underbrace{002}\!\end{array}$$
- Every four consecutive digits sum to a prime:
	$$\begin{array}{ccc} \! \underbrace{2830}\!02 & 2\! \underbrace{8300}\!2 & 28\! \underbrace{3002}\!\end{array}$$
- Every five consecutive digits sum to a prime:
	$$\begin{array}{cc} \! \underbrace{28300}\!2 & 2\! \underbrace{83002}\! \end{array}$$

You must answer $q$ queries, where each query consists of an integer, $n$. For each $n$, find and print the number of positive $n$-digit numbers, modulo $10^9+7$, that satisfy *all three* of Chloe's rules (i.e., every three, four, and five consecutive digits sum to a prime).

## Input Format

The first line contains an integer, $q$, denoting the number of queries. 		
Each of the $q$ subsequent lines contains an integer denoting the value of $n$ for a query.

## Output Format

For each query, print the number of $n$-digit numbers satisfying Chloe's rules, modulo $10^9 + 7$, on a new line.

## Constraints

* $1 \le q \le 2\times 10^4$

* $1 \le n \le 4\times 10^5$

## Sample Tests

### Test 1

```
1
6
```

### Test 2

```
95
```
