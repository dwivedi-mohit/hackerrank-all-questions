# Left Rotation

---

| Field | Value |
|---|---|
| **Slug** | `three-month-preparation-kit-array-left-rotation` |
| **Domain** |  |
| **Difficulty** | Easy |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/three-month-preparation-kit-array-left-rotation |

---

## Preview

Given an array and a number, d, perform d left rotations on the array.

## Problem Statement

A *left rotation* operation on an array of size $n$ shifts each of the array's elements $1$ unit to the left. Given an integer, $d$, rotate the array that many steps left and return the result.


**Example**

$d=2$

$arr = [1, 2, 3, 4, 5]$


After $2$ rotations, $arr' = [3, 4, 5, 1, 2]$.

**Function Description**


Complete the *rotateLeft* function in the editor below.


*rotateLeft* has the following parameters:


- *int d:*  the amount to rotate by

- *int arr[n]:* the array to rotate


**Returns**


- *int[n]:* the rotated array

## Input Format

The first line contains two space-separated integers that denote $n$, the number of integers, and $d$, the number of left rotations to perform. 	
The second line contains $n$ space-separated integers that describe $arr[]$.

## Constraints

- $1 \le n \le 10^5$

- $1 \le d \le n$

- $1 \le a[i] \le 10^6$

## Sample Tests

### Test 1

```
5 4
1 2 3 4 5
```

### Test 2

```
5 1 2 3 4
```
