# Lucky Numbers 

---

| Field | Value |
|---|---|
| **Slug** | `leonardo-and-lucky-numbers` |
| **Contest** | hourrank-16 |
| **Difficulty** | Easy |
| **Score** | 25 |
| **URL** | https://www.hackerrank.com/challenges/leonardo-and-lucky-numbers |

---

## Problem Statement

Leonardo thinks $4$ and $7$ are *lucky* digits! He defines a number as *lucky* if it can be represented as the sum of one or more of these lucky digits. For example, he considers the following numbers to be lucky:

* $14 \Leftarrow 7 + 7$
* $11 \Leftarrow 7 + 4$
* $18 \Leftarrow 7 + 7 + 4$
* $7 \Leftarrow 7$

You are given $q$ queries, where each query consists of a long integer denoting $n$. For each query, print ``Yes`` on a new line if $n$ is a lucky number; otherwise, print ``No``.

## Input Format

The first line contains an integer denoting $q$. 		
Each of the $q$ subsequent lines contains a long integer describing the value of $n$ for a query.

## Output Format

For each query, print ``Yes`` on a new line if $n$ is a lucky number; otherwise, print ``No``.

## Constraints

* $1 \le q \le 100$  
* $1 \le n \le 10^{16}$ 

**Subtasks**

* $1 \le n \le 100$ for $60\%$ of the maximum score
