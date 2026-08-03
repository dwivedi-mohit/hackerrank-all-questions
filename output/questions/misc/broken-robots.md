# Broken Robots

---

| Field | Value |
|---|---|
| **Slug** | `broken-robots` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 65 |
| **Contest** | 101hack54 |
| **URL** | https://www.hackerrank.com/challenges/broken-robots |

---

## Preview

Find the expected value of a number of burning candles.

## Problem Statement

<!-- image: illustrate the sample with candles and stuff -->

Kate has $n$ candles numbered from $1$ to $n$. Initially, they are not burning.

She has $m$ robots. The $i^\text{th}$ robot lights candles $a_i, a_i + d_i, a_i + 2 \cdot d_i, \dots, a_i + t \cdot d_i$, where $t$ is the biggest integer such that $a_i + t \cdot d_i \leq n$. Kate wants to command all the robots to do their work. A candle burns if it is lighted by at least one robot.

Unfortunately, exactly $k$ robots are broken, but Kate doesn't remember which ones!

You are asked to find the expected value of a number of burning candles after Kate commands all the robots to do their work, assuming exactly $k$ robots are independently chosen to be broken, and that all robots are equally likely to be broken.

This expected value can be represented in the form $p/q$, where $p$ and $q$ are comprime non-negative integers. You should print $p \cdot q ^ {-1}$ modulo $10 ^ 9 + 7$. Here $q ^ {-1}$ denotes modular multiplicative inverse of $q$.

Complete the function `expectedNumberOfBurningCandles` which takes in three integers $n$, $m$ and $k$ and returns an integer denoting the answer as explained above. The descriptions of the robots should be taken from the standard input as described in the input format section.

## Input Format

The first line contains three integers $n$, $m$ and $k$.

The next $m$ lines contain a description of the robots. The $i^\text{th}$ of these lines contains two space-separated integers $a_i$ and $d_i$.

## Output Format

Print a single integer denoting the answer.

## Constraints

- $1 \leq n, m \leq 2 \cdot 10 ^ 5$
- $1 \leq k \leq m$
- $1 \leq a_i, d_i \leq n$

Additionally, for $25\%$ of the total points:

- $n, m \leq 3000$

## Sample Tests

### Test 1

```
4 2 1
1 2
2 2
```

### Test 2

```
2
```
