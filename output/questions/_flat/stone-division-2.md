#  Stone Division, Revisited

---

| Field | Value |
|---|---|
| **Slug** | `stone-division-2` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/stone-division-2 |

---

## Preview

Find the maximum number of moves you can perform.

## Problem Statement

You have a pile of $n$ stones that you want to split into multiple piles, as well as a set, $S$, of $m$ distinct integers. We define a *move* as follows:

- First, choose a pile of stones. Let's say that the chosen pile contains $y$ stones. 
- Next, look for some $x \in S$ such that $x \ne y$ and $y$ is divisible by $x$ (i.e., $x$ is a factor of $y$); if such an $x$ exists, you can split the pile into $\frac{y}{x}$ equal smaller piles.

You are given $q$ queries where each query consists of $n$ and $S$. For each query, calculate the maximum possible number of moves you can perform and print it on a new line.

## Input Format

The first line contains an integer, $q$, denoting the number of queries. The $2 \cdot q$ subsequent lines describe each query in the following format:

1. The first line contains two space-separated integers describing the respective values of $n$ (the size of the initial pile in the query) and $m$ (the size of the set in the query).
2. The second line contains $m$ distinct space-separated integers describing the values in set $S$.

## Output Format

For each query, calculate the maximum possible number of moves you can perform and print it on a new line.

## Constraints

* $ 1\le q \le 10 $
* $1 \le n \le 10^{12}$
* $1 \le m \le 1000$
* $1 \le s_i \le 10^{12}$ 

**Subtask**

* $1 \le m \le 10$ for $30\%$ of the maximum score.

## Sample Tests

### Test 1

```
1
12 3
2 3 4
```

### Test 2

```
4
```
