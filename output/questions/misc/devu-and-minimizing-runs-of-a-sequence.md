# Devu and Minimizing Runs of a String

---

| Field | Value |
|---|---|
| **Slug** | `devu-and-minimizing-runs-of-a-sequence` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 50 |
| **Contest** | 101hack23 |
| **URL** | https://www.hackerrank.com/challenges/devu-and-minimizing-runs-of-a-sequence |

---

## Preview

Help Devu minimize runs of a string.

## Problem Statement

Devu likes to play with strings a lot. One day he found a string $s$ with characters 'R' and 'B' in a box of marbles. 

He defined _runs_ of a string as the size of string after merging all the consecutive equal characters of the string into a single character. E.g. 'RRBB' has $2$ runs, whereas 'RR' and 'RBBRRR' have $1$ and $3$ runs respectively.

In a single operation, Devu can remove a single character from some position in the string and insert it back at any other position. He is allowed to do at most one such operation. He wants to minimize the number of runs in the string $s$.

Please help Devu in finding minimum number of runs of the string $s$.

## Input Format

-	The first line of the input contains a single integer, $T$, denoting the number of test cases.
-	For each test case, there is a single line containing string $s$.

## Output Format

For each test case, print in a new line containing a single integer denoting the answer to the problem.

**Constraints**

-	$1 \leq $ size of string $s \leq 10^5$
-	Sum of sizes of string $s$ over all the test cases will be less than $2 * 10^6$

## Sample Tests

### Test 1

```
3
RB
RBRR
RRR
```

### Test 2

```
2
2
1
```
