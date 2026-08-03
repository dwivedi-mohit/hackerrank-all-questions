# Sherlock and Counting

---

| Field | Value |
|---|---|
| **Slug** | `sherlock-and-counting` |
| **Domain** | mathematics |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/sherlock-and-counting |

---

## Preview

Help Sherlock count numbers satisfying an inequality.

## Problem Statement

Watson gives Sherlock two integers, $n$ and $k$, and asks him to count the number of positive integer $i$'s such that: 

$$i \cdot (n-i) \le n \cdot k, \text{ and } i < n$$


Given $q$ queries where each query consists of some $n$ and $k$, print the number of possible $i$'s for each query on a new line.

## Input Format

The first line contains an integer, $q$, denoting the number of times Watson queries Sherlock. 		
Each of the $q$ subsequent lines contains two space-separated integers denoting the respective values of $n$ and $k$ for a query.

## Output Format

For each query, print the number of $i$'s satisfying the given formula on a new line.

## Constraints

- $1 \le q \le 10^5$ 

- $1 \le n, k \le 10^9$

## Sample Tests

### Test 1

```
2
5 1
5 2
```

### Test 2

```
2
4
```
