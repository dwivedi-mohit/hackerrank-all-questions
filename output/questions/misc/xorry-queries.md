# Xorry Queries

---

| Field | Value |
|---|---|
| **Slug** | `xorry-queries` |
| **Contest** | hourrank-28 |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/xorry-queries |

---

## Problem Statement

<!-- Image suggestion: Illustrate the sample input. For each query, create a table that explicitly computes each P(i). -->

Robin has an array $a = [a_1, a_2, \ldots, a_n]$ consisting of nonnegative integers. He wants to process $m$ queries. There are two types of queries:

- $1$ $i$ $x$. Replace $a_i$ with $a_i \oplus x$. Here, $\oplus$ represents the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR). 
- $2$ $l$ $r$. Find the sum $$\sum_{i=l}^r P(i) = P(l) + P(l + 1) + \ldots + P(r).$$

Here, we define $P(i)$ as follows:

$$P(i) = \begin{cases}
a_i \oplus a_{i+1} \oplus \ldots \oplus a_{i+p-1} & \text{if $i + p - 1 \le n$} \\\
0 & \text{otherwise}
\end{cases}$$

Complete the functions `xorQueries` which takes in an integer array $a$ and two integers $m$ and $p$, and processes $m$ queries, returning the answers to all type-$2$ queries as an array. You need to take the query information from the standard input, as described in the input format section below.

## Input Format

The first line contains three space-separated integers $n$, $m$ and $p$.  

The second line contains $n$ space-separated integers $a_1, a_2, \ldots, a_n$.  

The following $m$ lines describe the queries. The $i^\text{th}$ line describes the $i^\text{th}$ query in the format described in the problem statement, i.e., either $1$ $i$ $x$ or $2$ $l$ $r$.

## Output Format

For each type-$2$ query, print the answer for that query in a single line.

## Constraints

- $1 \le n, m \le 10^5$  
- $1 \le p \le n$  
- $0 \le a_i, x \le 10^5$  
- $1 \le i \le n$  
- $1 \le l \le r \le n$  

**Subtask**  

- For ~24% of the total score, $n, m \le 3000$
