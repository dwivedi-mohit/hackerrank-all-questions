# Triple sum

---

| Field | Value |
|---|---|
| **Slug** | `triple-sum` |
| **Domain** |  |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/triple-sum |

---

## Preview

Sum of special triplets having elements from 3 different arrays.

## Problem Statement

Given $3$ arrays $a,\ b,\ c$ of different sizes, find the number of *distinct* triplets $(p,\ q,\ r)$ where $p$ is an element of $a$, written as $p \in a$, $\ q \in b$, and $\ r \in c$, satisfying the criteria:  $p \le q \ and \  q \ge r$.

For example, given $a = [3,5,7], b = [3,6],$ and $c = [4,6,9]$, we find four distinct triplets: $(3,6,4), (3,6,6), (5,6,4), (5,6,6)$.


**Function Description**

Complete the *triplets* function in the editor below.  It must return the number of distinct triplets that can be formed from the given arrays.


triplets has the following parameter(s):

- *a, b, c*: three arrays of integers .

## Input Format

The first line contains $3$ integers $lena,\ lenb,\ and\ lenc$, the sizes of the three arrays.

The next $3$ lines contain space-separated integers numbering $lena,\ lenb,\ and\  lenc$ respectively.

## Output Format

Print an integer representing the number of distinct triplets.

## Constraints

$1 \le lena,lenb,lenc \le 10^5$

$1 \le \text{ all elements in } a, b, c \le 10^8$

## Sample Tests

### Test 1

```
3 2 3
1 3 5
2 3
1 2 3
```

### Test 2

```
8
```

### Test 3

```
3 3 3
1 4 5
2 3 3
1 2 3
```

### Test 4

```
5
```

### Test 5

```
4 3 4
1 3 5 7
5 7 9
7 9 11 13
```

### Test 6

```
12
```
