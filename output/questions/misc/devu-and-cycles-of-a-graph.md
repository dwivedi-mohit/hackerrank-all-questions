# Devu and Cycles of a Graph

---

| Field | Value |
|---|---|
| **Slug** | `devu-and-cycles-of-a-graph` |
| **Domain** | misc |
| **Difficulty** | Advanced |
| **Score** | 100 |
| **Contest** | 101hack23 |
| **URL** | https://www.hackerrank.com/challenges/devu-and-cycles-of-a-graph |

---

## Preview

Help Devu deal with a counting problem related to cycles of a graph.

## Problem Statement

Devu likes to play with graphs a lot. He recently found a graph of $n$ nodes and $m$ edges. Now he wants to assign each edge a weight of zero or one such that - 

-	For each cycle in the graph, the sum of the weights of it's edges is even. 
-	Sum of weights of all the edges of the graph should be even. 

Please help Devu count the number of possible assignments of weights to the edges of the graph satisfying the above conditions. Print your answer modulo $(10^9 + 7)$.

## Input Format

-	First line of input contains a single integer $T$ denoting number of test cases.
-	For each test case, the first line contains two space-separated integers, $n, m$, denoting the number of nodes and edges in the graph respectively.
-	Then, in the next $m$ lines each contain two space-separated integers $u, v$ ($1$ based indexing), denoting an edge of the graph. It is guaranteed that there is no multiedge or loop in the graph.

## Output Format

For each test case, print in a new line containing an integer denoting the answer to the problem.

**Constraints** 


-	$ 1 \leq T \leq 5$
-	$ 1 \leq n\leq 500$
-	$ 0 \leq m\leq 500$

## Sample Tests

### Test 1

```
1
3 3
1 2
2 3
3 1
```

### Test 2

```
4
```
