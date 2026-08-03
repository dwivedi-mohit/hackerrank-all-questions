# White Falcon And Tree

---

| Field | Value |
|---|---|
| **Slug** | `white-falcon-and-tree` |
| **Domain** | data-structures |
| **Difficulty** | Hard |
| **Score** | 120 |
| **URL** | https://www.hackerrank.com/challenges/white-falcon-and-tree |

---

## Preview

Given a tree with N nodes and two queries, maintain the tree under these two queries.

## Problem Statement

White Falcon has a tree with $N$ nodes. Each node contains a linear function. Let's denote by $f_u(x)$ the linear function contained in the node $u$.


Let's denote the path from node $u$ to node $v$ like this: $p_1,p_2,p_3,\ldots,p_k$, where $p_1 = u$ and $p_k = v$, and $p_i$ and $p_{i+1}$ are connected.


White Falcon also has $Q$ queries. They are in the following format:


1. $1$ $u$ $v$ $a$ $b$. Assign $ax + b$ as the function of all the nodes on the path from $u$ to $v$, i.e., $f_{p_i}(x)$ is changed to $ax+b$ where $p_1,p_2,p_3,\ldots,p_k$ is the path from $u$ to $v$.

2. $2$ $u$ $v$ $x$. Calculate $f_{p_k}(f_{p_{k-1}}(f_{p_{k-2}}(\ldots f_{p_1}(x))))$ modulo $(10^9 + 7)$

## Input Format

The first line contains $N$, the number of nodes. The following $N$ lines each contain two integers $a$ and $b$ that describe the function $ax + b$.


Following $N - 1$ lines contain edges of the tree. 

The next line contains $Q$, the number of queries. Each subsequent line contains one of the queries described above.

## Output Format

For every query of the second kind, print one line containing an integer, the answer for that query.


**Constraints**

$1 \leq  N \leq  50000$ (Number of nodes) 

$1 \leq  Q \leq  50000$ (Number of queries) 

$0 \leq a, b, x < 10^9 + 7$

## Sample Tests

### Test 1

```
2
1 1
1 2
1 2
2
1 2 2 1 1
2 1 2 1
```

### Test 2

```
3
```
