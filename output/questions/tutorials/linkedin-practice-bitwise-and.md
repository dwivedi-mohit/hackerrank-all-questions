# Bitwise AND

---

| Field | Value |
|---|---|
| **Slug** | `linkedin-practice-bitwise-and` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/linkedin-practice-bitwise-and |

---

## Preview

Apply everything we've learned in this bitwise AND challenge.

## Problem Statement

Given set $S = \{1, 2, 3,\ldots, N\}$. Find two integers, $A$ and $B$ (where $A \lt B$), from set $S$ such that the value of $A \text{&} B$ is the maximum possible *and also less than a given integer, $K$*. In this case, $\text{&}$ represents the *bitwise AND* operator.

## Input Format

The first line contains an integer, $T$, the number of test cases. 		
Each of the $T$ subsequent lines defines a test case as $2$ space-separated integers, $N$ and $K$, respectively.

## Output Format

For each test case, print the maximum possible value of  $A \text{&} B$ on a new line.

## Constraints

* $1 \le T \le 10^3$
* $2 \le N \le 10^3$
* $2 \le K \le N$

## Sample Tests

### Test 1

```
3
5 2
8 5
2 2
```

### Test 2

```
1
4
0
```
