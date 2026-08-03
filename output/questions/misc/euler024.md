# Project Euler #24: Lexicographic permutations

---

| Field | Value |
|---|---|
| **Slug** | `euler024` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 100 |
| **Contest** | projecteuler |
| **URL** | https://www.hackerrank.com/challenges/euler024 |

---

## Preview

We finally get to some permutations.

## Problem Statement

<sub>This problem is a programming version of [Problem 24](https://projecteuler.net/problem=24) from [projecteuler.net](https://projecteuler.net/)</sub>


A permutation is an ordered arrangement of objects. For example, $dabc$ is one possible permutation of the word $abcd$. If all of the permutations are listed alphabetically, we call it lexicographic order. The lexicographic permutations of $abc$ are:

 $$\text{abc   acb   bac   bca   cab   cba}$$
 
What is the $N^{th}$ lexicographic permutation of the word $abcdefghijklm$?

## Input Format

The first line contains an integer $T$ , i.e., number of test cases.

Next $T$ lines will contain an integer $N$.

## Output Format

Print the values corresponding to each test case.

## Constraints

$1 \le T \le 1000$

$1 \le N \le 13!$

## Sample Tests

### Test 1

```
2
1
2
```

### Test 2

```
abcdefghijklm
abcdefghijkml
```
