# Super Functional Strings

---

| Field | Value |
|---|---|
| **Slug** | `super-functional-strings` |
| **Domain** | algorithms |
| **Difficulty** | Advanced |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/super-functional-strings |

---

## Problem Statement

We define a function, $F$, on a string, $P$, as follows:

$$F(P) = \bigg(length(P)^{distinct(P)} \bigg)\ \% \ (10^9 + 7)$$

where:

* $length(P)$ denotes the number of characters in string $P$.
* $distinct(P)$ denotes the number of distinct characters in string $P$.

Consuela loves creating string challenges and she needs your help testing her newest one! Given a string, $S$, consisting of $N$ lowercase letters, compute the summation of function $F$ (provided above) over all possible *distinct substrings* of $S$. As the result is quite large, print it modulo $10^9 + 7$.

## Input Format

The first line contains a single integer, $T$, denoting the number of test cases.	
Each of the $T$ subsequent lines contains a string, $S$.

## Output Format

For each test case, print the answer modulo $10^9 + 7$.

## Constraints

- $1 \le T \le 100$

- $1 \le N \le 10^5$

- The sum of $N$ over all test cases does not exceed $10^5$.


**Scoring**

* $N \le 100$ for $20 \%$ of test data.
* $N \le 1000$ for $40 \%$ of test data.

* $N \le 10^5$ for $100 \%$ of test data.

## Sample Tests

### Test 1

```
3
aa
aba
abc
```

### Test 2

```
3
19
38
```
