# Diagonal Filling

---

| Field | Value |
|---|---|
| **Slug** | `diagonal-filling` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 75 |
| **Contest** | 101hack53 |
| **URL** | https://www.hackerrank.com/challenges/diagonal-filling |

---

## Preview

Answer queries on a diagonally-filled grid.

## Problem Statement

Kaye has a rectangular board of dimensions $n \times m$, where $n$ and $m$ are [coprime](https://en.wikipedia.org/wiki/Coprime_integers). The rows are numbered $1$ to $n$, and the columns are numbered $1$ to $m$. The cell at the $i^\text{th}$ row and $j^\text{th}$ column is identified as $(i, j)$.


Her friend Jay starts filling the board in a unique way. First, he chooses some starting cell $(r, c)$ and starts filling the numbers in increasing order, i.e., $1, 2, 3, \ldots, nm$, such that he always moves *down-right* of the current cell. If he is in the last row, he moves to the first row, and if he is in the last column, he moves to the first column. 

![image](https://s3.amazonaws.com/hr-assets/0/1492938153-98fa08a97b-final1.png)

For example, in this figure, if he is in cell $(5, 6)$, then he moves next to $(1, 7)$ and then to $(2, 1)$.

Jay has finished filling the board and wants to answer $q$ queries. But he is tired, so he asks Kaye to answer them for him.

There are two types of queries. Each query will deal with a submatrix with top-left corner at $(r_1, c_1)$ and bottom-right corner at $(r_2, c_2)$.

- *Type 1*: What is the sum of the numbers in that submatrix modulo $nm$?

- *Type 2*: How many numbers in that submatrix are coprime with $nm$?

Complete the functions `initialize` and `query`. `initialize` takes in five integers $n$, $m$, $r$, $c$ and $q$ and lets you prepare for the upcoming queries, while `query` takes in five integers $\mathrm{type}$, $r_1$, $c_1$, $r_2$, $c_2$ and returns the answer for that query.

## Input Format

The first line contains a single integer $t$ denoting the number of test cases. The description of $t$ test cases follows.

The first line of each test case contains five space-separated integers $n, m, r, c$ and $q$. The meanings of these numbers are described in the problem statement. 

The next $q$ lines describe the queries. The $i^\text{th}$ line contains five space-separated integers $\mathrm{type}$, $r_1$, $c_1$, $r_2$, $c_2$ where $\mathrm{type}$ is either $1$ or $2$, depending on the query type.

## Output Format

For each query, print a line containing a single integer denoting the answer for that query.

## Constraints

- $1 \le t \le 20$
- $1 \le n, m \le 10^9$
- $n$ and $m$ are coprime
- $1 \le r, r_1, r_2 \le n$
- $1 \le c, c_1, c_2 \le m$
- $r_1 \le r_2$
- $c_1 \le c_2$
- $1 \le q \le 5 \cdot 10^3$

**Subtasks**

- $1 \le n, m \le 10^3$ for $20\%$ of the maximum score.
- $1 \le n, m \le 10^6$ for $50\%$ of the maximum score.

## Sample Tests

### Test 1

```
1
5 7 3 4 4
1 2 3 4 5
2 2 3 4 5
1 3 5 5 7
2 3 5 5 7
```

### Test 2

```
9
4
13
9
```
