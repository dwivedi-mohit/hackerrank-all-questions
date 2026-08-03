# Array Partition

---

| Field | Value |
|---|---|
| **Slug** | `array-partition` |
| **Contest** | hourrank-29 |
| **Difficulty** | Medium |
| **Score** | 45 |
| **URL** | https://www.hackerrank.com/challenges/array-partition |

---

## Problem Statement

Given an array $A$ consisting of $N$ positive integers, split the array $A$ into $2$ non empty subsets $P$ and $Q$ such that an element from array $A$ either belongs to subset $P$ or to subset $Q$ and $\gcd(\prod{P_i}, \prod{Q_i}) = 1$. Calculate the number of ways of splitting the array $A$ into 2 subsets $P$ and $Q$. 

Since the answer can be quite large, print it modulo $10^9 + 7$.

## Input Format

First line of input contains a single integer $T$ denoting number of test cases.    
First line of each test case contains a single integer $N$ denoting size of array $A$.  
Second line of each test case contains $N$ space separated integer denoting elements of array $A$.

## Output Format

Output consists of $T$ lines, where $i^{th}$ lines contains required answer for $i^{th}$ test cases.

## Constraints

* $1 \le T \le 5$
* $1 \le N \le 10^5$
* $1 \le A_i \le 10^6$

**Scoring**

* $1 \le N \le 15, 1 \le A_i \le 15$ for $20\%$ test data.
* $1 \le N \le 1000, 1 \le A_i \le 10^6$ for $50\%$ test data.
* $1 \le N \le 10^5, 1 \le A_i \le 10^6$ for $100\%$ test data.
