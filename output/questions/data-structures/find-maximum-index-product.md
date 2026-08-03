# Find Maximum Index Product

---

| Field | Value |
|---|---|
| **Slug** | `find-maximum-index-product` |
| **Domain** | data-structures |
| **Difficulty** | Medium |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/find-maximum-index-product |

---

## Preview

Given N numbers, for each index find the greatest index less than the current and the smallest index greater than current, such that the current value is less than the chosen index and maximise the product of the chosen indices..

## Problem Statement

You are given a list of $N$ numbers $a_{1}, a_{2}, \ldots, a_{n}$. For each element at position $i$ ($1 \le i \le N$), we define $Left(i)$ and $Right(i)$ as:

$Left(i)$ = closest index j such that j < i and $a_j>a_i$. If no such j exists then $Left(i)$ = 0.

$Right(i)$ = closest index k such that k > i and $a_k>a_i$. If no such k exists then $Right(i)$ = 0. 


We define $IndexProduct(i)$ = $Left(i)$ * $Right(i)$. You need to find out the maximum $IndexProduct(i)$ among all i.

## Input Format

The first line contains an integer $N$, the number of integers.
The next line contains the $N$ integers describing the list a[1..N].

**Constraints** 

$1 \le N \le 10^{5}$

$1 \le a_i \le 10^9$

## Output Format

Output the maximum $IndexProduct$ among all indices from $1$ to $N$.

## Sample Tests

### Test 1

```
5
5 4 3 4 5
```

### Test 2

```
8
```
