# Tree Isomorphism

---

| Field | Value |
|---|---|
| **Slug** | `tree-isomorphism` |
| **Contest** | hourrank-21 |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/tree-isomorphism |

---

## Problem Statement

Little Alexey was playing with trees while studying two new awesome concepts: *subtree* and *isomorphism*. 

A *[tree](https://en.wikipedia.org/wiki/Tree_(graph_theory))* is a connected, undirected graph with no cycles. We can denote a tree by a pair $(V, E)$, where $V$ is the set of vertices and $E$ is the set of edges. Here's an example of a tree:   

![image](https://s3.amazonaws.com/hr-assets/0/1495799530-8f89e74622-TreeIsomorphism1.png)

Let $V'$ be a subset of $V$, and let $E'$ be the set of edges between the vertices in $V'$. If the graph $(V', E')$ is is a tree, then it is called a *subtree* of $G$. Here's an example of a subtree of the tree above:  

![image](https://s3.amazonaws.com/hr-assets/0/1495799540-e1c2027b06-TreeIsomorphism2.png)

Two trees are said to be [*isomorphic*](https://en.wikipedia.org/wiki/Graph_isomorphism) if they contain the same number of vertices and those vertices are connected in the same way. For example, the following two trees are isomorphic:

![image](https://s3.amazonaws.com/hr-assets/0/1495799559-24edbfc8c1-TreeIsomorphism3.png)

More formally, two trees $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ are said to be isomorphic if there exists a one-to-one correspondence $f : V_1 \rightarrow V_2$ such that $(u, v) \in E_1$ if and only if $(f(u), f(v)) \in E_2$.  

Now he wonders, how many non-isomorphic trees can he construct using such a procedure? He asks you for help!

## Input Format

The first line contains a single integer $n$ denoting the number of vertices of the tree. The number of edges is $n - 1$. The vertices are numbered $1$ to $n$.  

The next $n - 1$ lines describe the edges of the tree. The $i^\text{th}$ such line contains two space-separated integers $a_i$ and $b_i$ denoting the vertices that the $i^\text{th}$ edge connects.

## Output Format

Print a single line containing a single integer denoting the number different non-isomorphic trees that Little Alexey can obtain.

## Constraints

- $1 \le n \le 19$
- $1 \le a_i, b_i \le n$
- It's guaranteed that the given graph forms a tree.
