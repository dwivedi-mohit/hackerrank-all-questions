# Tripartite Matching

---

| Field | Value |
|---|---|
| **Slug** | `tripartite-matching` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/tripartite-matching |

---

## Preview

Given three graphs, find number of $(a, b, c)$ triples such that there is an edge $(a, b)$ in $G_1$, an edge $(b, c)$ in $G_2$, and an edge $(c, a)$ in $G_3$.

## Problem Statement

You are given $3$ unweighted, undirected graphs, $G_1$, $G_2$, and $G_3$, with $n$ vertices each, where the $k^{th}$ graph has $m_k$ edges and the vertices in each graph are numbered from $1$ through $n$. Find the number of ordered triples $(a, b, c)$, where $1 \le a, b, c \le n$, $a \ne b, b \ne c, c \ne a$, such that there is an edge $(a, b)$ in $G_1$, an edge $(b, c)$ in $G_2$, and an edge $(c, a)$ in $G_3$.

## Input Format

The first line contains single integer, $n$, denoting the number of vertices in the graphs. The subsequent lines define $G_1$, $G_2$, and $G_3$. Each graph is defined as follows:

1. The first line contains an integer, $m$, describing the number of edges in the graph being defined.
2. Each line $i$ of the $m$ subsequent lines (where $1 \le i \le m$) contains $2$ space-separated integers describing the respective nodes, $u_i$ and $v_i$ connected by edge $i$.

## Output Format

Print a single integer denoting the number of distinct $(a, b, c)$ triples as described in the *Problem Statement* above.

## Constraints

- $n \leq 10^5$
- $m_k \leq 10^5$, and $k \in \{1, 2, 3\}$
- Each graph contains no cycles and any pair of directly connected nodes is connected by a maximum of $1$ edge.

## Sample Tests

### Test 1

```
3
2
1 2
2 3
3
1 2
1 3
2 3
2
1 3
2 3
```

### Test 2

```
3
```
