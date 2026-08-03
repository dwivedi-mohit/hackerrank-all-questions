# Project Euler #31: Coin sums

---

| Field | Value |
|---|---|
| **Slug** | `euler031` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 100 |
| **Contest** | projecteuler |
| **URL** | https://www.hackerrank.com/challenges/euler031 |

---

## Preview

Currency Change

## Problem Statement

<sub>This problem is a programming version of [Problem 31](https://projecteuler.net/problem=31) from [projecteuler.net](https://projecteuler.net/)</sub>


In England the currency is made up of pound, $£$, and pence, $p$, and there are eight coins in general circulation:


$$ \text{1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).}$$


It is possible to make $£2$ in the following way:
$$ 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p$$


How many different ways can $N$ $p$ be made using any number of coins? As the result can be large print answer mod $(10^9 + 7)$

## Input Format

The first line contains an integer $T$ , i.e., number of test cases.

Next $T$ lines will contain an integer $N$.


**Note:** N is given as $p$ and not $£$

## Output Format

Print the values corresponding to each test case.

## Constraints

$1 \le T \le 10^4$

$1 \le N \le 10^5$

## Sample Tests

### Test 1

```
3
10
15
20
```

### Test 2

```
11
22
41
```
