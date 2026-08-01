# Coprime Paths

- **Domain:** data-structures
- **Difficulty:** Expert
- **Max Score:** 80
- **Success Ratio:** 0.8149190710767066
- **Total Submissions:** 2842
- **Solved Count:** 2316
- **URL:** https://www.hackerrank.com/challenges/coprime-paths

## Problem Statement

You are given an undirected, connected graph, $G$, with $n$ nodes and $m$ edges where $m = n − 1$. Each node $i$ is initially assigned a value, $node_i$, that has *at most* $3$ prime divisors. 

You must answer $q$ queries in the form `u v`. For each query, find and print the *number of $(x, y)$ pairs* of nodes on the path between $u$ and $v$ such that $gcd(node_x, node_y) = 1$ and the length of the path between $u$ and $v$ is minimal among all paths from $u$ to $v$.

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ and $q$.		
The second line contains $n$ space-separated integers describing the respective values of $node_1, node_2, \ldots, node_{n}$.		
Each of the $n-1$ subsequent lines contains two space-separated integers, $u$ and $v$, describing an edge between nodes $u$ and $v$.		
Each of the $q$ subsequent lines contains two space-separated integers, $u$ and $v$, describing a query.		


## Output Format

For each query, print an integer on a new line denoting the *number of $(x, y)$ pairs* of nodes on the path between $u$ and $v$ such that $gcd(node_x, node_y) = 1$ and the length of the path between $u$ and $v$ is minimal among all paths from $u$ to $v$.

## Constraints

+ $1 \le n, q \le 25 \times 10^3$  
+ $1 \le node_i \le 10^7$  
+ $1 \le u, v \le n$

## Sample Input

6 5
3 2 4 1 6 5
1 2
1 3
2 4
2 5
3 6
4 6
5 6
1 1
1 6
6 1

## Sample Output

9
6
0
3
3

## Explanation

The diagram below depicts graph  and the  paths specified by each query, as well as the Pair Values for each path in the form :

Recall that, for each queried path, we want to find and print the number of  pairs of nodes such that .
