# Max-Min Difference in an Interval

---

| Field | Value |
|---|---|
| **Slug** | `max-min-difference-in-an-interval` |
| **Contest** | hourrank-18 |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/max-min-difference-in-an-interval |

---

## Problem Statement

Consider an array of integers, $A=[a_0, a_1, \ldots , a_{n-1}]$. Let $max(b, e)$ and $min(b, e)$ be the respective maximum and minimum values in the inclusive range between index $b$ and $e$. 

Given $A$, perform $q$ queries where each query consists of two integers, $low$ and $high$. For each query, find and print the number of $(b,e)$ pairs that satisfy the following:

- $0 \le b \le e < n$
- $low \le max(b, e) - min(b, e) \le high$.

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the size of array $A$) and $q$ (the number of queries).		
The second line contains $n$ space-separated integers describing the respective values of $a_0, a_1, \ldots , a_{n-1}$.		
Each line $j$ of the $q$ subsequent lines contains two space-separated integers describing the respective values of $low_j$ and $high_j$ for the $j^{th}$ query.

## Output Format

Print $q$ lines where each line $j$ is the number of possible pairs for the $j^{th}$ query.

## Constraints

- $ 1 \le n \le 5 \times 10^5$
- $ n \times q \le 2 \times 10^6$
- $ 1 \le a_i \le 10^9$
- $ 1 \le low_j \le high_j \le 10^9$ for $0 \le j < q$
