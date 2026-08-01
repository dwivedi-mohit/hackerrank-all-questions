# Type of Triangle

- **Domain:** algorithms
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9676716568155181
- **Total Submissions:** 828499
- **Solved Count:** 801715
- **URL:** https://www.hackerrank.com/challenges/what-type-of-triangle

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

## Sample Output

Isosceles
Equilateral
Scalene
Not A Triangle

## Explanation

Values in the tuple  form an Isosceles triangle, because .

Values in the tuple  form an Equilateral triangle, because .
Values in the tuple  form a Scalene triangle, because .

Values in the tuple  cannot form a triangle because the combined value of sides  and  is not larger than that of side .
