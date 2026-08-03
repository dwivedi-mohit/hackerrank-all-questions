# Subsets Counting

---

| Field | Value |
|---|---|
| **Slug** | `subsets-counting` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 80 |
| **Contest** | 101hack31 |
| **URL** | https://www.hackerrank.com/challenges/subsets-counting |

---

## Problem Statement

You are given a set of integers from $1$ to $N$. Count the interesting pairs of ($A$, $B$) that satisfy the following conditions:

1. $A$ and $B$ are both subsets of the given set.
2. XOR($A$) &le; XOR($B$)
3. $A$ and $B$ have no common elements.

XOR($A$) is the bit-xor (`^` in C++ and Java) results over all its elements (e.g. XOR({1, 3}) = 2). We define the XOR of an empty set to be $0$ (XOR({}) = $0$). 

**Note:** The answer may be large so you only need to print its remainder by dividing with $M$.

## Input Format

The first line contains two space-separated integers, $N$ and $M$.

**Constraints**

In $20\%$ test cases: $1$ &le; $N$ &le; $10$

In $50\%$ test cases: $1$ &le; $N$ &le; $100$  $M=10^9+7$

In $100\%$ test cases: $1$ &le; $N$ &le; $3000$  $1$ &le; $M$ &le; $10^9+7$

## Output Format

Print the answer on a single line.

## Sample Tests

### Test 1

```
2 10
```

### Test 2

```
5
```
