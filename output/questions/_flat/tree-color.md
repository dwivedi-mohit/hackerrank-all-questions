# Tree Color

---

| Field | Value |
|---|---|
| **Slug** | `tree-color` |
| **Domain** | misc |
| **Difficulty** | Expert |
| **Score** | 100 |
| **Contest** | 101hack41 |
| **URL** | https://www.hackerrank.com/challenges/tree-color |

---

## Preview

Perform queries on a tree.

## Problem Statement

You are given a tree consisting of $n$ vertices where each vertex $i$ has:

- A color, $c_i$, assigned to it. 
- A value, $value_i$, assigned to it. Initially, the values in all vertices are $0$.

You must answer $q$ queries of the following two types:

1. `1 v c s`: Add the number $s$ to all vertices, $u$, such that there are no vertices having a color equal to $c$ on the path between $u$ and $v$.
2. `2 v`: Print the current value in vertex $v$ (i.e., $value_v$) on a new line.

Assume that you have a variable called $lastAns$ that's initially equal to $0$ and subsequently always stores the result of the last type `2` query. *Instead of original numbers in all queries, you'll be given the XOR ($\oplus$) of the number with $lastAns$ except the type of the query.* In other words, if $lastAns = 1$, $v = 3$, $c = 5$, and $s = 2$, then $v = 2 \cdot (3 \oplus 1)$, $c = 4 \cdot (5 \oplus 1)$, and $s = 3 \cdot (2 \oplus 1)$.

Given the definition for the tree and $q$ queries, perform each query in order. For each query of type `2 v`, print the current value in vertex $v$ on a new line.

## Input Format

The first line consists of a single integer, $n$, denoting the number of vertices in the tree. 		
The second line consists of $n$ space-separated integers where each integer $i$ ($1 \le i \le n$) denotes the color, $c_i$, assigned to vertex $i$.		
Each of the $n - 1$ subsequent lines consist of two space-separated integers, $a$ and $b$, defining an edge between vertices $a$ and $b$.		
The next line contains a single integer, $q$, denoting the number of queries. 	
Each of the $q$ subsequent lines contains a query in the format described above (note that these may be larger than a $32$-bit type).

## Output Format

For each query of type `2 v`, print the value of vertex $v$ on a new line.

## Constraints

- $1 \le n, q \le 10^5$
- $1 \le a, b \le n$
- $1 \le v, c \le n$
- $0 \le s \le 10^9$
- These constraints relating to query values are possible *only after* XOR with $lastAns$, so be aware that the numbers received as input may not fit in a $32$-bit type.
- The environment time limits for popular competitive programming languages have been *doubled* for this challenge. See the default limits at our [Environment](/environment) page.

## Sample Tests

### Test 1

```
5
1 2 1 2 1
1 3
1 2
2 4
2 5
8
1 1 2 4
2 3
2 0
2 5
1 4 2 1
2 4
1 2 3 5
2 1
```

### Test 2

```
4
0
0
0
9
```
