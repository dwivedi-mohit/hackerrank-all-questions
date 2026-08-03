# Requirement

---

| Field | Value |
|---|---|
| **Slug** | `requirement` |
| **Domain** | algorithms |
| **Difficulty** | Advanced |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/requirement |

---

## Preview

Given a list of inequalities, calculate the number of different assignments that satisfy them.

## Problem Statement

There are $n$ variables and $m$ requirements. Requirements are represented as $(x \le y)$, meaning that the $x^{th}$ variable must be less than or equal to the $y^{th}$ variable. 

Your task is to assign non-negative numbers smaller than $10$ to each variable and then calculate the number of different assignments satisfying all requirements. Two assignments are different if and only if at least one variable is assigned to a different number in both assignments. Print your answer modulo $10^3+7$.

## Input Format

The first line contains $2$ space-separated integers, $n$ and $m$, respectively.
Each of the $m$ subsequent lines contains $2$ space-seperated integers describing the respective $x$ and $y$ values for an $(x \le y)$ requirement.

## Output Format

Print your answer modulo $10^3+7$.

## Constraints

- $0 \lt n \lt 14$
- $0 \lt m \lt 200$
- $0 \le x, y \lt n$

## Sample Tests

### Test 1

```
6 7
1 3
0 1
2 4
0 4
2 5
3 4
0 2
```

### Test 2

```
1000
```
