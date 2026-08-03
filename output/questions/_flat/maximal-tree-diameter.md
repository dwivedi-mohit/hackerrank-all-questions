# Maximal Tree Diameter

---

| Field | Value |
|---|---|
| **Slug** | `maximal-tree-diameter` |
| **Contest** | hourrank-19 |
| **Difficulty** | Hard |
| **Score** | 75 |
| **URL** | https://www.hackerrank.com/challenges/maximal-tree-diameter |

---

## Problem Statement

Consider an unrooted tree with $n$ vertices numbered from $1$ to $n$ connected by $n-1$ edges of length $1$. We define the *diameter* of a tree as the longest path between any two vertices of the tree.

We can modify the tree to maximize its diameter by performing the following moves exactly once:

* Remove one edge from the tree so that it splits into two smaller trees. 
* Pick one vertex from each of the two trees and join them by adding an edge.

For example, the diameter of the initial tree in the diagram below is $2$, but we can increase this to $3$ by removing the edge between vertices $2$ and $4$ and adding an edge connecting vertices $1$ and $4$:

![image](https://s3.amazonaws.com/hr-assets/0/1490188750-c35f58412c-torquetree5.png)

Given a tree, print the maximum possible diameter after modifying the tree.

## Input Format

The first line contains an integer denoting $n$ (the number of vertices).		
Each of the $n-1$ subsequent lines contains two space-separated integers, $u$ and $v$, defining an edge connecting vertex $u$ and vertex $v$.

## Output Format

Print the maximum possible diameter after modifying the tree.

## Constraints

- $2 \le n \le 5 \cdot 10^5$

**Subtasks**

- $2 \le n \le 3000$  for $30\%$ of the maximum score.
