# Rectangle Area

---

| Field | Value |
|---|---|
| **Slug** | `rectangle-area` |
| **Domain** | cpp |
| **Difficulty** | Easy |
| **Score** | 25 |
| **URL** | https://www.hackerrank.com/challenges/rectangle-area |

---

## Preview

Find out the area of a rectangle. You are given the objects to the class and you have to implement these classes.

## Problem Statement

In this challenge, you are required to compute the area of a rectangle using classes. 

Create two classes:

**Rectangle**	

The *Rectangle* class should have two data fields-*width* and *height* of *int* types. The class should have *display()* method, to print the *width* and *height* of the rectangle separated by space.

**RectangleArea**

The *RectangleArea* class is derived from *Rectangle* class, i.e., it is the sub-class of *Rectangle* class. The class should have *read\_input()* method, to read the values of *width* and *height* of the rectangle. The *RectangleArea* class should also overload the *display()* method to print the area $\left(\texttt{width} \times \texttt{height}\right)$ of the rectangle.

## Input Format

The first and only line of input contains two space separated integers denoting the width and height of the rectangle.

## Output Format

The output should consist of exactly two lines:		
In the first line, print the *width* and *height* of the rectangle separated by space.

In the second line, print the *area* of the rectangle.

## Constraints

- $1 \le {width}, {height} \le 100$

## Sample Tests

### Test 1

```
10 5
```

### Test 2

```
10 5
50
```
