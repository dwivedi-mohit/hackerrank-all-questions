# Counting Road Networks

---

| Field | Value |
|---|---|
| **Slug** | `counting-road-networks` |
| **Domain** | algorithms |
| **Difficulty** | Expert |
| **Score** | 90 |
| **URL** | https://www.hackerrank.com/challenges/counting-road-networks |

---

## Preview

Find the number of ways to build roads connecting different numbers of cities.

## Problem Statement

Lukas is a Civil Engineer who loves designing road networks to connect $n$ cities numbered from $1$ to $n$. He can build any number of bidirectional roads as long as the resultant network satisfies these constraints:

1. It must be possible to reach any city from any other city by traveling along the network of roads.

2. No two roads can directly connect the same two cities. 

3. A road cannot directly connect a city to itself.


In other words, the roads and cities must form a simple connected labeled graph.

You must answer $q$ queries, where each query consists of some $n$ denoting the number of cities Lukas wants to design a bidirectional network of roads for. For each query, find and print the number of ways he can build roads connecting $n$ cities on a new line; as the number of ways can be quite large, print it modulo $663224321$.

## Input Format

The first line contains an integer, $q$, denoting the number of queries.  	
Each of the $q$ subsequent lines contains an integer denoting the value of $n$ for a query.

## Output Format

For each of the $q$ queries, print the number of ways Lukas can build a network of bidirectional roads connecting $n$ cities, modulo $663224321$, on a new line.

## Constraints

+ $1 \le q, n \le 10^5$

## Sample Tests

### Test 1

```
3
1
3
10
```

### Test 2

```
1
4
201986643
```
