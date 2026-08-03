# Almost Equal Rows

---

| Field | Value |
|---|---|
| **Slug** | `almost-equal-rows` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 65 |
| **Contest** | 101hack48 |
| **URL** | https://www.hackerrank.com/challenges/almost-equal-rows |

---

## Preview

Find the number of 'almost equal' pairs of rows in a graph's shortest path matrix.

## Problem Statement

Alexa loves studying the properties of graphs! Recently, she took an undirected connected graph, $G$, and calculated a matrix named $dist$, where $dist[i][j]$ denotes the *minimum* distance from vertex $i$ to vertex $j$. She then looked for equal rows in the matrix, but found that $dist[i] \ne dist[j]$ for $i \ne j$ since $dist[i][i] = 0$ but $dist[j][i] \ne 0$.

Alexa solved this problem by saying that for an $(i, j)$ pair (where $1 \le i < j \le n$), row $i$ *almost equals* row $j$ if $dist[i][x] = dist[j][x]$ for all $x$ such that $1 \le x \le n$, $x \ne i$, and $x \ne j$. In other words, row $i$ almost equals row $j$ if they're equal if we ignore their entries at columns $i$ and $j$. 


For example, suppose $dist$ is the following $6\times 6$ matrix:


<!-- https://s3.amazonaws.com/hr-assets/0/1492872650-5db7bb4f36-almostequal.jpg -->

![Example dist matrix](https://s3.amazonaws.com/hr-assets/0/1492872807-f90230dd3b-almostequal2.jpg "Example dist matrix")

The first table shows that row $3$ is almost equal to row $5$, since they are equal except for their entries at columns $3$ and $5$. On the other hand, the second table shows that row $2$ is *not* almost equal to row $5$ because they're not equal even if you ignore columns $2$ and $5$, since their entries at column $3$ are not equal.


Given $G$, print the total number of $(i, j)$ pairs (where $1 \le i < j \le n$) such that row $i$ *almost equals* row $j$.

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of vertices in $G$) and $m$ (the number of edges in $G$).  		
Each line $i$ of the $m$ subsequent lines contains two space-separated integers, $a_i$ and $b_i$, describing an undirected edge connecting vertices $a_i$ and $b_i$.

## Output Format

Print an integer denoting the number of $(i, j)$ pairs (where $1 \le i < j \le n$) such that row $i$ *almost equals* row $j$.

## Constraints

- $G$ is an undirected, connected graph.

- $1 \le n, m \le 3 \times 10^5$
- $1 \le a_i, b_i \le n$

- $a_i \ne b_i$

## Sample Tests

### Test 1

```
4 4
1 2
2 3
3 4
1 4
```

### Test 2

```
2
```
