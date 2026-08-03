# Clique

---

| Field | Value |
|---|---|
| **Slug** | `clique` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/clique |

---

## Preview

Find the minimum size of the largest clique in a graph.

## Problem Statement

A clique in a graph is set of nodes such that there is an edge between any two distinct nodes in the set. Finding the largest clique in a graph is a computationally difficult problem. Currently no polynomial time algorithm  is known for solving this. However, you wonder what is the minimum size of the largest clique in any graph with $n$ nodes and $m$ edges.


For example, consider a graph with $n=4$ nodes and $m=5$ edges.  The graph below shows $4$ nodes with $4$ edges and no cliques.  It is evident that the addition of any $5^{th}$ edge must create two cliques with $3$ members each.



![image](https://s3.amazonaws.com/hr-assets/0/1526329612-3c9c0f082d-cliqueExample.png)

## Input Format

The first line contains an integer $t$, the number of test cases.


Each of the next $t$ lines contains two space-separated integers $n$ and $m$.

## Output Format

For each test case, print the minimum size of the largest clique that must be formed given $n$ and $m$.

## Constraints

* $1 \le t \le 100000$

* $2 \le n \le 10000$

* $1 \le m \le \frac{n \times (n-1)}{2}$

## Sample Tests

### Test 1

```
3 
3 2 
4 6 
5 7
```

### Test 2

```
2 
4 
3
```
