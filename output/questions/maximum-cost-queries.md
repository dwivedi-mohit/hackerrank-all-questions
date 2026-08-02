# Super Maximum Cost Queries

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.8538321469955306
- **Total Submissions:** 6041
- **Solved Count:** 5158
- **URL:** https://www.hackerrank.com/challenges/maximum-cost-queries

## Problem Statement

Victoria has a tree, $T$, consisting of $N$ nodes numbered from $1$ to $N$. Each edge from node $U_i$ to $V_i$ in tree $T$ has an integer weight, $W_i$.

Let's define the cost, $C$, of a path from some node $X$ to some other node $Y$ as the maximum weight ($W$) for any edge in the unique path from node $X$ to node $Y$.

Victoria wants your help processing $Q$ queries on tree $T$, where each query contains $2$ integers, $L$ and $R$, such that $L \le R$. For each query, she wants to print the number of different paths in $T$ that have a cost, $C$, in the inclusive range $[L, R]$.

It should be noted that path from some node $X$ to some other node $Y$ is considered same as path from node $Y$ to $X$ i.e $\{X,Y\}$ is same as $\{Y,X\}$. 

## Input Format

The first line contains $2$ space-separated integers, $N$ (the number of nodes) and $Q$ (the number of queries), respectively.	
Each of the $N-1$ subsequent lines contain $3$ space-separated integers, $U$, $V$, and $W$, respectively, describing a bidirectional road between nodes $U$ and $V$ which has weight $W$. 	
The $Q$ subsequent lines each contain $2$ space-separated integers denoting $L$ and $R$.

## Output Format

For each of the $Q$ queries, print the number of paths in $T$ having cost $C$ in the inclusive range $[L, R]$ on a new line.

## Constraints

- $1 \le N,Q \le 10^5$   
- $1 \le U, V \le N$   
- $1 \le W \le 10^9$  
- $1 \le L \le R \le 10^9$ 


**Scoring**

* $1 \le N,Q \le 10^3$ for $30\%$ of the test data.  
* $1 \le N,Q \le 10^5$ for $100\%$ of the test data.


## Sample Input

5 5
1 2 3
1 4 2
2 5 6
3 4 1
1 1
1 2
2 3
2 5
1 6

## Sample Output

3
5
5
10

## Explanation

:

:

:

...etc.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
