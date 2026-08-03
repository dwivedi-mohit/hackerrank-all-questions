# Largest Pyramid

---

| Field | Value |
|---|---|
| **Slug** | `largest-pyramid` |
| **Contest** | hourrank-23 |
| **Difficulty** | Medium |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/largest-pyramid |

---

## Problem Statement

You are given a rectangular field whose dimensions are $n \times m$. The field is split into $nm$ different $1\times 1$ cells. The cell on the $i^{th}$ row and $j^{th}$ column has a constant height of $h_{i,j}$.  

Now, you wish to build a *pyramid* somewhere in the field. Formally, a pyramid of size $s$ is a $(2s-1)\times (2s-1)$ square where the cell at the $i^{th}$ row and $j^{th}$ column has a constant height of $\min(i, j, 2s-i, 2s-j)$. For example, here are pyramids of sizes from $1$ to $4$:  

$$
\begin{bmatrix} 
1
\end{bmatrix}
\quad
\begin{bmatrix} 
1 & 1 & 1  \\\
1 & 2 & 1  \\\
1 & 1 & 1
\end{bmatrix}
\quad
\begin{bmatrix} 
1 & 1 & 1 & 1 & 1  \\\
1 & 2 & 2 & 2 & 1  \\\
1 & 2 & 3 & 2 & 1  \\\
1 & 2 & 2 & 2 & 1  \\\
1 & 1 & 1 & 1 & 1 
\end{bmatrix}
\quad
\begin{bmatrix} 
1 & 1 & 1 & 1 & 1 & 1 & 1 \\\
1 & 2 & 2 & 2 & 2 & 2 & 1 \\\
1 & 2 & 3 & 3 & 3 & 2 & 1 \\\
1 & 2 & 3 & 4 & 3 & 2 & 1 \\\
1 & 2 & 3 & 3 & 3 & 2 & 1 \\\
1 & 2 & 2 & 2 & 2 & 2 & 1 \\\
1 & 1 & 1 & 1 & 1 & 1 & 1
\end{bmatrix}
$$

To build a pyramid, you have $k$ blocks whose dimensions are $1\times 1\times 1$. You can increase the height of any cell by $1$ by placing a single block on that cell. However, you can't reduce the height of any cell. You also can't change the height of any region outside the field.  

What is the largest pyramid that you can form? Note that you don't have to use all of the blocks.

## Input Format

The first line of input contains a single integer $q$ denoting the number of queries.  
The first line of each query contains three space-separated integers $n$, $m$ and $k$.  
The next $n$ lines describe the field. The $j^{th}$ number in the $i^{th}$ line represents $h_{i,j}$.

## Output Format

For each query, print a single line containing a single integer denoting the size of the maximum pyramid you can build. If it's impossible to build any pyramid, print $0$.

## Constraints

- $1 \le q \le 5$  
- $1 \le n,m \le 350$  
- $1 \le k \le 10^9$  
- $0 \le h_{i,j} \le 200$  

**Subtasks**  

- For $40\%$ of the maximum points, $1 \le n,m \le 30$
