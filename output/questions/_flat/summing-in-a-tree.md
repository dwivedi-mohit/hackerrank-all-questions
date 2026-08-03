# Summing in a Tree

---

| Field | Value |
|---|---|
| **Slug** | `summing-in-a-tree` |
| **Domain** | misc |
| **Difficulty** | Expert |
| **Score** | 80 |
| **Contest** | 101hack47 |
| **URL** | https://www.hackerrank.com/challenges/summing-in-a-tree |

---

## Preview

Given a tree and a sequence of numbers, find the result of a given summation.

## Problem Statement

You have a directed tree with $n$ nodes numbered $0, 1, 2, \ldots, n-1$ that is rooted at node $0$. A *directed tree* means that all edges are directed and point *away* from the root node. For example, the diagram below depicts a directed tree with $n = 8$ nodes:


![image](https://s3.amazonaws.com/hr-assets/0/1489572938-b7bf5dc8e4-sherlock-and-tree-1-ex.png)

We define:

- $\textrm{level}(u)$ as the edge distance between node $u$ and the root node.
- the *height*, $h$, of the tree as the maximum $\textrm{level}$ of any node.
- $\textrm{subtree}(u)$ as the set of nodes reachable from node $u$ (note that this includes node $u$).
- $f(l, k)$ as the number of nodes $v$ such that $\textrm{subtree}(v)$ contains at least $k$ nodes whose $\textrm{level}$ is $l$.

    More formally, suppose we define $S_{v,l}$ as the set $\{u \in \textrm{subtree}(v) \mid \textrm{level}(u) = l\}$.  Then $f(l, k)$ is the number of nodes $v$ such that $\left\vert{S_{v,l}}\right\vert \ge k$.

Given the numbers $a_0, a_1, a_2, \ldots, a_h$, find and print the result of:

$$\sum_{i=0}^{h} f(i, a_i)$$

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of nodes in the tree) and $h$ (the height of the tree).	
The second line contains $n-1$ space-separated integers describing the respective values of $p_1, p_2, \ldots, p_{n-1}$, where each $p_i$ is the node ID of node $i$'s parent node. In other words, each $p_i$ defines a directed edge from $p_i$ to $i$.  

The third line contains $h+1$ space-separated integers describing the respective values of $a_0, a_1, \ldots, a_h$.

## Output Format

Print a single integer denoting $\sum_{i=0}^{h} f(i, a_i)$.

## Constraints

- $1 \le n \le 5 \times 10^5$ 

- $0 \le h < n$

- $0 \le p_i < n$

- $0 \le a_i \le n$

- It is guaranteed that the input defines a valid directed tree.

- $h$ is the height of the tree.


**Scoring**

This challenge uses *binary* scoring, so you *must* pass all test cases to earn a positive score.

## Sample Tests

### Test 1

```
5 2
0 0 2 2
0 1 2
```

### Test 2

```
10
```
