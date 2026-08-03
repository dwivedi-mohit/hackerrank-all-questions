# Next Topological Ordering

---

| Field | Value |
|---|---|
| **Slug** | `next-topological-sorting` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 50 |
| **Contest** | 101hack40 |
| **URL** | https://www.hackerrank.com/challenges/next-topological-sorting |

---

## Preview

Find the lexicographically next topological sorting.

## Problem Statement

For a [directed acyclic graph][DAG] (DAG), a *topological ordering* is a linear ordering of its vertices such that for every directed edge from vertex $u$ to vertex $v$ (i.e., edge $u \rightarrow v$), $u$ is listed before $v$.

As you may know, a given DAG may have multiple topological orderings. For example, consider the following graph:

![graph](https://s3.amazonaws.com/hr-challenge-images/0/1466936094-7e7ddd7c62-chart.png)

In this diagram, $[1, 2, 3, 5, 4]$ and $[2, 5, 1, 3, 4]$ are two of the possible topological orderings.

A topological ordering $a_1, a_2, \ldots, a_n$ is considered [lexicographically smaller](https://en.wikipedia.org/wiki/Lexicographical_order) than another ordering, $b_1, b_2, \ldots, b_n$, if $a_i < b_i$, for the first index $i$ where $a_i$ and $b_i$ differ.

Given a DAG and a topological ordering, $p$, find the smallest topological ordering that is also *lexicographically greater than* $p$.

**Note:** Each pair of vertices have at most one directed edge between them.


[DAG]: https://en.wikipedia.org/wiki/Directed_acyclic_graph

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of vertices) and $m$ (the number of directed edges) in the DAG.		
Each of the $m$ subsequent lines contains a pair of space-separated integers, $u$ and $v$, describing a directed edge from vertex $u$ (the first value) to vertex $v$ (the second value). 		
The last line contains a permutation of $n$ distinct space-separated positive integers (where each integer is $\in [1,n]$) denoting topological ordering $p$.

## Output Format

Print $n$ space-separated integers denoting the smallest topological ordering that is also lexicographically greater than $p$; if $p$ is already the lexicographically largest topological ordering, print $-1$ instead.

## Constraints

- $1 \le n \le 10^5$ 

- $1 \le m \le 2 \times 10^5$   

- $0 \le m \le \dfrac{n \cdot (n-1)}{2}$  

- $1 \le u, v \le n$

**Subtasks** 


- For $\text{20%}$ of the maximum score, $1 \le n \le 10^3$ and $1 \le m \le 2 \times 10^3$.      

- For additional $\text{20%}$ of the maximum score, $1 \le n \le 10^3$ and $1 \le m \le 2 \times 10^5$.

## Sample Tests

### Test 1

```
5 5
1 3
2 3
3 4
2 5
5 4
1 2 5 3 4
```

### Test 2

```
2 1 3 5 4
```
