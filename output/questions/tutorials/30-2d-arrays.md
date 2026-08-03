# Day 11: 2D Arrays

---

| Field | Value |
|---|---|
| **Slug** | `30-2d-arrays` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/30-2d-arrays |

---

## Preview

Find the maximum sum of any hourglass in a 2D-Array.

## Problem Statement

**Objective**	
Today, we are building on our knowledge of *arrays* by adding another dimension. Check out the [Tutorial](/challenges/30-2d-arrays/tutorial) tab for learning materials and an instructional video.		

**Context**		
Given a $6 \times 6$ *2D Array*, $A$: 

	1 1 1 0 0 0
    0 1 0 0 0 0
    1 1 1 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0

We define an hourglass in $A$ to be a subset of values with indices falling in this pattern in $A$'s graphical representation:

    a b c
      d
    e f g

There are $16$ hourglasses in $A$, and an *hourglass sum* is the sum of an hourglass' values. 

**Task**	
Calculate the hourglass sum for every hourglass in $A$, then print the *maximum* hourglass sum.

**Example**


In the array shown above, the maximum hourglass sum is $7$ for the hourglass in the top left corner.

## Input Format

There are $6$ lines of input, where each line contains $6$ space-separated integers that describe the *2D Array* $A$.

## Output Format

Print the maximum hourglass sum in $A$.

## Constraints

- $-9 \le A[i][j] \le 9$	
- $0 \le i,j \le 5$

## Sample Tests

### Test 1

```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```

### Test 2

```
a b c
 d
e f g
```

### Test 3

```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
```

### Test 4

```
19
```

### Test 5

```
1 1 1 1 1 0 1 0 0 0 0 0
 1 0 0 0
1 1 1 1 1 0 1 0 0 0 0 0
0 1 0 1 0 0 0 0 0 0 0 0
 1 1 0 0
0 0 2 0 2 4 2 4 4 4 4 0
1 1 1 1 1 0 1 0 0 0 0 0
 0 2 4 4
0 0 0 0 0 2 0 2 0 2 0 0
0 0 2 0 2 4 2 4 4 4 4 0
 0 0 2 0
0 0 1 0 1 2 1 2 4 2 4 0
```

### Test 6

```
2 4 4
 2
1 2 4
```
