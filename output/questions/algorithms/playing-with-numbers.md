# Absolute Element Sums

---

| Field | Value |
|---|---|
| **Slug** | `playing-with-numbers` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/playing-with-numbers |

---

## Preview

Execute Q queries on an array of N integers.

## Problem Statement

Given an array of integers, you must answer a number of queries. Each query consists of a single integer, $x$, and is performed as follows:

1. Add $x$ to each element of the array, permanently modifying it for any future queries.
2. Find the absolute value of each element in the array and print the sum of the absolute values on a new line.

**Tip:** The Input/Output for this challenge is *very large*, so you'll have to be creative in your approach to pass all test cases.

**Function Description**


Complete the *playingWithNumbers* function in the editor below.  It should return an array of integers that represent the responses to each query.


playingWithNumbers has the following parameter(s):


- *arr*: an array of integers

- *queries*: an array of integers

## Input Format

The first line contains an integer $n$ the number of elements in $arr$.

The second line contains $n$ space-separated integers $arr[i]$.

The third line contains an integer $q$, the number of queries.

The fourth line contains $q$ space-separated integers $x$ where $queries[j] = x$.

## Output Format

For each query, print the sum of the absolute values of all the array's elements on a new line.

## Constraints

- $1 \le n \le 5 \times 10^5$

- $1 \le q \le 5 \times 10^5$

- $-2000 \le arr[i] \le 2000$, where $0 \le i \lt n$.
- $-2000 \le queries[j] \le 2000$, where $0 \le j \lt q$

## Sample Tests

### Test 1

```
3
-1 2 -3
3
1 -2 3
```

### Test 2

```
5
7
6
```
