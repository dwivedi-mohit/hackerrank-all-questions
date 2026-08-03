# Tile Painting: Revisited!

---

| Field | Value |
|---|---|
| **Slug** | `tile-painting-revisited` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/tile-painting-revisited |

---

## Preview

How many ways can Nikita paint her tiles green so that the painted indices form an Arithmetic Progression?

## Problem Statement

Nikita has a row of $N$ white tiles indexed from $1$ to $N$. This time, she's painting them green! 

Find the number of ways Nikita can paint certain tiles in green so that the indices of the green tiles form an [Arithmetic Progression](https://en.wikipedia.org/wiki/Arithmetic_progression). As this value can be quite large, your answer must be modulo $(10^9 + 7)$.

**Note:** Nikita must paint *at least* $1$ tile.

## Input Format

The first line contains a single integer, $T$, denoting the number of test cases.	
Each test case consists of a single line containing an integer, $N$, denoting the length of row of tiles.

## Output Format

On a new line for each test case, print the number of ways Nikita can paint her white tiles green so that the indices of the green tiles form an [Arithmetic Progression](https://en.wikipedia.org/wiki/Arithmetic_progression). Because this number can be quite large, your answer must be modulo $(10^9+7)$.

## Constraints

* $1 \le T \le 10$
* $1 \le N \le 10^{10}$

**Scoring**

* $1 \le N \le 2000$ for $20\%$ of test data.
* $1 \le N \le 10^5$ for $50\%$ of test data.
* $1 \le N \le 10^{10}$ for $100\%$ of test data.

## Sample Tests

### Test 1

```
3
3
4
5
```

### Test 2

```
7
13
22
```
