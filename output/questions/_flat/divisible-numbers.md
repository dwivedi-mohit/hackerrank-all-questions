# Divisible Numbers

---

| Field | Value |
|---|---|
| **Slug** | `divisible-numbers` |
| **Domain** | algorithms |
| **Difficulty** | Expert |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/divisible-numbers |

---

## Preview

Given an integer, find its smallest factor that does not contain zeroes and whose digits sum to a number &ge; the product of its digits.

## Problem Statement

Given an integer, $n$, find the smallest integer $m$ such that $m$ is divisible by $n$ (i.e., $n$ is a factor of $m$) and satisfies the following properties:

+ $m$ must not contain zeroes in its decimal representation. 
+ The sum of $m$'s digits must be *greater than or equal to* the product of $m$'s digits. 

Given $n$, find $m$ and print *the number of digits* in $m$'s decimal representation.

## Input Format

A single integer denoting $n$.

## Output Format

Print the *number of digits* in the decimal representation of the smallest possible $m$.

## Constraints

- $1 \le n \le 3 \times 10^4$
- $n$ is not divisible by $10$.

**Time Limits**

- The time limits for this challenge are available [here](http://hr-testcases.s3.amazonaws.com/1361/limits.json).

## Sample Tests

### Test 1

```
1
```

### Test 2

```
1
```

### Test 3

```
9
```

### Test 4

```
1
```
