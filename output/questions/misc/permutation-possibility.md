# Permutation Possibility

---

| Field | Value |
|---|---|
| **Slug** | `permutation-possibility` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 15 |
| **Contest** | 101hack47 |
| **URL** | https://www.hackerrank.com/challenges/permutation-possibility |

---

## Preview

Determine if numbers can be added to a sequence to make it some permutation of the distinct sequence of integers from 1 to some 'n'.

## Problem Statement

A [permutation](https://en.wikipedia.org/wiki/Permutation) of a sequence, $S = \{s_0, s_1, \ldots, s_{m-1}\}$, is a sequence consisting of some rearrangement of the $m$ elements of $S$. For example, all the permutations of $S = \{1, 2, 3\}$ are  $\{1, 2, 3\}$,  $\{1, 3, 2\}$, $\{2, 1, 3\}$, $\{2, 3, 1\}$, $\{3, 1, 2\}$, and $\{3, 2, 1\}$.

Mark writes sequence $S$ on a piece of paper and asks Lisa to insert zero or more integers *anywhere* in the sequence so that it becomes a permutation of $\{1, 2, \ldots, n\}$ (i.e., a sequence of distinct integers from $1$ to $n$) for any integer $n$. 

Given $S$, print `YES` if Lisa's task is possible; otherwise, print `NO` instead.

## Input Format

The first line contains a single integer denoting $m$.

The second line contains $m$ space-separated integers describing the respective values of $s_0, s_1, \ldots, s_{m-1}$.

## Output Format

If Lisa can insert integers into the sequence to make it a permutation of $\{1, 2, \ldots, n\}$ for any $n$, print `YES`; otherwise, print `NO` instead.

## Constraints

- $1 \le m \le 100$ 

- $1 \le s_i \le 10^5$

## Sample Tests

### Test 1

```
3
1 2 3
```

### Test 2

```
YES
```

### Test 3

```
3
2 2 1
```

### Test 4

```
NO
```

### Test 5

```
3
4 1 6
```

### Test 6

```
YES
```
