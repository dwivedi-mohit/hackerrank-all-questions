# Maximizing XOR

---

| Field | Value |
|---|---|
| **Slug** | `maximizing-xor` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/maximizing-xor |

---

## Preview

Given two integers, L and R, find the maximal value of A xor B,
 where A and B satisfy a condition.

## Problem Statement

Given two integers, $l$ and $r$, find the maximal value of $a$ [xor](http://en.wikipedia.org/wiki/Bitwise_operation#XOR) $b$, written $a \oplus b$, where $a$ and $b$ satisfy the following condition:

$l \le a \le b \le r$


For example, if $l = 11$ and $r = 12$, then

$11 \oplus 11 = 0$

$11 \oplus 12 = 7$

$12 \oplus 12 = 0$


Our maximum value is $7$.


**Function Description**

Complete the *maximizingXor* function in the editor below.  It must return an integer representing the maximum value calculated.


maximizingXor has the following parameter(s):

- *l*: an integer, the lower bound, inclusive

- *r*: an integer, the upper bound, inclusive

## Input Format

The first line contains the integer $l$.

The second line contains the integer $r$.

## Output Format

Return the maximal value of the xor operations for all permutations of the integers from $l$ to $r$, inclusive.

## Constraints

$1 \le l \le r \le 10$<sup>3</sup>

## Sample Tests

### Test 1

```
10
15
```

### Test 2

```
7
```

### Test 3

```
11
100
```

### Test 4

```
127
```
