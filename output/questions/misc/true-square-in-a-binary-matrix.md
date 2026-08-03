# True Square in a Binary Matrix

---

| Field | Value |
|---|---|
| **Slug** | `true-square-in-a-binary-matrix` |
| **Contest** | hourrank-14 |
| **Difficulty** | Advanced |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/true-square-in-a-binary-matrix |

---

## Problem Statement

Consider an $n \times n$ square matrix where each cell contains a binary integer (i.e., a $0$ or $1$). You can perform the following swap operation *at most* one time:

> Choose two *rectangular* submatrices that do not intersect or overlap and *swap* them. Note that both submatrices must have the same exact dimensions and you *cannot* rotate or otherwise change their orientation.

Given an $n \times n$ binary matrix, perform *at most* one swap operation such that the largest $k \times k$ submatrix consisting only of $1$'s has a maximal value of $k$. Then print the value of this maximal $k$ as your answer.

## Input Format

The first line contains a single integer, $n$, denoting the length of the matrix's sides.	
Each line $i$ of the $n$ subsequent lines contains $n$ space-separated binary integers describing the respective values of each cell in row $i$ of the matrix.

## Output Format

Print the value of $k$ for the maximal $k \times k$ submatrix consisting only of $1$'s.

## Constraints

* $1 \le n \le 300$
