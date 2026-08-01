# Tree Coordinates

- **Domain:** c
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.6381644934804414
- **Total Submissions:** 11964
- **Solved Count:** 7635
- **URL:** https://www.hackerrank.com/challenges/tree-coordinates

## Problem Statement

We consider [metric space](https://en.wikipedia.org/wiki/Metric_space) to be a pair, $(M, \rho)$, where $M$ is a set and $\rho: M \times M \rightarrow \mathbb{R}$ such that the following conditions hold:

- $\rho(x, y) \ge 0$
- $\rho(x, y) = 0 \Leftrightarrow x = y$
- $\rho(x, y) = \rho(y, x)$
- $\rho(x, y) \le \rho(x, z) + \rho(z, y)$

where $\rho(x, y)$ is the *distance* between points $x$ and $y$.

Let's define the *product* of two metric spaces, $(M_1, \rho_1) \times (M_2, \rho_2)$, to be $(M, \rho)$ such that:

- $M = M_1 \times M_2$
- $\rho(z_1, z_2) = \rho_1(x_1, x_2) + \rho_2(y_1, y_2)$, where $z_1 = (x_1, y_1)$, $z_2 = (x_2, y_2)$.

So, it follows logically that $(M, \rho)$ is also a metric space. We then define *squared metric space*, $(M, \rho)^2$, to be the product of a metric space multiplied with itself: $(M, \rho) \times (M, \rho)$.

For example, $(\mathbb{R}, abs)$, where $abs(x, y) = |x - y|$ is a metric space. $(\mathbb{R}, abs)^2 = (\mathbb{R}^2, abs_2)$, where $abs_2((x_1, y_1), (x_2, y_2)) = |x_1-x_2|+|y_1-y_2|$.

----

In this challenge, we need a tree-space. You're given a tree, $T = (V, E)$, where $V$ is the set of vertices and $E$ is the set of edges. Let the function $\rho: V \times V \rightarrow \mathbb{Z}$ be the distance between two vertices in tree $T$ (i.e., $\rho(x, y)$ is the number of edges on the path between vertices $x$ and $y$). Note that $(V, \rho)$ is a metric space.

You are given a tree, $T$, with $n$ vertices, as well as $m$ points in $(V, \rho)^2$. Find and print the distance between the two furthest points in this metric space!

## Input Format

The first line contains two space-separated positive integers describing the respective values of $n$ (the number of vertices in $T$) and $m$ (the number of given points).		
Each line $i$ of the $n - 1$ subsequent lines contains two space-separated integers, $u_i$ and $v_i$, describing edge $i$ in $T$.		
Each line $j$ of the $m$ subsequent lines contains two space-separated integers describing the respective values of $x_j$ and $y_j$ for point $j$.

## Output Format

Print a single non-negative integer denoting the maximum distance between two of the given points in metric space $(T, \rho)^2$.

## Constraints

- $1 \le n \le 7.5 \cdot 10^4$
- $2 \le m \le 7.5 \cdot 10^4$
- $1 \le u_i, v_i \le n$
- $1 \le x_j, y_j \le n$

**Scoring**

This challenge uses **binary** scoring, so you *must* pass all test cases to earn a positive score.

## Sample Input

2 2
1 2
1 2
2 1

## Sample Output

2

## Explanation

The distance between points  and  is .
