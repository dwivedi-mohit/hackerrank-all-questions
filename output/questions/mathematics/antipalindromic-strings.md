# Anti-Palindromic Strings

---

| Field | Value |
|---|---|
| **Slug** | `antipalindromic-strings` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/antipalindromic-strings |

---

## Preview

Count the number of strings that do not contain any palindromic string of the length greater than 1 as a substring.

## Problem Statement

You are given two integers, $N$ and $M$. Count the number of strings of length $N$ (under the alphabet set of size $M$) that doesn't contain any palindromic string of the length greater than $1$ as a consecutive substring.

## Input Format

Several test cases will be given to you in a single file. The first line of the input will contain a single integer, $T$, the number of test cases.

Then there will be $T$ lines, each containing two space-separated integers, $N$ and $M$, denoting a single test case. The meanings of $N$ and $M$ are described in the Problem Statement above.

## Output Format

For each test case, output a single integer - the answer to the corresponding test case. This number can be huge, so output it modulo $10^9+7$.

**Constraints**


$1 \leq T \leq 10^5$<br>
$1 \leq N, M \leq 10^9$

## Sample Tests

### Test 1

```
2
2 2
2 3
```

### Test 2

```
2
6
```

### Test 3

```
AA
AB
BA
BB
```

### Test 4

```
AA
AB
AC
BA
BB
BC
CA
CB
CC
```
