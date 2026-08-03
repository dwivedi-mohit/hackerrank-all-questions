# Flipping bits

---

| Field | Value |
|---|---|
| **Slug** | `one-month-preparation-kit-flipping-bits` |
| **Domain** |  |
| **Difficulty** | Easy |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/one-month-preparation-kit-flipping-bits |

---

## Preview

Flip bits in its binary representation.

## Problem Statement

You will be given a list of 32 bit unsigned integers. Flip all the bits ($1 \rightarrow 0$ and $0 \rightarrow 1$) and return the result as an unsigned integer.


**Example** 

$n = 9_{10}$ 


$ 9_{10} = 1001_2$.  We're working with 32 bits, so:


$00000000000000000000000000001001_2 = 9_{10}$

$11111111111111111111111111110110_2 = 4294967286_{10}$


Return $4294967286$.
 
**Function Description**

Complete the *flippingBits* function in the editor below.


flippingBits has the following parameter(s):

- *int n:* an integer 


**Returns** 


- *int:* the unsigned decimal integer result

## Input Format

The first line of the input contains $q$, the number of queries. 

Each of the next $q$ lines contain an integer, $n$, to process.

## Constraints

$1 \le q \le 100$

$0 \le n \lt 2^{32}$

## Sample Tests

### Test 1

```
3 
2147483647 
1 
0
```

### Test 2

```
2147483648 
4294967294 
4294967295
```
