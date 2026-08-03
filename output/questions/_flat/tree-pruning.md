# Tree Pruning

---

| Field | Value |
|---|---|
| **Slug** | `tree-pruning` |
| **Domain** | algorithms |
| **Difficulty** | Advanced |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/tree-pruning |

---

## Preview

Given tree with N nodes, perform at most K removals so that weight of remaining nodes is maximized

## Problem Statement

A tree, $t$, has $n$ vertices numbered from $1$ to $n$ and is rooted at vertex $1$. Each vertex $i$ has an integer weight, $w_i$, associated with it, and $t$'s *total weight* is the sum of the weights of its nodes. A single *remove operation* removes the subtree rooted at some arbitrary vertex $u$ from tree $t$. 

Given $t$, perform up to $k$ remove operations so that the total weight of the remaining vertices in $t$ is maximal. Then print $t$'s maximal total weight on a new line.

**Note:** If $t$'s total weight is already maximal, you may opt to remove $0$ nodes.

## Input Format

The first line contains two space-separated integers, $n$ and $k$, respectively.

The second line contains $n$ space-separated integers describing the respective weights for each node in the tree, where the $i^{th}$ integer is the weight of the $i^{th}$ vertex.		
Each of the $n-1$ subsequent lines contains a pair of space-separated integers, $u$ and $v$, describing an edge connecting vertex $u$ to vertex $v$.

## Output Format

Print a single integer denoting the largest total weight of $t$'s remaining vertices.

## Constraints

- $2 \le n \le 10^5$

- $1 \le k \le 200$

- $1 \le i \le n$
- $-10^9 \le w_i \le 10^9$

## Sample Tests

### Test 1

```
5 2
1 1 -1 -1 -1
1 2
2 3
4 1
4 5
```

### Test 2

```
2
```
