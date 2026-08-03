# Lazy White Falcon

---

| Field | Value |
|---|---|
| **Slug** | `lazy-white-falcon` |
| **Domain** | data-structures |
| **Difficulty** | Hard |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/lazy-white-falcon |

---

## Preview

Execute queries on the nodes of a tree.

## Problem Statement

White Falcon just solved the data structure problem below using heavy-light decomposition. Can you help her find a new solution that doesn't require implementing any fancy techniques? 

There are $2$ types of query operations that can be performed on a tree:

1. `1 u x`: Assign $x$ as the value of node $u$.
2. `2 u v`: Print the sum of the node values in the unique path from node $u$ to node $v$.

Given a tree with $N$ nodes where each node's value is initially $0$, execute $Q$ queries.

## Input Format

The first line contains $2$ space-separated integers, $N$ and $Q$, respectively.		
The $N - 1$ subsequent lines each contain $2$ space-separated integers describing an undirected edge in the tree.		
Each of the $Q$ subsequent lines contains a query you must execute.

## Output Format

For each type-$2$ query, print its integer result on a new line.

## Constraints

- $1 \leq N,Q \leq 10^5$
- $1 \leq x \leq 1000$
- It is guaranteed that the input describes a connected tree with $N$ nodes. 
- Nodes are enumerated with $0$-based indexing.

## Sample Tests

### Test 1

```
3 3
0 1
1 2
1 0 1
1 1 2
2 0 2
```

### Test 2

```
3
```
