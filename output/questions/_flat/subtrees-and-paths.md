# Subtrees And Paths

---

| Field | Value |
|---|---|
| **Slug** | `subtrees-and-paths` |
| **Domain** | data-structures |
| **Difficulty** | Advanced |
| **Score** | 120 |
| **URL** | https://www.hackerrank.com/challenges/subtrees-and-paths |

---

## Preview

Given a tree with N nodes, perform queries like add value to all nodes subrooted at a given node and find maximum value on a given path.

## Problem Statement

Given a rooted tree of $N$ nodes, where each node is uniquely numbered in between *[1..N]*. The node 1 is the root of the tree. Each node has an integer value which is initially 0.

You need to perform the following two kinds of queries on the tree:

* *add t value*: Add value to all nodes in subtree rooted at *t*
* *max a b*: Report maximum value on the path from *a* to *b*

## Input Format

First line contains *N*, number of nodes in the tree. Next *N-1* lines contain two space separated integers *x* and *y* which denote that there is an edge between node *x* and node *y*.

Next line contains *Q*, the number of queries to process.

Next *Q* lines follow with either *add* or *max* query per line.

**Constraints**

$1 \le N \le 10^5$

$1 \le Q \le 10^5$

$1 \le t, a, b, x, y \le N$  

$x \ne y$  

$-10^4 \le value \le 10^4$

## Output Format

For each *max* query output the answer in a separate line.

## Sample Tests

### Test 1

```
5
1 2
2 3
2 4
5 1
6
add 4 30
add 5 20
max 4 5
add 2 -20
max 4 5
max 3 4
```

### Test 2

```
30
20
10
```
