# Sherlock and Queries on the Graph

---

| Field | Value |
|---|---|
| **Slug** | `sherlock-and-queries-on-the-graph` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 120 |
| **Contest** | 101hack26 |
| **URL** | https://www.hackerrank.com/challenges/sherlock-and-queries-on-the-graph |

---

## Problem Statement

_My dear Watson, I cannot agree with those who rank modesty among the virtues. To the logician all things should be seen exactly as they are, and to underestimate one’s self is as much a departure from truth as to exaggerate one’s own powers._

Watson has one interesting problem for Sherlock based on graphs. He gives him a connected, unweighted, and undirected graph of $N$ vertices and $M$ edges. Now, he wants Sherlock to find the answer to $Q$ queries of the following form:

$A$ $B$ $C$ $D$ : For the current query add an edge between nodes numbered $A$ and $B$ (note that this operation is temporary and only for the current query). Now, output the maximum number of bridge edges occuring on any path between $C$ and $D$. A bridge edge is an edge on whose removal the number of connected components in the graph increase by one.

## Input Format

The first line contains $N$, $M$, and $Q$. Each of the next $M$ lines contain a pair of integers $A$ and $B$, denoting an undirected, unweighted edge between $A$ and $B$.

Each of the next $Q$ lines contain four integers denoting the queries.

## Output Format

For each query, print the required answer in one line.

**Constraints**


$1 \le N, M, Q \le 10^5$ 

$1 \le A, B, C, D \le N$

## Sample Tests

### Test 1

```
6 6 2
1 2
1 3
2 3
1 4
3 5
3 6
4 6 1 2
4 6 4 5
```

### Test 2

```
0
1
```
