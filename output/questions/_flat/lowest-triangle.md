# Minimum Height Triangle

---

| Field | Value |
|---|---|
| **Slug** | `lowest-triangle` |
| **Domain** | mathematics |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/lowest-triangle |

---

## Preview

Find the smallest height of a triangle preserving the given constraints.

## Problem Statement

Given integers $b$ and $a$, find the smallest integer $h$, such that there exists a triangle of height $h$, base $b$, having an area of at least $a$.


![image](https://s3.amazonaws.com/hr-assets/0/1496306792-f2c37eea44-triangle.jpg)


**Example**

$b = 4$

$a = 6$


The minimum height $h$ is $3$.  One example is a triangle formed at points (0, 0), (4, 0), (2, 3).


**Function Description**


Complete the *lowestTriangle* function in the editor below.


*lowestTriangle* has the following parameters:


- *int b:* the base of the triangle

- *int a:* the minimum area of the triangle


**Returns**


- *int:*  the minimum integer height to form a triangle with an area of at least $a$

## Input Format

There are two space-separated integers $b$ and $a$, on a single line.

## Constraints

+ $1 \le b \leq 10^6$
+ $1 \le a \le 10^6$

## Sample Tests

### Test 1

```
2 2
```

### Test 2

```
2
```

### Test 3

```
17 100
```

### Test 4

```
12
```
