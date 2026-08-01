# Day 5: Template Literals

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9952578058796688
- **Total Submissions:** 61364
- **Solved Count:** 61073
- **URL:** https://www.hackerrank.com/challenges/js10-template-literals

## Problem Statement

**Objective**

In this challenge, we practice using JavaScript Template Literals. Check the attached tutorial for more details.

**Task**

The code in the editor has a tagged template literal that passes the area and perimeter of a rectangle to a tag function named *sides*. Recall that the first argument of a tag function is an array of string literals from the template, and the subsequent values are the template's respective expression values. 

Complete the function in the editor so that it does the following:

1. Finds the initial values of $s_1$ and $s_2$ by plugging the *area* and *perimeter* values into the formula: $$s = \frac{P \pm \sqrt{P^2 - 16 \cdot A}}{4}$$ where $A$ is the rectangle's area and $P$ is its perimeter.
2. Creates an array consisting of $s_1$ and $s_2$ and sorts it in ascending order.
3. Returns the sorted array.

## Input Format

The first line contains an integer denoting $s_1$.		
The second line contains an integer denoting $s_2$.

## Output Format

Return an array consisting of $s_1$ and $s_2$, sorted in ascending order.

## Constraints

- $1 \le s_1, s_2 \le 100$

## Sample Input

10
14

## Sample Output

10
14

## Explanation

The locked code in the editor passes the following arrays to the tag function:

- The value of  is [ 'The area is: ', '.\nThe perimeter is: ', '.' ].

- The value of  is [ 140, 48 ], where the first value denotes the rectangle's area, , and the second value denotes its perimeter, .

When we plug those values into our formula, we get the following:

We then store these values in an array, [14, 10], sort the array, and return the sorted array, [10, 14], as our answer.
