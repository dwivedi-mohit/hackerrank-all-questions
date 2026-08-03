# Tara's Beautiful Permutations

---

| Field | Value |
|---|---|
| **Slug** | `taras-beautiful-permutations` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/taras-beautiful-permutations |

---

## Preview

Count the number of good permutations.

## Problem Statement

Tara has an array, $A$, consisting of $n$ integers where each integer occurs *at most* $2$ times in the array. 

Let's define $P$ to be a permutation of $A$ where $p_i$ is the $i^{th}$ element of permutation $P$. Tara thinks a permutation is *beautiful* if there is no index $i$ such that $p_i - p_{i+1} = 0$ where $i \in [0, n-1)$.

You are given $q$ queries where each query consists of some array $A$. For each $A$, help Tara count the number of possible beautiful permutations of the $n$ integers in $A$ and print the count, modulo $10^9 + 7$, on a new line.

**Note:** Two permutations, $P$ and $Q$, are considered to be *different* if and only if there exists an index $i$ such that $p_i \neq q_i$ and $i \in [0, n)$.

## Input Format

The first line contains a single integer, $q$, denoting the number of queries. The $2 \cdot q$ subsequent lines describe each query in the following form:

1. The first line contains an integer, $n$, denoting the number of elements in array $A$. 
2. The second line contains $n$ space-separated integers describing the respective values of $a_0, a_1, \ldots, a_{n-1}$ in array $A$.

## Output Format

For each query, print the the number of possible beautiful permutations, modulo $10^9+7$, on a new line.

## Constraints

* $1 \le a_i \le 10^9$
* Each integer in $A$ can occur at most $2$ times.

For $40 \%$ of the maximum score:

* $1 \le q \le 100$  

* $1 \le n \le 1000$

* The sum of $n$ over all queries does not exceed $10^4$.


For $100 \%$ of the maximum score:


* $1 \le q \le 100$  

* $1 \le n \le 2000$

## Sample Tests

### Test 1

```
3
3
1 1 2
2
1 2
4
1 2 2 1
```

### Test 2

```
1
2
2
```
