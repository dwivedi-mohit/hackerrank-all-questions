# Largest Non-Coprime Submatrix

---

| Field | Value |
|---|---|
| **Slug** | `largest-coprime-submatrix` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/largest-coprime-submatrix |

---

## Preview

Given a matrix find the largest coprime submatrix.

## Problem Statement

Given a matrix you need to find the submatrix with the largest number of elements, where the GCD (Greatest Common Divisor) of its elements is greater than one. A submatrix of the matrix is a sub-section composed of contiguous rows and columns of the original matrix.
<br/>

**Input**
Two numbers n,m in the first line. Followed by n lines with m numbers in each line.<br/>

**Constraints**


1<=N,M<=200<br/>
1<=numbers<=10000<br/>

**Output**
Just a largest area where GCD is greater than 1.<br/>

**Sample Input**


    3 3
    2 6 8
    4 8 3
    6 9 4

**Sample Output**


    4

If you observe the following submatrix:


    2 6

    4 8


The GCD is 2.
There is no matrix larger than this with a GCD > 1.

## Sample Tests

### Test 1

```
3 3
2 6 8
4 8 3
6 9 4
```

### Test 2

```
4
```

### Test 3

```
2 6 
4 8
```
