# Impressive Tree

---

| Field | Value |
|---|---|
| **Slug** | `impressive-tree` |
| **Domain** | misc |
| **Difficulty** | Expert |
| **Score** | 90 |
| **Contest** | 101hack52 |
| **URL** | https://www.hackerrank.com/challenges/impressive-tree |

---

## Preview

Answer some queries involving a rooted tree.

## Problem Statement

You are given a weighted, rooted tree with $n$ nodes. The nodes are numbered $1$ to $n$, and the root node is $1$. The edges are numbered $1$ to $n-1$.

For a node $a$, let $D(a)$ be the *set* of descendants of $a$. Also, note that $S \setminus T$ denotes the [*set difference*](https://en.wikipedia.org/wiki/Complement_(set_theory)#Relative_complement) operation, so $D(a) \setminus D(b)$ denotes the set of descendants of $a$ that are not descendants of $b$.

You need to perform $q$ operations of two types:

- *Update*. You are given two integers $i$ and $x$, and you need to increase the weight of the $i^\text{th}$ edge by $x$.

- *Query*. You are given two nodes $u$ and $v$. A temporary edge between $u$ and $v$ of weight $1$ is added. After this query, this temporary edge is removed. For two nodes $a$ and $b$, let $d(a, b)$ be the weight of the shortest path from node $a$ to node $b$. Then the answer to this query depends on three cases:
    - If $u$ is an ancestor of $v$, the answer is the sum of $d(a, b)$ for all $a$ in $D(u) \setminus D(v)$ and for all $b$ in $D(v)$.

    - If $v$ is an ancestor of $u$, the answer is the sum of $d(a, b)$ for all $a$ in $D(u)$ and for all $b$ in $D(v) \setminus D(u)$.

    - Otherwise, the answer is the sum of $d(a, b)$ for all $a$ in $D(u)$ and for all $b$ in $D(v)$.


Note that the definition of $D(a)$ is unchanged even in the presence of a temporary edge. 

Since the answer to a query may be very large, only find the answer modulo $10^9 + 7$.

## Input Format

The first line of input contains two space-separated integers $n$ and $q$.


The next $n-1$ lines describe the edges. The $i^\text{th}$ line contains three space-separated integers $u_i, v_i, x_i$ denoting that the $i^\text{th}$ edge connects nodes $u_i$ and $v_i$ and has weight $x_i$.


The next $q$ lines describe the operations.

- For an *update* operation, there are three space-separated integers $1, i, x$. 
- For a *query* operation, there are three space-separated integers $2, u, v$.

## Output Format

For each *query* operation, print a single line containing a single integer denoting the answer for that query modulo $10^9 + 7$.

## Constraints

- $1 \le n, q \le 10^5$

- $1 \leq i < n$
- $1 \leq x_i, x \leq 10^9$
- $1 \le u_i, v_i, u, v \le n$

- $u \not= v$


**Subtasks**

- For $30\%$ of the maximum score, $n, q \le 10^3$

## Sample Tests

### Test 1

```
11 6
1 2 3
1 3 1
1 4 4
2 5 2
2 6 5
2 7 2
4 8 8
4 9 3
7 10 4
7 11 3
2 2 4
1 4 8
2 2 4
2 2 10
1 6 5
2 2 10
```

### Test 2

```
144
168
27
29
```
