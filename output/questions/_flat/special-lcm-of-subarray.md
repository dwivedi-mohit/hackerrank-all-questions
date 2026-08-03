# Special LCM of Subarray

---

| Field | Value |
|---|---|
| **Slug** | `special-lcm-of-subarray` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 40 |
| **Contest** | 101hack27 |
| **URL** | https://www.hackerrank.com/challenges/special-lcm-of-subarray |

---

## Problem Statement

You are given an array of integers $A$ of size $N$ where $N$ is an **even number**.

Array $A$ will contain $N/2$ distinct prime numbers and each prime will occur exactly **twice** in the array. 


You need to answer $Q$ queries.

For each query, let $S$ = prime numbers from $L$ to $R$ which occur only once.

Output the $LCM$ $modulo$ $3$ of $S$ for each query.


**Constraints**

$2 \le N \le 10^5$

$1 \le Q \le 10^5$

$1 \le A[i] \le 10^6$

$A[i]$ is a **prime number**

$N$ is an **even number**

## Input Format

The first line of input contains $N$ and $Q$, separated by space. The next line contains $N$ space-separated integers. $Q$ queries follow, each containing two integers, $L$ and $R$, separated by a space.

## Output Format

For each query, output the result as asked above.

## Sample Tests

### Test 1

```
10 3
3 5 11 3 7 13 5 7 11 13
2 4
2 3
5 9
```

### Test 2

```
0
1
1
```
