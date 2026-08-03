# Project Euler #18: Maximum path sum I

---

| Field | Value |
|---|---|
| **Slug** | `euler018` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 100 |
| **Contest** | projecteuler |
| **URL** | https://www.hackerrank.com/challenges/euler018 |

---

## Preview

Find path with largest sum in a pyramid.

## Problem Statement

<sub>This problem is a programming version of [Problem 18](https://projecteuler.net/problem=18) from [projecteuler.net](https://projecteuler.net/)</sub>

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is $23$. The path is denoted by numbers in bold. 


$~~~~~~\textbf{3}$

$~~~~\textbf{7}~~4$

$~~2~~\textbf{4}~~6$

$8~~5~~\textbf{9}~~3$ 


That is, $3 + 7 + 4 + 9 = 23$.

Find the maximum total from top to bottom of the triangle given in input.

## Input Format

First line contains $T$, the number of testcases. For each testcase: 

First line contains $N$, the number of rows in the triangle.  

For next $N$ lines, $i$'th line contains $i$ numbers.

## Output Format

For each testcase, print the required answer in a newline.

## Constraints

+ $1 \leqslant T \leqslant 10$ 

+ $1 \leqslant N \leqslant 15$ 

+ $numbers \in [0,100)$

## Sample Tests

### Test 1

```
1
4
3
7 4
2 4 6
8 5 9 3
```

### Test 2

```
23
```
