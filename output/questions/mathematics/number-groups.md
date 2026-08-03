# Number Groups

---

| Field | Value |
|---|---|
| **Slug** | `number-groups` |
| **Domain** | mathematics |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/number-groups |

---

## Preview

Find the sum of consecutive odd number groups.

## Problem Statement

The positive odd numbers are sorted in ascending order as $1, 3, 5, 7, 9, 11, 13, 15, 17, 19 \ldots$, and grouped as $(1), (3, 5), (7, 9, 11), (13, 15, 17, 19), \ldots $ and so on.

Thus, the first group is $(1)$, the second group is $(3, 5)$, the third group is $(7, 9, 11)$, etc. In general, the $k^\text{th}$ group contains the next $k$ elements of the sequence. 

Given $k$, find the sum of the elements of the $k^\text{th}$ group. For example, for $k = 3$, the answer is $27$:


![image](https://s3.amazonaws.com/hr-assets/0/1511935621-d85a3653c7-Numbergroups-2.png)

Complete the function `sumOfGroup` with input integer $k$.  Return the sum of the elements of the $k$th group.

## Constraints

- $1 \le k \le 10^6$


**Subtasks**


- For $50\%$ of the maximum score, $k \le 10^3$

## Sample Tests

### Test 1

```
sumOfGroup
```
