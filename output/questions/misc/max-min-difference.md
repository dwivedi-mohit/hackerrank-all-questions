# Minimizing the Max-Min Difference

---

| Field | Value |
|---|---|
| **Slug** | `max-min-difference` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 20 |
| **Contest** | 101hack43 |
| **URL** | https://www.hackerrank.com/challenges/max-min-difference |

---

## Preview

Delete an element such that the absolute difference between the smallest and largest elements is minimal.

## Problem Statement

Consider a sequence of $n$ integers, $A = \{a_0, a_1, \ldots, a_{n-1}\}$. We want to delete exactly one element, $a_i$, such that the difference between the smallest and largest elements (i.e., $max(A) - min(A)$) in the sequence is minimal. Then print the minimal absolute difference between the maximal and minimal elements on a new line.

## Input Format

The first line contains an integer, $n$, denoting the number of integers in the sequence.

The second line contains $n$ space-separated integers describing the respective values of $a_0,a_1, \ldots, a_{n-1}$.

## Output Format

Print a single integer denoting the minimal absolute difference between $max(A)$ and $min(A)$ after removing exactly one element.

## Constraints

- For $\text{50%}$ of the test cases  $3\leq n\leq 1000$
- For $\text{100%}$ of the test cases $3\leq n\leq 10^5$，$0\leq a_i\leq 10^9$

## Sample Tests

### Test 1

```
5
7 4 3 1 3
```

### Test 2

```
3
```

### Test 3

```
10
5 4 0 8 3 8 4 1 1 8
```

### Test 4

```
7
```
