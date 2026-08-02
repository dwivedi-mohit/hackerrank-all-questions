# DAG Queries

- **Domain:** ai
- **Difficulty:** Expert
- **Max Score:** 80
- **Success Ratio:** 0.6205472379969025
- **Total Submissions:** 1937
- **Solved Count:** 1202
- **URL:** https://www.hackerrank.com/challenges/dag-queries

## Problem Statement

You are given a [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (DAG) with $n$ vertices and $m$ edges. Each vertex $v$ has an integer, $a_v$, associated with it and the initial value of $a_v$ is $0$ for all vertices. You must perform $q$ queries on the DAG, where each query is one of the following types:

1. `1 u x`: Set $a_v$ to $x$ for all $v$ such that there is a path in the DAG from $u$ to $v$.
2. `2 u x`: Set $a_v$ to $x$ for all $v$ such that there is a path from $u$ to $v$ and $a_v > x$.
3. `3 u`: Print the value of $a_u$ on a new line.

## Input Format

The first line contains three space-separated integers describing the respective values of $n$ (the number of vertices in the DAG), $m$ (the number of edges in the DAG), and $q$ (the number of queries to perform).	
Each of the $m$ subsequent lines contains two space-separated integers describing the respective values of $u$ and $v$ (where $1 \le u, v \le n$, $u \ne v$) denoting a directed edge from vertex $u$ to vertex $v$ in the graph.		
Each of the $q$ subsequent lines contains a query in one of the three formats described above.


## Output Format

For each query of type $3$ (i.e., `3 u`), print the value of $a_u$ on a new line.

## Constraints

- $2 \le n \le 10^5$
- $1 \le m, q \le 10^5$
- $0 \le x \le 10^9$
- $0 \le a_v \le 10^9$
- It's guaranteed that the graph is acyclic, but there may be more than one edge connecting two nodes.

## Sample Input

6 5 18
1 2
1 3
3 4
2 4
5 6
1 1 3
3 1
3 2
3 3
3 4
1 2 2
3 1
3 2
3 3
3 4
2 6 7
3 5
3 6
2 1 3
3 1
3 2
3 3
3 4

## Sample Output

3
3
3
3
3
2
3
2
0
0
3
2
3
2

## Explanation

The diagram below depicts the changes to the graph after all type  and type  queries:

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
