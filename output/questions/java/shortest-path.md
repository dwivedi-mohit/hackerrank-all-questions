# Find the Path

- **Domain:** java
- **Difficulty:** Hard
- **Max Score:** 75
- **Success Ratio:** 0.6408934707903781
- **Total Submissions:** 2328
- **Solved Count:** 1492
- **URL:** https://www.hackerrank.com/challenges/shortest-path

## Problem Statement

You are given a table, $a$, with $n$ rows and $m$ columns. The top-left corner of the table has coordinates $(0,0)$, and the bottom-right corner has coordinates $(n-1, m-1)$. The $i^{th}$ cell contains integer $a_{i,j}$.

A path in the table is a sequence of cells $(r_1,c_1), (r_2,c_2), \ldots, (r_k,c_k)$ such that for each $i \in \{1,\ldots,k-1\}$, cell $(r_i,c_i)$ and cell $(r_{i+1},c_{i+1})$ share a side. 

The weight of the path $(r_1,c_1), (r_2,c_2), \ldots, (r_k,c_k)$ is defined by $\sum_{i=1}^{k} a_{r_{i},c_{i}}$ where $a_{r_{i},c_{i}}$ is the weight of the cell $(r_{i},c_{i})$.

You must answer $q$ queries. In each query, you are given the coordinates of two cells, $(r_1,c_1)$ and $(r_2,c_2)$. You must find and print the minimum possible weight of a path connecting them.

**Note:** A cell can share sides with at most $4$ other cells. A cell with coordinates $(r,c)$ shares sides with $(r-1, c)$, $(r+1, c)$, $(r, c-1)$ and $(r, c+1)$.

## Input Format

The first line contains $2$ space-separated integers, $n$ (the number of rows in $a$) and $m$ (the number of columns in $a$), respectively.		
Each of $n$ subsequent lines contains $m$ space-separated integers. The $j^{th}$ integer in the $i^{th}$ line denotes the value of $a_{i,j}$. 	
The next line contains a single integer, $q$, denoting the number of queries. 		
Each of the $q$ subsequent lines describes a query in the form of $4$ space-separated integers: $r_1$, $c_1$, $r_2$, and $c_2$, respectively. 

## Output Format

On a new line for each query, print a single integer denoting the minimum possible weight of a path between $(r_1,c_1)$ and $(r_2,c_2)$.

## Constraints

* $1 \le n \le 7$
* $1 \le m \le 5 \times 10^3$
* $0 \le a_{i,j} \le 3 \times 10^3$
* $1 \le q \le 3 \times 10^4$

For each query:

* $0 \le r_1,r_2 < n$
* $0 \le c_1,c_2 < m$

## Sample Input

3 5
0 0 0 0 0
1 9 9 9 1
0 0 0 0 0
3
0 0 2 4
0 3 2 3
1 1 1 3

## Sample Output

1
18

## Explanation

The input table looks like this:

The first two queries are explained below:

- In the first query, we have to find the minimum possible weight of a path connecting  and . Here is one possible path:

The total weight of the path is .

- In the second query, we have to find the minimum possible weight of a path connecting  and . Here is one possible path:

The total weight of the path is .
