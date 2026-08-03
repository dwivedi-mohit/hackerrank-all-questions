# Constructing a Number

---

| Field | Value |
|---|---|
| **Slug** | `constructing-a-number` |
| **Domain** | mathematics |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/constructing-a-number |

---

## Preview

Construct a number divisible by 3 from the given numbers by reordering their digits.

## Problem Statement

Manipulating numbers is at the core of a programmer's job. To test how well you know their properties, you are asked to solve the following problem.

You are given $n$ non-negative integers $a_1$, $a_2$, ..., $a_n$. You want to know whether it's possible to construct a new integer using all the digits of these numbers such that it would be divisible by $3$. You can reorder the digits as you want. The resulting number can contain leading zeros.

For example, consider the numbers $50, 40, 90$ from which you have to construct a new integer as described above. Numerous arrangements of digits are possible; but we have illustrated one below. 


![image](https://s3.amazonaws.com/hr-assets/0/1514370322-1398c77ec5-number_cons1.png)


Complete the function `canConstruct` which takes an integer array as input and return "`Yes`" or "`No`" based on whether or not the required integer can be formed.

## Input Format

The first line contains a single integer $t$ denoting the number of queries. The following lines describe the queries.

Each query is described in two lines. The first of these lines contains a single integer $n$. The second contains $n$ space-separated integers $a_1$, $a_2$, ..., $a_n$.

## Output Format

For each query, print a single line containing "`Yes`" if it's possible to construct such integer and "`No`" otherwise.

## Constraints

- $1 \leq t \leq 100$
- $1 \leq n \leq 100$
- $1 \leq a_i \leq 10^9$

**Subtasks**

For 33.33% of the total score:

- $n = 1$
- $1 \leq a_1 \leq 10 ^ 6$

## Sample Tests

### Test 1

```
3
1
9
3
40 50 90
2
1 4
```

### Test 2

```
Yes
Yes
No
```
