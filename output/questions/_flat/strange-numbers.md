# Strange numbers

---

| Field | Value |
|---|---|
| **Slug** | `strange-numbers` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/strange-numbers |

---

## Preview

How many strange numbers belong to interval [L, R]?

## Problem Statement

Let $length(A)$ denote the count of digits of a number $A$ in its decimal representation.

John is looking for new methods of determining which numbers are strange all day long.

All non-negative numbers of length 1 are strange. Further, a number $X$ with $length(X) \ge1$ can also be considered strange if and only if


* $X$ is evenly divisible by $length(X)$

* the number $X/length(X)$ is recursively strange

Your task is to calculate how many strange numbers belong to an interval $[L, R]$.


**Input Format**

The first line contains single integer $T$ - the number of test cases. Next $T$ lines contain two integers separated by single space $L$ and $R$.


**Output Format**

In $T$ lines, print $T$ integers - count of strange numbers belonging to the interval $[L, R]$.

**Constraints**

$1 \le T \le 200$

$0 \le L < R \le 10^{18}$


**Sample Input**

    5
    7 25
    45 50
    1 100
    99 103
    0 1000000
  

**Sample Output**

    10
    1
    26
    0
    96
  

**Explanation**

First testcase: There are $10$ strange numbers that belong to the interval $[7,25]$. They are $7,8,9,10,12,14,16,18,20,24$.

Second testcase: Only $48$ satisfies the given constraints.

## Sample Tests

### Test 1

```
5
7 25
45 50
1 100
99 103
0 1000000
```

### Test 2

```
10
1
26
0
96
```
