# Tight Arrays

---

| Field | Value |
|---|---|
| **Slug** | `tight-arrays` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 15 |
| **Contest** | 101hack48 |
| **URL** | https://www.hackerrank.com/challenges/tight-arrays |

---

## Preview

Find the shortest array that begins with a, ends with c, contains b, and whose absolute difference of adjacent values are at most 1.

## Problem Statement

We call an array of integers *tight* if every pair of adjacent integers in the array has an absolute difference $\le 1$. For example, the array $[3, 4, 4, 3, 2, 1, 2, 3, 4, 4, 5, 5]$ is tight, but the array $[1, 2, 4, 3, 3]$ is not:


![Illustration of tight arrays.](https://s3.amazonaws.com/hr-assets/0/1491899184-219fb128de-12.png "Illustration of tight arrays.")

The diagram above shows the absolute differences between each pair of adjacent elements. Note that the second array is *not* tight, because it has a pair of adjacent elements whose absolute difference is greater than $1$.

Given $a$, $b$, and $c$, complete the function below by returning the length of the shortest tight array such that the first element is $a$, the last element is $c$, and the array contains $b$.

## Input Format

Three space-separated integers describing the respective values of $a$, $b$, and $c$.

## Output Format

Return a single integer denoting the length of the shortest tight array such that the first element is $a$, the last element is $c$, and the array contains the element $b$.

## Constraints

- $1 \le a, b, c \le 100$

## Sample Tests

### Test 1

```
5 7 11
```

### Test 2

```
7
```

### Test 3

```
3 1 2
```

### Test 4

```
4
```

### Test 5

```
5 5 6
```

### Test 6

```
2
```
