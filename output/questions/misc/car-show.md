# Car Show

---

| Field | Value |
|---|---|
| **Slug** | `car-show` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 50 |
| **Contest** | 101hack52 |
| **URL** | https://www.hackerrank.com/challenges/car-show |

---

## Preview

Find the number of choices for the set of cars to display.

## Problem Statement

You are in charge of planning a prestigious car show that will run for several days.

The company has an array of $n$ cars, numbered $1$ to $n$ from left to right. They don't necessarily have distinct models, though. We represent a car's model with an integer: car $i$ has model $A_i$. 

The show will run for $q$ days. You are tasked to select a nonempty subset of the cars to be displayed on each day. However, there are a few restrictions. Specifically, for the $i^\text{th}$ day,

- The set of displayed cars must form a contiguous subarray of the cars.
- The set of displayed cars must lie between car $l_i$ and car $r_i$, inclusive.
- The models of the displayed cars must be distinct.

For each day, how many valid choices are there for the set of cars to display on that day?

## Input Format

The first line contains two space-separated integers $n$ and $q$. 

The second line contains $n$ space-separated integers $A_1, A_2, \ldots, A_n$.

The $i^\text{th}$ of the next $q$ lines contains two space-separated integers $l_i$, $r_i$.

## Output Format

Print $q$ lines. The $i^\text{th}$ line must contain a single integer denoting the answer for the $i^\text{th}$ line.

## Constraints

- $1 \le n, q \le 10^5$

- $1 \le A_i \le 10^6$

- $1 \le l_i \le r_i \le n$


**Subtasks**


- For $20\%$ of the maximum score, $n, q \le 10^3$

## Sample Tests

### Test 1

```
7 5
6 5 1 2 4 6 1
1 7
2 7
1 6
3 6
2 5
```

### Test 2

```
24
19
20
10
10
```
