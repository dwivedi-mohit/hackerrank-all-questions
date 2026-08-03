# Longest Palindromic Subsequence

---

| Field | Value |
|---|---|
| **Slug** | `longest-palindromic-subsequence` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/longest-palindromic-subsequence |

---

## Preview

Insert characters in a string so that length longest palindromic subsequence increases by at least K.

## Problem Statement

Steve loves playing with palindromes. He has a string, $s$, consisting of $n$ lowercase English alphabetic characters (i.e., `a` through `z`). He wants to calculate the number of ways to insert exactly $1$ lowercase character into string $s$ such that the length of the [longest palindromic subsequence](http://www.geeksforgeeks.org/dynamic-programming-set-12-longest-palindromic-subsequence/) of $s$ increases by *at least* $k$. Two ways are considered to be *different* if either of the following conditions are satisfied:

- The positions of insertion are different.
- The inserted characters are different. 

This means there are *at most* $26 \times (n+1)$ different ways to insert exactly $1$ character into a string of length $n$.

Given $q$ queries consisting of $n$, $k$, and $s$, print the number of different ways of inserting exactly $1$ new lowercase letter into string $s$ such that the length of the longest palindromic subsequence of $s$ increases by *at least* $k$.

## Input Format

The first line contains a single integer, $q$, denoting the number of queries. The $2q$ subsequent lines describe each query over two lines:

1. The first line of a query contains two space-separated integers denoting the respective values of $n$ and $k$. 	
2. The second line contains a single string denoting $s$.

## Output Format

On a new line for each query, print the number of ways to insert exactly $1$ new lowercase letter into string $s$ such that the length of the longest palindromic subsequence of $s$ increases by *at least* $k$.

## Constraints

* $1 \le q \le 10$
* $1 \le n \le 3000$
* $0 \le k \le 50$
* It is guaranteed that $s$ consists of lowercase English alphabetic letters (i.e., `a` to `z`) only.

**Subtasks**

* $1 \le n \le 100$ for $\text{25%}$ of the maximum score.
* $1 \le n \le 1000$ for $\text{70%}$ of the maximum score.

## Sample Tests

### Test 1

```
3
1 1
a
3 2
aab
3 0
aba
```

### Test 2

```
2
1
104
```
