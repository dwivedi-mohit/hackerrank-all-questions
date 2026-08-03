# Summing the N series 

---

| Field | Value |
|---|---|
| **Slug** | `summing-the-n-series` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/summing-the-n-series |

---

## Preview

Sum the N series.

## Problem Statement

There is a sequence whose $n^{\text{th}}$ term is

$$T_n = n^2 - (n-1)^2$$


Evaluate the series

$$S_n = T_1 + T_2 + T_3 + \cdots + T_n$$

Find $S_n \bmod (10^9+7)$.


**Example**


$n = 3$


The series is $1^2-0^2 + 2^2-1^2 + 3^2-2^2 = 1 + 3 + 5 = 9$.


**Function Description**


Complete the *summingSeries* function in the editor below.


*summingSeries* has the following parameter(s):


- *int n:* the inclusive limit of the range to sum


**Returns**


- *int:* the sum of the sequence, modulo $(10^9+7)$

## Input Format

The first line of input contains $t$, the number of test cases.

Each test case consists of one line containing a single integer $n$.

## Constraints

+ $1 \le t \le 10$

+ $1 \le n \le 10^{16}$

## Sample Tests

### Test 1

```
2
2
1
```

### Test 2

```
4
1
```
