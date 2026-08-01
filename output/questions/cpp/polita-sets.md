# Beautiful Sets

- **Domain:** cpp
- **Difficulty:** Hard
- **Max Score:** 75
- **Success Ratio:** 0.7096774193548387
- **Total Submissions:** 124
- **Solved Count:** 88
- **URL:** https://www.hackerrank.com/challenges/polita-sets

## Problem Statement

Consider a set, $S$, consisting of $k$ integers. The set is *beautiful* if *at least one* of the following conditions holds true for every $x \in S$:

1. $x-1 \in S$
2. $x+1 \in S$

For example, $S = \{1, 2, 50, 51\}$ is *beautiful* but $S = \{1, 5, 9\}$ is *not beautiful*. Given two integers, $n$ and $k$, can you find the number of different $k$-element beautiful sets you can create using integers $\in [1, n]$?

Perform $q$ queries where each query $i$ consists of some $n_i$ and $k_i$. For each query:

- Find the number of different beautiful sets having exactly $k$ elements that can be generated using integers in the inclusive range from $1$ to $n$. 
- Print the number of beautiful sets, modulo $10^9+7$, on a new line.

## Input Format

The first line contains an integer, $q$, denoting the number of queries.	
Each line $i$ of the $q$ subsequent lines consists of two space-separated positive integers describing the respective values of $n_i$ and $k_i$ for the query.


## Output Format

For each query, print the number of different beautiful sets of size $k$ that can be generated using integers in the inclusive range from $1$ to $n$ on a new line. As the answers to these queries can be quite large, each answer must be modulo $10^9+7$. 

## Constraints

* $1 \le q \le 10$   
* $1 \le n \le 10^6$ 
* $1 \le k \le n$  

**Subtasks**

* $1 \le n \le 1000$  for $40\%$ of the maximum score.



## Sample Input

6 4
27 2

## Sample Output

26

## Explanation

For the first query, the beautiful sets of size  we can create using numbers from  to  are shown below:

-

-

-

-

-

-

As there are are six such sets, we print the result of  on a new line.
