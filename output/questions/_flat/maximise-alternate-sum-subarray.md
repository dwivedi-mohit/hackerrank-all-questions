# Maximize Alternate Sum Subarray

---

| Field | Value |
|---|---|
| **Slug** | `maximise-alternate-sum-subarray` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 100 |
| **Contest** | 101hack27 |
| **URL** | https://www.hackerrank.com/challenges/maximise-alternate-sum-subarray |

---

## Problem Statement

You are given a sequence $C$ of $N$ integers. $C[1]$ represents the first element of the sequence and $C[N]$ represents the last element of the sequence.


You need to process $2$ types of queries on this sequence:


**Query 1: U X Y** 

For this query, you need to change the sequence's $X^{th}$ element to $Y$, i.e. $C[X] = Y$.


**Query 2: Q A B**

For this query, you need to print:

$max${$C[i] - C[i+1] + C[i+2] - C[i+3] + ....C[j]$ $|$ $A$ &le; $i$ &le; $j$ &le; $B$}  


More formally, consider the array from position $A$ to $B$ only, now find a subarray in this array which maximizes alternative plus minus sum of the array.

## Input Format

The first line contains $N$, which represents the number of elements of the sequence.

The next line contains $N$ space-separated elements of the sequence.

The next line contains $Q$, the number of queries to follow.

$Q$ queries follow; each query can be either of type 1 or type 2 on a separate line.

## Output Format

For each query of type $2$, output the answer in a new line.


**Constraints**

$1 \le N \le 10^5$

$1 \le Q \le 2 \times 10^5$

$abs(C[i]) \le 10^9$

## Sample Tests

### Test 1

```
10
-6 -900 -7 5 -2 -7 -4 3 3 3
5
Q 1 3
Q 8 10
Q 6 8
Q 3 3
Q 4 8
```

### Test 2

```
894
3
3
-7
7
```
