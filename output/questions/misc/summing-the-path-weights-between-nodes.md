# Summing the Path Weights Between Nodes

---

| Field | Value |
|---|---|
| **Slug** | `summing-the-path-weights-between-nodes` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 50 |
| **Contest** | 101hack49 |
| **URL** | https://www.hackerrank.com/challenges/summing-the-path-weights-between-nodes |

---

## Preview

Sum the weights of all simple paths from red nodes to black nodes in a tree

## Problem Statement

We define the following terms:

- *Simple Path:* A path that doesn't contain any node or edge more than once.

- *Simple Cycle:* A cycle that doesn't contain any node or edge more than once.

- *[Tree](https://en.wikipedia.org/wiki/Tree_(graph_theory)):* A connected, undirected graph with no simple cycles.

![image](https://s3.amazonaws.com/hr-assets/0/1495001775-e291cea4c0-TotalDistanceBetweenNodes1.png)

Given an [edge-weighted tree](https://en.wikipedia.org/wiki/Glossary_of_graph_theory_terms#weighted_graph) with $n$ nodes numbered from $1$ to $n$ where each node is either *red* or *black*, find and print the sum of the weights of all unique *simple* paths from a *red* node to a *black* node in the tree.

## Input Format

The first line contains an integer, $n$, denoting the number of nodes in the tree. 	
The second line contains $n$ space-separated binary integers describing the respective values of $c_1, c_2, \ldots, c_n$, where a $c_i$ value of $0$ denotes that node $i$ is *red* and a value of $1$ denotes it's *black*.		
Each of the $n-1$ subsequent lines contains three space-separated integers describing the respective values of $u$, $v$, and $w$ that define an edge with weight $w$ connecting nodes $u$ and $v$.

## Output Format

Print an integer denoting the sum of the weights of all unique simple paths from a red node to a black node in the tree.

## Constraints

- $1 \leq n \leq 10^5$

- Each $c_i$ is in the set $\{0,1\}$, where $0$ denotes *red* and $1$ denotes *black*.
- $1 \leq u, v \leq n$

- $1 \leq w \leq 10^6$


**Subtasks**


- For $33.33\%$ of the maximum score, $n \le 6000$

## Sample Tests

### Test 1

```
4
0 0 1 1
1 2 1
2 3 2
2 4 2
```

### Test 2

```
10
```
