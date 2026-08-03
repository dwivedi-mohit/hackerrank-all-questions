# Minimum Edges in a Layered Graph

---

| Field | Value |
|---|---|
| **Slug** | `mlp` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 30 |
| **Contest** | 101hack45 |
| **URL** | https://www.hackerrank.com/challenges/mlp |

---

## Preview

Find the minimum number of edges in a graph with k layers.

## Problem Statement

Consider a graph with $n$ vertices split into $k \ge 2$ layers numbered from $0$ through $k-1$. Each layer contains *at least* one vertex, with the exception that the first and the last layers contain exactly one vertex. Some edge $(u, v)$ connecting vertices $u$ and $v$ exists if and only if $u$ is on layer $a$, $v$ is on layer $b$, and $|a-b| = 1$. For example:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1484590408-0704ec56a3-MLP-ps.png)

Given $n$ and $k$, find and print the minimum number of edges in such a graph; if no such graph exists, print `-1` instead.

## Input Format

A single line of two space-separated integers describing the respective values of $n$ (the number of vertices) and $k$ (the number of layers).

## Output Format

Print a single integer denoting the minimum number of edges in such a graph. If no graph satisfies the constraints, print `-1` instead.

## Constraints

- $1 \le n \le 100$
- $2 \le k \le 100$
- Each layer must contain at least one vertex.
- The first and last layers must contain exactly one vertex.

## Sample Tests

### Test 1

```
5 4
```

### Test 2

```
5
```

### Test 3

```
56 57
```

### Test 4

```
-1
```
