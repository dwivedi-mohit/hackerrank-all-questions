# Longest Increasing Subsequence Arrays

---

| Field | Value |
|---|---|
| **Slug** | `longest-increasing-subsequence-arrays` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/longest-increasing-subsequence-arrays |

---

## Preview

Find the number of m-element arrays that have {1, 2, ..., n-1, n} as a subsequence.

## Problem Statement

We define the following:

- A *subsequence* of an array is an ordered subset of the array's elements having the same sequential ordering as the original array. For example, the subsequences of array $[1, 2, 3]$ are $\{1\}$, $\{2\}$, $\{3\}$, $\{1, 2\}$, $\{2, 3\}$, $\{1, 3\}$, and $\{1, 2, 3\}$.
- The [longest increasing subsequence](https://en.wikipedia.org/wiki/Longest_increasing_subsequence) of an array of numbers is the longest possible subsequence that can be created from its elements such that all elements are in increasing order.

Victoria has two integers, $m$ and $n$. She builds unique arrays satisfying the following criteria:

- Each array contains $m$ integers.
- Each integer is $\in [1, n]$.
- The longest increasing subsequence she can create from the array has length $n$.

Given $p$ pairs of $m$ and $n$ values, print the number of arrays Victoria creates for each pair on a new line. As this number can be quite large, print your answer modulo $(10^9+7)$.

## Input Format

The first line contains a single positive integer, $p$, denoting the number of pairs. 		
Each line $i$ of the $p$ subsequent lines contains two space-separated integers describing the respective $m$ and $n$ values for a pair.

## Output Format

On a new line for each pair, print a single integer denoting the number of different arrays Victoria creates modulo $(10^9+7)$.

## Constraints

- $1 \leq p \leq 50$
- $1 \leq m \leq 5 \times 10^5$
- $1 \leq n \leq 10^5$
- $n \leq m$

## Sample Tests

### Test 1

```
2
4 2
4 3
```

### Test 2

```
11
9
```
