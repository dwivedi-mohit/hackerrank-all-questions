# Changing Numbers

---

| Field | Value |
|---|---|
| **Slug** | `changing-numbers` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 55 |
| **Contest** | 101hack54 |
| **URL** | https://www.hackerrank.com/challenges/changing-numbers |

---

## Preview

Find the number of numbers you can get after some number of operations.

## Problem Statement

<!-- image: enumerate all 23 numbers reachable in the sample -->

*Combinatorics and number theory are very useful in computer science. Solve this problem to improve your skills in these fields.*

You are given integers $n$ and $k$.

Let's define $q_i$. Initially, you have an integer $i$. You can modify it in two ways:

1. Multiply the current number by some number $p$, where $p$ is a prime number and $p \leq n$.
2. If the current number is divisible by $p$, divide it by $p$, where $p$ is a prime number and $p \leq n$.

Then, we define $q_i$ as the number of distinct numbers you can get if you perform these modifications no more than $k$ times in total starting with $i$. 

You need to find $\sum\limits_{i=1}^{n} i \cdot q_i$ modulo $10 ^ 9 + 7$. You are asked to find this sum to avoid printing a lot of numbers.

Complete the function `distinctNumbers` which takes in two integers $n$ and $k$ and returns a single integer denoting the sum above.

## Input Format

The single line contains two space-separated integers $n$ and $k$.

## Output Format

Print a single number denoting the answer.

## Constraints

- $1 \leq n, k \leq 10 ^ 6$

Additionally, for $40\%$ of the total points:

- $n, k \leq 3000$.

## Sample Tests

### Test 1

```
3 1
```

### Test 2

```
23
```

### Test 3

```
4 2
```

### Test 4

```
82
```
