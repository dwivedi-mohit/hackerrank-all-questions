# Related Species

---

| Field | Value |
|---|---|
| **Slug** | `divyam-and-sorted-list` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 30 |
| **Contest** | indeed-prime-codesprint |
| **URL** | https://www.hackerrank.com/challenges/divyam-and-sorted-list |

---

## Preview

Find if a non decreasing sequence can be formed from two given sequences.

## Problem Statement

A group of scientists have broken down species DNA into sequences of integers. They determine that two species with the respective DNA sequences $A$ and $B$ are considered to be related if a non-decreasing sequence $C$ of the same length can be found, such that $C_i = A_i$ or $C_i = B_i$.

Given the DNA sequences for two species, help the scientists determine if they are related.

## Input Format

The first line contains an integer, $T$, the number of test cases.		

For each test case:		
The first line contains an integer, $N$, the length of the DNA sequence.		
The second line contains a sequence of space-separated integers describing species $A$.		
The third line contains a sequence of space-separated integers describing species $B$.

**Constraints:**	
$1 \le T \le 5$		
$1 \le N \le 10^5$		
$0 \le A_i,\ B_i \le 10^{10}$

## Output Format

On a new line for each test case, print **YES** if a non-decreasing sequence of the same length can be found (i.e.: species are related) or **NO** if it cannot.

## Sample Tests

### Test 1

```
3
3
1 2 3
4 4 4
3
3 2 1
6 5 4
2
1 0
10 2
```

### Test 2

```
YES
NO
YES
```
