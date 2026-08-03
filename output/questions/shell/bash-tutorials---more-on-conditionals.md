# More on Conditionals

---

| Field | Value |
|---|---|
| **Slug** | `bash-tutorials---more-on-conditionals` |
| **Domain** | shell |
| **Difficulty** | Easy |
| **Score** | 3 |
| **URL** | https://www.hackerrank.com/challenges/bash-tutorials---more-on-conditionals |

---

## Preview

Three sides of a triangle are provided to you. Is the Triangle Scalene, Equilateral or Isosceles?

## Problem Statement

Given three integers ($X$, $Y$, and $Z$) representing the three sides of a triangle, identify whether the triangle is scalene, isosceles, or equilateral.

- If all three sides are equal, output `EQUILATERAL`.

- Otherwise, if any two sides are equal, output `ISOSCELES`.

- Otherwise, output `SCALENE`.

## Input Format

Three integers, each on a new line.

## Output Format

One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).

## Constraints

$1 \le X,Y,Z \le 1000$

The sum of any two sides will be greater than the third.

## Sample Tests

### Test 1

```
2
3
4
```

### Test 2

```
6
6
6
```

### Test 3

```
SCALENE
```

### Test 4

```
EQUILATERAL
```
