# Project Euler #22: Names scores

---

| Field | Value |
|---|---|
| **Slug** | `euler022` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 100 |
| **Contest** | projecteuler |
| **URL** | https://www.hackerrank.com/challenges/euler022 |

---

## Preview

A score for every name.

## Problem Statement

<sub>This problem is a programming version of [Problem 22](https://projecteuler.net/problem=22) from [projecteuler.net](https://projecteuler.net/)</sub>


You are given around five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score. 


For example, when the list in sample is sorted into alphabetical order, `PAMELA`, which is worth $16 + 1 + 13 + 5 + 12 + 1 = 48$, is the $5^{th}$ name in the list. So, `PAMELA` would obtain a score of $5 \times 48 = 240$.

You are given $Q$ queries, each query is a name, you have to print the score.

## Input Format

The first line contains an integer $N$, i.e., number of names.

Next $N$ lines will contain a Name.

Followed by integer $Q$ followed by $Q$ lines each having a word.

## Output Format

Print the values corresponding to each test case.

## Constraints

+ $1 \leqslant N \leqslant 5200$

+ length of each word will be less than $12$

+ $1 \leqslant Q \leqslant 100$

## Sample Tests

### Test 1

```
5
ALEX
LUIS
JAMES
BRIAN
PAMELA
1
PAMELA
```

### Test 2

```
240
```
