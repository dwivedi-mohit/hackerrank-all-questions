# Beautiful Sets

---

| Field | Value |
|---|---|
| **Slug** | `polita-sets` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 75 |
| **URL** | https://www.hackerrank.com/challenges/polita-sets |

---

## Preview

Count the number of beautiful Sets.

## Problem Statement

Consider a set, $S$, consisting of $k$ integers. The set is *beautiful* if *at least one* of the following conditions holds true for every $x \in S$:

1. $x-1 \in S$
2. $x+1 \in S$

For example, $S = \{1, 2, 50, 51\}$ is *beautiful* but $S = \{1, 5, 9\}$ is *not beautiful*. Given two integers, $n$ and $k$, can you find the number of different $k$-element beautiful sets you can create using integers $\in [1, n]$?

Perform $q$ queries where each query $i$ consists of some $n_i$ and $k_i$. For each query:

- Find the number of different beautiful sets having exactly $k$ elements that can be generated using integers in the inclusive range from $1$ to $n$. 
- Print the number of beautiful sets, modulo $10^9+7$, on a new line.

## Input Format

The first line contains an integer, $q$, denoting the number of queries.	
Each line $i$ of the $q$ subsequent lines consists of two space-separated positive integers describing the respective values of $n_i$ and $k_i$ for the query.

## Output Format

For each query, print the number of different beautiful sets of size $k$ that can be generated using integers in the inclusive range from $1$ to $n$ on a new line. As the answers to these queries can be quite large, each answer must be modulo $10^9+7$.

## Constraints

* $1 \le q \le 10$ 

* $1 \le n \le 10^6$ 
* $1 \le k \le n$


**Subtasks**

* $1 \le n \le 1000$  for $40\%$ of the maximum score.

## Sample Tests

### Test 1

```
2
6 4
27 2
```

### Test 2

```
6
26
```
