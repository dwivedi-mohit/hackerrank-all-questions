# Tower 3-coloring

---

| Field | Value |
|---|---|
| **Slug** | `tower-3-coloring` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/tower-3-coloring |

---

## Preview

Count different colorings of a tower with 3 colors

## Problem Statement

For a given integer $n$, there is a tower built from $3^n$ blocks stacked vertically. Each of these blocks can be colored in $3$ different colors: red, green or blue. How many different colorings of the tower can be created? Two colorings are considered different if and only if there exists at least one block with different colors in the colorings. Since the result can be a huge number, apply a modulo $10^9 + 7$ on the result.

## Input Format

The first line contains a single integer $n$.

## Output Format

In a single line print a single integer denoting the number of different colorings of tower of the height $3^n$ calculated modulo $10^9+7$.

## Constraints

+ $1 \leq n \leq 10^9$

## Sample Tests

### Test 1

```
1
```

### Test 2

```
27
```
