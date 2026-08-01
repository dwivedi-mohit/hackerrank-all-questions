# Vertical Paths

- **Domain:** python
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.9033631332481907
- **Total Submissions:** 2349
- **Solved Count:** 2122
- **URL:** https://www.hackerrank.com/challenges/vertical-paths

## Problem Statement

You have a rooted tree with $n$ vertices numbered from $1$ through $n$ where the root is vertex $1$. 

You are given $m$ triplets, the $j^{th}$ triplet is denoted by three integers $u_{j}, v_{j}, c_{j}$. The $j^{th}$ triplet represents a simple path in the tree with endpoints in $u_i$ and $v_i$ such that $u_j$ is ancestor of $v_j$. The cost of the path is $c_{j}$. 

You have to select a subset of the paths such that the sum of path costs is maximum and the $i^{th}$ edge of the tree belongs to at most $d_i$ paths from the subset. Print the sum as the output.





## Input Format

The first line contains a single integer, $T$, denoting the number of testcases. Each testcase is defined as follows:

* The first line contains two space-separated integers, $n$ (the number of vertices) and $m$ (the number of paths), respectively.
* Each line $i$ of the $n - 1$ subsequent lines contains three space-separated integers describing the respective values of $a_i$, $b_i$, and $d_i$ where ($a_i$, $b_i$) is an edge in the tree and $d_i$ is maximum number of paths which can include this edge.
* Each line of the $m$ subsequent lines contains three space-separated integers describing the respective values of $u_j$, $v_j$, and $c_j$ ($u_j \ne v_j$) that define the $j^{th}$ path and its cost.

## Output Format

You must print $T$ lines, where each line contains a single integer denoting the answer for the corresponding testcase.

## Constraints

- Let $M$ be the sum of $m$ over all the trees. 
- Let $D$ be the sum of $n \times m$ over all the trees.
- $1 \le T \le 10^3$  
- $1 \le M, m \le 10^3$  
- $1 \le D, n \le 5 \times 10^5$  
- $1 \le c_i \le 10^9$  
- $1 \le d_j \le m$

## Sample Input

8 8
1 2 3
1 3 1
2 4 5
2 5 1
2 6 1
3 7 2
4 8 1
1 2 3
2 8 5
1 8 7
1 5 8
1 6 10
3 7 5
1 7 6
1 7 6

## Explanation

One of the possible subsets contains paths . Its total cost is .
