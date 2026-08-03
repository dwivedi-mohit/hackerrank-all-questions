# Sum vs XOR

---

| Field | Value |
|---|---|
| **Slug** | `sum-vs-xor` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 25 |
| **URL** | https://www.hackerrank.com/challenges/sum-vs-xor |

---

## Preview

Find all the numbers below n such that the sum and xor of that number with n are the same.

## Problem Statement

Given an integer $n$, find each $x$ such that:

* $0 \le x \le n$
* $n+x = n \oplus x$

where $\oplus$ denotes the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operator. Return the number of $x$'s satisfying the criteria.

**Example** 

$n = 4$ 


There are four values that meet the criteria:


- $4 + 0 = 4 \oplus 0 = 4$
- $4 + 1 = 4 \oplus 1 = 5$
- $4 + 2 = 4 \oplus 2 = 6$
- $4 + 3 = 4 \oplus 3 = 7$  


Return $4$.


**Function Description**

Complete the sumXor function in the editor below.


sumXor has the following parameter(s):

- *int n:* an integer 


**Returns** 

- *int:* the number of values found

## Input Format

A single integer, $n$.

## Output Format

**Sample Input 0**

    5
  

**Sample Output 0**

    2
  

**Explanation 0**

For $n=5$, the $x$ values $0$ and $2$ satisfy the conditions:

* $5 + 0 = 5,\ \ 5 \oplus 0 = 5$
* $5 + 2 = 7,\ \ 5 \oplus 2 = 7$

**Sample Input 1**

    10
  

**Sample Output 1**

    4

**Explanation 1**

For $n = 10$, the $x$ values $0$, $1$, $4$, and $5$ satisfy the conditions:

* $10+0 = 10,\ \ 10 \oplus 0 = 10$
* $10+1 = 11,\ \ 10 \oplus 1 = 11$
* $10+4 = 14,\ \ 10 \oplus 4 = 14$
* $10+5 = 15,\ \ 10 \oplus 5 = 15$

## Constraints

* $0 \le n \le 10^{15}$

**Subtasks**

* $0 \le n \le 100$ for $\text{60%}$ of the maximum score.

## Sample Tests

### Test 1

```
5
```

### Test 2

```
2
```

### Test 3

```
10
```

### Test 4

```
4
```
