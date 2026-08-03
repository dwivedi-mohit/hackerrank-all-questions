# Most Distant

---

| Field | Value |
|---|---|
| **Slug** | `most-distant` |
| **Domain** | mathematics |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/most-distant |

---

## Preview

Measure the gap between the two most distant coordinates.

## Problem Statement

Keko has $N$ dots in a 2-D coordinate plane. He wants to measure the gap between the most distant two dots. To make the problem easier, Keko decided to change each dot's $x$ *or* $y$ coordinate to zero. 


Help Keko calculate the distance!

## Input Format

The first line contains an integer, $N$, the number of dots.

The next $N$ lines each contain the integer coordinates of the dots in $(x, y)$ fashion.


**Constraints**

$2\leq N \leq 10^6$

$-10^9\leq x_i,\,y_i \leq 10^9$

It is guaranteed that all dots are distinct, and either their $x$ or $y$ coordinate is equal to $0$.

## Output Format

Print the distance between the most distant dots with an absolute error of, at most, $10^{-6}$.

## Sample Tests

### Test 1

```
4
-1 0
1 0
0 1
0 -1
```

### Test 2

```
2.000000
```
