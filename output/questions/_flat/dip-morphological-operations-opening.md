# Morphological Operations: Opening

---

| Field | Value |
|---|---|
| **Slug** | `dip-morphological-operations-opening` |
| **Domain** | ai |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/dip-morphological-operations-opening |

---

## Preview

Opening an image with a structuring element.

## Problem Statement

You are provided the following image $B$

	0000000000
    0111111100
    0000111100
    0000111100
    0001111100
    0000111100
    0001100000
    0000000000
    0000000000
  

The structuring element $S$ is given below, and its' origin is the middle pixel.

	111
	111
	111
  

What is the **total number of pixels marked 1** in the image obtained after $B$ is opened with the structuring element $S$? Only enter the integer, or a program to compute it.

## Sample Tests

### Test 1

```
0000000000
0111111100
0000111100
0000111100
0001111100
0000111100
0001100000
0000000000
0000000000
```

### Test 2

```
111
111
111
```
