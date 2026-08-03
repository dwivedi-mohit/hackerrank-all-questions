# Day 7: Spearman's Rank Correlation Coefficient

---

| Field | Value |
|---|---|
| **Slug** | `s10-spearman-rank-correlation-coefficient` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient |

---

## Preview

Computing Spearman's rank correlation coefficient.

## Problem Statement

**Objective** <br>
In this challenge, we practice calculating *Spearman's rank correlation coefficient*. Check out the [Tutorial](/challenges/s10-spearman-rank-correlation-coefficient/tutorial) tab for learning materials!

**Task**<br>
Given two $n$-element data sets, $X$ and $Y$, calculate the value of Spearman's rank correlation coefficient.

## Input Format

The first line contains an integer, $n$, denoting the number of values in data sets $X$ and $Y$. 	
The second line contains $n$ space-separated real numbers (scaled to *at most* one decimal place) denoting data set $X$. 	
The third line contains $n$ space-separated real numbers (scaled to *at most* one decimal place) denoting data set $Y$.

## Output Format

Print the value of the Spearman's rank correlation coefficient, rounded to a scale of $3$ decimal places.

## Constraints

- $10 \le n \le 100$
- $1 \le x_{i} \le 500$, where $x_{i}$ is the $i^{th}$ value of data set $X$.
- $1 \le y_{i} \le 500$, where $y_{i}$ is the $i^{th}$ value of data set $Y$.
- Data set $X$ contains unique values.
- Data set $Y$ contains unique values.

## Sample Tests

### Test 1

```
10
10 9.8 8 7.8 7.7 1.7 6 5 1.4 2 
200 44 32 24 22 17 15 12 8 4
```

### Test 2

```
0.903
```
