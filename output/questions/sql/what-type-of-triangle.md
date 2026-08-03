# Type of Triangle

---

| Field | Value |
|---|---|
| **Slug** | `what-type-of-triangle` |
| **Domain** | sql |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/what-type-of-triangle |

---

## Preview

Query a triangle's type based on its side lengths.

## Problem Statement

Write a query identifying the *type* of each record in the **TRIANGLES** table using its three side lengths. Output one of the following statements for each record in the table:

- **Equilateral**: It's a triangle with $3$ sides of equal length.
- **Isosceles**: It's a triangle with $2$ sides of equal length.
- **Scalene**: It's a triangle with $3$ sides of differing lengths.
- **Not A Triangle**: The given values of *A*, *B*, and *C* don't form a triangle.

## Input Format

The **TRIANGLES** table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/12887/1443815629-ac2a843fb7-1.png" />

Each row in the table denotes the lengths of each of a triangle's three sides.

## Sample Tests

### Test 1

```
Isosceles
Equilateral
Scalene
Not A Triangle
```
