# Birthday Triplets

- **Domain:** regex
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.5707317073170731
- **Total Submissions:** 205
- **Solved Count:** 117
- **URL:** https://www.hackerrank.com/challenges/the-triplets

## Problem Statement

Julia received a really simple function, $f$, for her birthday! The function is defined as:
$$f_{n} = a^{n} + b^{n} + c^{n}$$ 
Here, $a$, $b$, $c$, and $n$ are positive integers and $a \lt b \lt c$. Unfortunately, she forgot the values of $a$, $b$, and $c$; however, she *does* remember the values of $f_{2}$, $f_{3}$, and $f_{4}$!

Julia wants your help finding the triplet $\left(a,\ b,\ c\right)$ so she can calculate the value of $f_{n}$. If there is more than one such triplet, then she always chooses the one with the smallest value of $a$; if there are still many such triplets, then she chooses the one with the smallest value of $b$.  

----

You are given $q$ queries, where each query consists of $f_{2}$, $f_{3}$, $f_{4}$, $l$, and $r$. For each query, find the value of $S \bmod \left(10^{9} + 7\right)$ and print it on a new line, where $S$ is defined as:   
$$S = \sum_{n = l}^{r}f_{n}$$

**Note:** It is guaranteed that the triplet $\left(a,\ b,\ c\right)$ always exists for the given values of $f_{2}$, $f_{3}$, and $f_{4}$.

## Input Format

The first line of the input contains an integer, $q$, denoting the number of queries.	
Each of the $q$ subsequent lines contains five space-separated integers describing the respective values of $f_{2}$, $f_{3}$, $f_{4}$, $l$, and $r$ for a query.

## Output Format

For each query, print the value of $S \bmod \left(10^{9} + 7\right)$ on a new line.

## Constraints

- $1 \le q \le 2500$
- $6 \le f_{1}\le 15 \times 10^{3}$
- $1 \le l \le r \le 10^{15}$

## Sample Input

4
14 36 98 5 6
49 251 1393 7 10
14 36 98 6 9
49 251 1393 8 8

## Sample Output

1070
72592824
30124
1686433

## Explanation

The breakdown below describes the first and last queries:

- , , , , and

For this query, the triplet is .
From this, we calculate:

We then print the value of  on a new line.

- , , , , and

For this query, the triplet is .
From this, we calculate:

We then print the value of  on a new line.
