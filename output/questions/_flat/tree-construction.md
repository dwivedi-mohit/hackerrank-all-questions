# Tree Construction

---

| Field | Value |
|---|---|
| **Slug** | `tree-construction` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 50 |
| **Contest** | 101hack32 |
| **URL** | https://www.hackerrank.com/challenges/tree-construction |

---

## Preview

Given the degrees of all nodes in a tree, construct a feasible tree.

## Problem Statement

Given the respective *degrees* of all nodes in a tree, construct a feasible tree.

The [degree](https://en.wikipedia.org/wiki/Degree_(graph_theory)) of a node refers to the number of edges connecting to it (in other words, its number of directly-connected neighboring nodes).

## Input Format

The first line contains an integer, $n$, indicating the number of nodes in the tree.

The second line contains $n$ space-separated integers, $degree[1 ... n]$, denoting the [degree](https://en.wikipedia.org/wiki/Degree_(graph_theory)) of each node from $1 ... n$, respectively.

It is guaranteed that **at least one possible tree** exists.

**Constraints**		
For 30% test cases, $2 \le n \le 10$.

For 50% test cases, $2 \le n \le 50$.

For 100% test cases, $2 \le n \le 1000; \forall 1 \le i \le n, 1 \le d[i] \le n - 1; \sum_{i=1}^{n} d[i] = 2 \times (n - 1)$.

## Output Format

Print $n$ lines where the $i^{th}$ line contains the number describing node $n_i$'s *parent node*; if $n_i$ is the *root*, print $0$.

The degree of node $n_i$ *must* be $degree[i]$.

The answer is not unique, and *any feasible tree is acceptable*.

## Sample Tests

### Test 1

```
5
3 2 1 1 1
```

### Test 2

```
2
0
2
1
1
```
