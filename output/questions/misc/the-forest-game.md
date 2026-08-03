# The Forest Game

---

| Field | Value |
|---|---|
| **Slug** | `the-forest-game` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 80 |
| **Contest** | 101hack41 |
| **URL** | https://www.hackerrank.com/challenges/the-forest-game |

---

## Preview

Find the minimum total penalty score.

## Problem Statement

Andrea has created new game that she named *The Forest Game*. In this game, you start out with a tree of $n$ vertices rooted at vertex $1$ where each vertex $i$ has some assigned value, $c_i$. Each move is defined as follows:

1. Delete a vertex that is *the root* of some tree. Note that deleting a vertex also deletes its incident edges, and deleting a vertex with child vertices may split the tree into multiple trees. 
2. After each deletion, calculate the *penalty points* for the remaining vertices. The penalty points are equal to $\sum c_i$ for all remaining (non-deleted) vertices in the tree.

A player continues to perform moves until all $n$ vertices are deleted, and then calculate the *total penalty score* as the sum of all *penalty points* calculated after each deletion.

Now it's time to try Andrea's game out for yourself! Given the initial tree, print the minimum *total penalty score* you can achieve.

## Input Format

The first line contains a single integer, $n$, denoting the number of vertices in the initial tree.		
The second line contains $n$ space-separated integers describing $c_1, c_2, \ldots, c_n$, where each $c_i$ denotes the cost for vertex $i$.		
The third line contains $n - 1$ space-separated integers describing the respective parent vertices of each vertex from vertex $2$ to vertex $n$. In other words, the integer corresponding to each $parent_i$ denotes the *parent* of vertex $i + 1$.

## Output Format

Print a single integer denoting the minimum possible *total penalty score*.

## Constraints

- $1 \le n \le 3 \times 10^5$
- $1 \le c_i \le 10^7$
- $1 \le parent_i \le i$

## Sample Tests

### Test 1

```
4
2 1 3 4
1 1 2
```

### Test 2

```
17
```
