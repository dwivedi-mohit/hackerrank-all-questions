# Interval Selection

---

| Field | Value |
|---|---|
| **Slug** | `interval-selection` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 65 |
| **URL** | https://www.hackerrank.com/challenges/interval-selection |

---

## Preview

Given a list of intervals, select the largest subset such that no three intervals in the subset share a common point.

## Problem Statement

Given a set of $n$ intervals, find the size of its largest possible subset of intervals such that no three intervals in the subset share a common point.

## Input Format

The first line contains an integer, $s$, denoting the number of interval sets you must find answers for. The $s \cdot (n + 1)$ subsequent lines describe each of the $s$ interval sets as follows:

1. The first line contains an integer, $n$, denoting the number of intervals in the list. 
2. Each line $i$ of the $n$ subsequent lines contains two space-separated integers describing the respective starting ($a_i$) and ending ($b_i$) boundaries of an interval.

## Output Format

For each of the $s$ interval sets, print an integer denoting the size of the largest possible subset of intervals in the given set such that no three points in the subset overlap.

## Constraints

- $1 \le s \le 100$
- $2 \le n \le 1000$

- $1 \le a_i \le b_i \le 10^9$

## Sample Tests

### Test 1

```
4
3
1 2
2 3
2 4
3
1 5
1 5
1 5
4
1 10
1 3
4 6
7 10
4
1 10
1 3
3 6
7 10
```

### Test 2

```
2
2
4
3
```
