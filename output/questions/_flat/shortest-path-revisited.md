# Shortest Path Revisited

---

| Field | Value |
|---|---|
| **Slug** | `shortest-path-revisited` |
| **Domain** | misc |
| **Difficulty** | Expert |
| **Score** | 120 |
| **Contest** | 101hack30 |
| **URL** | https://www.hackerrank.com/challenges/shortest-path-revisited |

---

## Preview

Find the shortest path in a graph, under the given condition.

## Problem Statement

You are given a weighted, undirected graph $G$. The nodes of $G$ are enumerated by integer numbers from $1$ to $N$, inclusively. Find the length of the shortest path from the node numbered $1$ to the node numbered $N$.

Piece of cake, isn't it? So, let's apply one more condition.

Each edge in the graph has its own **tag** - a lowercase Latin letter. Now, a string obtained by writing out the tags of the edges of the path should be a substring of the given string $S$.

Whenever you move by the edge, the weight of this edge gets multiplied by the number of occurrences of the string formed by the tags of already travelled edges (including the new one) in the string $S$.

Could you now find the length of the shortest path from the $1$<sup>st</sup> node to the $N$<sup>th</sup>?

## Input Format

The first line contains two space separated integers $N$ and $M$, denoting the number of nodes and the number of edges in the graph $G$, respectively.

The following $M$ lines contain three integers $X_i$ $Y_i$ $Z_i$, followed by a single space, and a lowercase English letter $C_i$. This denotes that there is a bidirectional edge between the $X_i$<sup>th</sup> node and the $Y_i$<sup>th</sup> node with a weight of $Z_i$ and a tag $C_i$.

The next line contains a lowercase English letter string $S$.

**Constraints**

- $2 \leq N \leq 1000$
- $1 \leq M \leq 6 \times 1000$
- $1 \leq X_i, Y_i \leq N$
- $1 \leq Z_i \leq 10^3$
- $1 \leq |S| \leq 1000$
- $S$ consists only of lowercase Latin letters.
- There is at least one path from the $1$<sup>st</sup> node to the $N$<sup>th</sup>, satisfying the given constraints.

## Output Format

Output a single line: The length of the shortest path under the given conditions.

## Sample Tests

### Test 1

```
3 3
1 2 3 a
2 3 4 b
1 3 5 c
aabb
```

### Test 2

```
10
```
