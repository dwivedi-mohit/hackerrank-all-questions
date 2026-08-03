# Day 5: Template Literals

---

| Field | Value |
|---|---|
| **Slug** | `js10-template-literals` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/js10-template-literals |

---

## Preview

JavaScript Template Strings

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

## Sample Tests

### Test 1

```
10
14
```

### Test 2

```
10
14
```
