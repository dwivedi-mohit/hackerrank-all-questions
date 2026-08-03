# Manipulative Numbers

---

| Field | Value |
|---|---|
| **Slug** | `manipulative-numbers` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 55 |
| **URL** | https://www.hackerrank.com/challenges/manipulative-numbers |

---

## Preview

Given A, find the largest K such that there exists a
 K-manipulative permutation B.

## Problem Statement

Suppose that $A$ is a list of $n$ numbers $\{A_1, A_2, A_3, \ldots , A_n\}$ and $B = \{B_1, B_2, B_3, .. ,B_n\}$ is a permutation of these numbers, we say B is *K-Manipulative* if and only if:

$M(B) = minimum(B_1 \oplus B_2, B_2 \oplus B_3, B_3 \oplus B_4, \ldots , B_{n-1} \oplus B_n, B_n \oplus B_1 )$ is not less than $2^K$, where $\oplus$ represents the _XOR_ operator.

You are given $A$. Find the largest $K$ such that there exists a _K-manipulative_ permutation $B$.


**Input:**

The first line is an integer $N$. The second line contains $N$ space separated integers - $A_1\ A_2\ \ldots\ A_n$.


**Output:**

The largest possible $K$, or $-1$ if there is no solution.

**Constraints:**


- $1 < n <= 100$ 
- $0 \le A_i \le 10^9, where\ i \in [1, n]$

## Sample Tests

### Test 1

```
3
13 3 10
```

### Test 2

```
2
```

### Test 3

```
4
1 2 3 4
```

### Test 4

```
1
```
