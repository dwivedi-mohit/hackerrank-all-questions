# Components in a graph

---

| Field | Value |
|---|---|
| **Slug** | `components-in-graph` |
| **Domain** | data-structures |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/components-in-graph |

---

## Preview

Given a graph, print the maximum and the minimum number of vertices in it's connected components.

## Problem Statement

There are $2 \times N$ nodes in an undirected graph, and a number of edges connecting some nodes.  In each edge, the first value will be between $1$ and $N$, inclusive.  The second node will be between $N+1$ and $2 \times N$, inclusive.  Given a list of edges, determine the size of the smallest and largest connected components that have $2$ or more nodes.  A node can have any number of connections.  The highest node value will always be connected to at least $1$ other node.  


**Note**
Single nodes should not be considered in the answer. 

**Example**

$bg = [[1, 5],[1, 6], [2, 4]]$





![image](https://s3.amazonaws.com/hr-assets/0/1610643454-3d793cb76a-connectedcomponentsexample.svg)

The smaller component contains $2$ nodes and the larger contains $3$.  Return the array $[2, 3]$.  


**Function Description** 

Complete the *connectedComponents* function in the editor below.


*connectedComponents* has the following parameter(s):

-	*int bg[n][2]:* a 2-d array of integers that represent node ends of graph edges
  

**Returns**

-	*int[2]:* an array with 2 integers, the smallest and largest component sizes

## Input Format

The first line contains an integer $n$, the size of $bg$.

Each of the next $n$ lines contain two space-separated integers, $bg[i][0]$ and $bg[i][1]$.

## Constraints

- $1 \le number of nodes N \le 15000$

- $1 \le bg[i][0] \le N$

- $N+1 \le bg[i][1] \le 2N$

## Sample Tests

### Test 1

```
STDIN Function
----- --------
5 bg[] size n = 5
1 6 bg = [[1, 6],[2, 7], [3, 8], [4,9], [2, 6]]
2 7
3 8
4 9
2 6
```

### Test 2

```
2 4
```
