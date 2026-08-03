# Bigger Arrays

---

| Field | Value |
|---|---|
| **Slug** | `bigger-arrays` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 70 |
| **Contest** | 101hack49 |
| **URL** | https://www.hackerrank.com/challenges/bigger-arrays |

---

## Preview

You are given an array. You need to handle some updates and queries on it.

## Problem Statement

If $Y$ and $Z$ are two arrays of the same length, we say that array $Y$ is *bigger* than array $Z$ if $Y_i > Z_i$ for *all* $i$.


![image](https://s3.amazonaws.com/hr-assets/0/1495001840-efd3a9130b-ANewProblemforNick.png)

- In the first example, $Y$ is bigger than $Z$.

- In the second example, $Y$ is *not* bigger than $Z$, since $Y_4$ is not bigger than $Z_4$.

- In the third example, $Y$ is *not* bigger than $Z$, since $Y_3$ is not bigger than $Z_3$.


If $S$ is an array of integers, let $F(S)$ be defined as follows. Consider all possible arrays of integers $X$ with the same length as $S$ and such that $1 \le X_i \le S_i$ for every position $i$. Then $F(S)$ is the maximum number of such arrays you can write such that no array is bigger than any other array in the list. Two arrays $Y$ and $Z$ considered different if there is at least one position $i$ where $Y_i \ne Z_i$.

For example, $F([2, 3]) = 4$, because you can write the following $4$ arrays: $[2, 2]$, $[2, 3]$, $[1, 3]$, $[2, 1]$. Note that no array is bigger than any other array in the list. Also, you can verify that if you write more than $4$ arrays, then there will always be an array that's bigger than some other array in the list. Hence, $F([2, 3]) = 4$.


You are given an array $A = [A_1, A_2, \ldots, A_n]$ with $n$ elements. You need to process $q$ queries. There are two types of queries:

- $1$ $l$ $r$ $x$: Assign each element from positions $l$ to $r$ of array $A$ to $x$, i.e., set $A_i := x$ for $l \le i \le r$.

- $2$ $l$ $r$ : Let array $B$ be the subarray of array $A$ from positions $l$ to $r$. Find $F(B)$ modulo $10^9 + 7$.

## Input Format

The first line contains two space-separated integers $n$ and $q$, the number of elements in the array and the number of queries, respectively.

The next line contains $n$ space-separated integers $A_1, A_2, ..., A_n$ denoting the elements of array $A$.


The next $q$ lines describe the queries. Each query is described by a single line which starts with a number $t$ denoting the query type. Then:

- If $t = 1$, then it is followed by three integers $l$, $r$ and $x$.

- If $t = 2$, then it is followed by two integers $l$ and $r$.

## Output Format

For each query of $\mathrm{type}$ $2$, print a single line containing a single integer denoting the answer for that query modulo $10^9 + 7$.

## Constraints

- $1 \le n, q \le 10^5$

- $1 \le A_i, x \le 10^9$

- $1 \le l \le r \le n$

- $1 \le t \le 2$

## Sample Tests

### Test 1

```
5 4
1 1 3 4 5
1 1 2 2
2 2 3
1 2 5 3
2 1 2
```

### Test 2

```
4
4
```
