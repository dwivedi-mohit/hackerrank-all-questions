# Counting On a Tree

---

| Field | Value |
|---|---|
| **Slug** | `counting-on-a-tree` |
| **Domain** | data-structures |
| **Difficulty** | Expert |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/counting-on-a-tree |

---

## Preview

Given a tree, count the number of ordered pairs satisfying some conditions.

## Problem Statement

Taylor loves [trees](https://en.wikipedia.org/wiki/Tree_(graph_theory)), and this new challenge has him stumped!

Consider a tree, $t$, consisting of $n$ nodes. Each node is numbered from $1$ to $n$, and each node $i$ has an integer, $c_i$, attached to it. 

A *query* on tree $t$ takes the form `w x y z`. To process a query, you must print the count of ordered pairs of integers $(i, j)$ such that the following four conditions are all satisfied: 

- $i \ne j$
- $i \in$ the path from node $w$ to node $x$.
- $j \in$ path from node $y$ to node $z$.
- $c_i = c_j$


Given $t$ and $q$ queries, process each query in order, printing the pair count for each query on a new line.

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of nodes) and $q$ (the number of queries). 	
The second line contains $n$ space-separated integers describing the respective values of each node (i.e., $c_1, c_2, \ldots, c_n$). 	
Each of the $n - 1$ subsequent lines contains two space-separated integers, $u$ and $v$, defining a bidirectional edge between nodes $u$ and $v$.		
Each of the $q$ subsequent lines contains a `w x y z` query, defined above.

## Output Format

For each query, print the count of ordered pairs of integers satisfying the four given conditions on a new line.

## Constraints

* $1 \le n \le 10^5$

* $1 \le q \le 50000$

* $1 \le c_i \le 10^9$

* $1 \le u, v, w, x, y, z \le n$


Scoring for this problem is Binary, that means you have to pass all the test cases to get a positive score.

## Sample Tests

### Test 1

```
10 5
10 2 3 5 10 5 3 6 2 1
1 2
1 3
3 4
3 5
3 6
4 7
5 8
7 9
2 10
8 5 2 10
3 8 4 9
1 9 5 9
4 6 4 6
5 8 5 8
```

### Test 2

```
0
1
3
2
0
```
