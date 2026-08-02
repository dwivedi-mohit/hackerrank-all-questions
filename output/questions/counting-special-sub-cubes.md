# Counting Special Sub-Cubes

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.836830835117773
- **Total Submissions:** 2335
- **Solved Count:** 1954
- **URL:** https://www.hackerrank.com/challenges/counting-special-sub-cubes

## Problem Statement

Given an $n \times n \times n$ *cube*, let $f(x,y,z)$ (where $1 \le x,y,z \le n$) denote the value stored in cell $(x,y,z)$. 

A $k \times k \times k$ *sub-cube* (where $1 \le k \le n$) of an $n \times n \times n$ cube is considered to be *special* if the maximum value stored in any cell in the sub-cube is equal to $k$.

For each $k$ in the inclusive range $[1, n]$, calculate the number of special sub-cubes. Then print each $count_k$ as a single line of space-separated integers (i.e., $count_1 \ count_2 \ \ldots \ count_n$).

## Input Format

The first line contains an integer, $q$, denoting the number of queries. The $2 \cdot q$ subsequent lines describe each query over two lines:

1. The first line contains an integer, $n$, denoting the side length of the initial cube.
2. The second line contains $n^3$ space-separated integers describing an array of $n^3$ integers in the form $a_0, a_1, \ldots, a_{n^3-1}$. The integer in some cell $(x,y,z)$ is calculated using the formula $a[(x-1) \cdot n^2+(y-1) \cdot n+z]$.


## Output Format

For each query, print $n$ space-separated integers where the $i^{th}$ integer denotes the number of special sub-cubes for $k=i$.

## Constraints

* $1 \le q \le 5$
* $1 \le n \le 50$
* $1 \le f(x,y,z) \le n$ where $1 \le x,y,z \le n$

## Sample Input

2
2 1 1 1 1 1 1 1
2
1 1 1 1 2 1 1 2

## Sample Output

7 1
6 1

## Explanation

We must perform the following  queries:

- We have a cube of size  and must calculate the number of special sub-cubes for the following values of :

- : There are  sub-cubes of size  and seven of them have a maximum value of  written inside them. So, for , the answer is .

- : There is only one sub-cube of size  and the maximum number written inside it is . So, for , the answer is .

We then print the respective values for each  as a single line of space-separated integers (i.e., 7 1).

- We have a cube of size  and must calculate the number of special sub-cubes for the following values of :

- : There are  sub-cubes of size  and six of them have a maximum value of  written inside them. So, for , the answer is .

- : There is only one sub-cube of size  and the maximum number written inside it is . So, for , the answer is .

We then print the respective values for each  as a single line of space-separated integers (i.e., 6 1).

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
