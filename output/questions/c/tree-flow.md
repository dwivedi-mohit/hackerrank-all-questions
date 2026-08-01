# Tree Flow

- **Domain:** c
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.7315270935960592
- **Total Submissions:** 2030
- **Solved Count:** 1485
- **URL:** https://www.hackerrank.com/challenges/tree-flow

## Problem Statement

Recall that a tree is an undirected, connected acyclic graph. We have a weighted tree, $T$, with $n$ vertices; let $dist_{u, v}$ be the total sum of edge weights on the path between nodes $u$ and $v$.

Let's consider all the matrices, $A_{u, v}$, such that:

- $A_{u, v} = -A_{v, u}$
- $0 \le |A_{u, v}| \le dist_{u, v}$
- $\sum_{i=1}^n A_{u, i} = 0$ for each $u \ne 1$ and $u \ne n$

We consider the *total value* of matrix $A$ to be:
$$\sum_{i=1}^n A_{1, i}$$

Calculate and print the maximum total value of $A$ for a given tree, $T$.

## Input Format

The first line contains a single positive integer, $n$, denoting the number of vertices in tree $T$. 		
Each line $i$ of the $n - 1$ subsequent lines contains three space-separated positive integers denoting the respective $a_i$, $b_i$, and $c_i$ values defining an edge connecting nodes $a_i$ and $b_i$ (where $1 \le a_i, b_i \le n$) with edge weight $c_i$.

## Output Format

Print a single integer denoting the maximum total value of matrix $A$ satisfying the properties specified in the *Problem Statement* above.

## Constraints

- $2 \le n \le 500000$
- $1 \le c_i \le 10^4$
- Test cases with $n \le 10$ have $30\%$ of total score
- Test cases with $n \le 500$ have $60\%$ of total score 

## Sample Input

1 2 2
1 3 1

## Explanation

In the sample case, matrix  is:

The sum of the elements of the first row is equal to .
