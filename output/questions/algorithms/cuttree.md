# Cut Tree

---

| Field | Value |
|---|---|
| **Slug** | `cuttree` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/cuttree |

---

## Preview

Given a tree T with n nodes, how many subtrees (T') of T have at most K edges connected to (T - T')

## Problem Statement

Given a tree *T* with *n* nodes, how many subtrees (*T'*) of *T* have at most *K* edges connected to (T - T')?

## Input Format

The first line contains two integers *n* and *K* followed by *n-1* lines each containing two integers a & b denoting that there's an edge between a & b.

## Output Format

A single integer which denotes the number of possible subtrees.

## Constraints

1 <= K <= n <= 50

Every node is indicated by a distinct number from 1 to n.

## Sample Tests

### Test 1

```
3 1
2 1
2 3
```

### Test 2

```
6
```
