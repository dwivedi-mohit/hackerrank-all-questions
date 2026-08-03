# The Chosen One

---

| Field | Value |
|---|---|
| **Slug** | `the-chosen-one` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/the-chosen-one |

---

## Preview

Given a list of integers, find and print an integer that is a divisor of all but one integer in the list.

## Problem Statement

You are given a sequence of $n$ integers, $a_0, a_1, \ldots, a_{n-1}$. Find and print any integer $x$ such that $x$ is divisor of every $a_i$ except for exactly one element.

## Input Format

The first line contains an integer, $n$, denoting the length of the sequence.		
The second line contains $n$ positive space-separated integers describing $a_0, a_1, \ldots, a_{n-1}$.

## Output Format

Print any positive integer denoting $x$ such that $x$ is a divisor of exactly $n-1$ of the sequence's elements. $x$ must be between $1$ and $2 \cdot 10^{18}$

## Constraints

- $1 \le n \le 10^5$
- $1 \le a_i \le 10^{18}$
- It is guaranteed that a solution exists.

## Sample Tests

### Test 1

```
4
3 6 18 12
```

### Test 2

```
6
```
