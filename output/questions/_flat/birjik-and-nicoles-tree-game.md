# Birjik and Nicole's Tree Game

---

| Field | Value |
|---|---|
| **Slug** | `birjik-and-nicoles-tree-game` |
| **Contest** | hourrank-20 |
| **Difficulty** | Expert |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/birjik-and-nicoles-tree-game |

---

## Problem Statement

Nicole and Birjik are seniors taking a break from job applications by creating the following game:

- Birjik draws a *rooted tree* with $n$ vertices numbered from $1$ to $n$, rooted at vertex $1$. 
- Nicole creates $q$ queries. For each query, she takes a copy of the tree and colors $k$ of its vertices *black*, leaving the remaining $n - k$ vertices *white*.
- The goal of the game is to answer each query by finding the respective values of $c_0, c_1, c_2, \ldots, c_k$, where each $c_i$ is the number of subtrees containing exactly $i$ *black* vertices (including the subtree's root vertex). 
    
For example, the diagram below depicts a query on a tree where $k = 3$ and the *black* vertices are $2$, $5$, and $4$:

![image](https://s3.amazonaws.com/hr-assets/0/1493321015-55bccf0522-Birjik-and-Nicoles-Tree-Game-PS.png)

Given the tree and $q$ queries, solve each query by printing the values of $c_0, c_1, c_2, \ldots, c_k$ on a new line.

## Input Format

The first line contains an integer, $n$, denoting the number of vertices of the tree.	
Each of the $n - 1$ subsequent lines contains two space-separated integers, $u$ and $v$, describing an edge connecting vertices $u$ and $v$.	
The next line contains an integer, $q$, denoting the number of queries. The $2 \cdot q$ subsequent lines describe each query over two lines:

1. The first line contains an integer denoting $k$.
2. The second line contains $k$ space-separated integers describing the respective IDs of the vertices to color *black*.

## Output Format

For each query, print a single line containing $k + 1$ integers describing the respective values of $c_0, c_1, \ldots, c_k$. Recall that each $c_i$ is the total number of subtrees containing exactly $i$ *black* vertices.

## Constraints

- $1 \le n, q, k \le 3 \times 10^5$  
- $1 \le u, v, k \le n$  
- It is guaranteed that the given graph is a tree.  
- It is guaranteed that the $k$ vertex IDs given in each query are distinct IDs that exist in the tree.
- The sum of $k$ over all queries in a test case is $\le 3 \times 10^5$
