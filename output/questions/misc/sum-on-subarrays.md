# Sum on Subarrays 

---

| Field | Value |
|---|---|
| **Slug** | `sum-on-subarrays` |
| **Domain** | misc |
| **Difficulty** | Expert |
| **Score** | 85 |
| **Contest** | 101hack48 |
| **URL** | https://www.hackerrank.com/challenges/sum-on-subarrays |

---

## Preview

Find the sum of a certain function for all subarrays of a given array.

## Problem Statement

Pranjal and Jillian have an array of $n$ elements, $a = [a_0, a_1, \ldots, a_{n-1}]$. For some subarray, $b$, of $a$, we define $G(b)$ as:

$$\Large G(b) = \max_{\substack{i, j \\ 0 \le i \le j \lt \operatorname{length}(b)}} |b_i - b_j|^2$$

where $\operatorname{length}(b)$ is the length of $b$, and $b_i$ is the $i^\text{th}$ element of $b$. 


They calculate the sum of $G(b)$ for all possible subarrays $b$ of $a$ by computing:

$$\Large \sum_{\substack{l, r \\ 0 \le l \le r \lt n}} G(a_{l\ldots r})$$

where $a_{l\ldots r}$ is the subarray of $a$ from index $l$ to index $r$.


Given $a$, print the sum above modulo $2^{64}$.

## Input Format

The first line contains an integer denoting $n$ (the size of the array). 	
The second line contains $n$ space-separated integers describing the respective values of $a_0, a_1, \ldots, a_{n-1}$.

## Output Format

Print an integer denoting the sum, modulo $2^{64}$.

## Constraints

- $1\le n \le 2\times 10^5$

- $1\le a_i \le 2\times 10^5$

## Sample Tests

### Test 1

```
5
1 2 3 4 5
```

### Test 2

```
50
```

### Test 3

```
4
3 1 4 2
```

### Test 4

```
44
```
