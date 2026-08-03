# BFS: Shortest Reach in a Graph

---

| Field | Value |
|---|---|
| **Slug** | `ctci-bfs-shortest-reach` |
| **Domain** |  |
| **Difficulty** | Hard |
| **Score** | 45 |
| **URL** | https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach |

---

## Preview

Implement a Breadth First Search (BFS).

## Problem Statement

Consider an undirected graph consisting of $n$ nodes where each node is labeled from $1$ to $n$ and the edge between any two nodes is always of length $6$. We define node $s$ to be the starting position for a BFS.  Given a graph, determine the distances from the start node to each of its descendants and return the list in node number order, ascending.  If a node is disconnected, it's distance should be $-1$.

For example, there are $n = 6$ nodes in the graph with a starting node $s = 1$.  The list of $edges = [[1,2],[2,3],[3,4],[1,5]]$, and each has a weight of $6$.



![image](https://s3.amazonaws.com/hr-assets/0/1528143002-2e9a521ad9-bfs_shortestExample.png)

Starting from node $1$ and creating a list of distances, for nodes $2$ through $6$ we have $distances = [6, 12, 18, 6, -1]$.


**Function Description**

Define a Graph class with the required methods to return a list of distances.

## Input Format

The first line contains an integer, $q$, the number of queries.


Each of the following $q$ sets of lines is as follows:


- The first line contains two space-separated integers, $n$ and $m$, the number of nodes and the number of edges.

- Each of the next $m$ lines contains two space-separated integers, $u$ and $v$, describing an edge connecting node $u$ to node $v$.

- The last line contains a single integer, $s$, the index of the starting node.

## Output Format

For each of the $q$ queries, print a single line of $n - 1$ space-separated integers denoting the shortest distances to each of the $n - 1$ other nodes from starting position $s$. These distances should be listed sequentially by node number (i.e., $1, 2, \ldots, n$), but *should not* include node $s$. If some node is unreachable from $s$, print $-1$ as the distance to that node.

## Constraints

* $1 \le q \le 10$

* $2 \le n \le 1000$

* $1 \le m \le \frac{n \cdot (n - 1)}{2}$

* $1 \le u, v, s \le n$

## Sample Tests

### Test 1

```
2
4 2
1 2
1 3
1
3 1
2 3
2
```

### Test 2

```
6 6 -1
-1 6
```
