# AND xor OR

---

| Field | Value |
|---|---|
| **Slug** | `and-xor-or` |
| **Domain** | data-structures |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/and-xor-or |

---

## Preview

Given an array, find the maximum value of the given expression for any range of size greater than 2.

## Problem Statement

Given an array $A[]$ of $N$ distinct elements. Let $M_1$ and $M_2$ be the smallest and the next smallest element in the interval $[ L , R ]$ where $1 \le L < R \le N$.


$S_i = (((M_1 \wedge M_2) \oplus (M_1 \vee M_2)) \wedge (M_1 \oplus M_2))$.


where $\wedge, \vee, \oplus$, are the bitwise operators $AND$, $OR$ and $XOR$ respectively.

Your task is to find the maximum possible value of $S_i$.

## Input Format

First line contains integer $N$.

Second line contains $N$ integers, representing elements of the array $A[]$.


**Constraints**

$1 < N \le 10^6$

$1 \le A_i \le 10^9$

## Output Format

Print the value of maximum possible value of $S_i$.

## Sample Tests

### Test 1

```
5
9 6 3 5 2
```

### Test 2

```
15
```
