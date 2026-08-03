# Diagonal Difference

---

| Field | Value |
|---|---|
| **Slug** | `three-month-preparation-kit-diagonal-difference` |
| **Domain** |  |
| **Difficulty** | Easy |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/three-month-preparation-kit-diagonal-difference |

---

## Preview

Calculate the absolute difference of sums across the two diagonals of a square matrix.

## Problem Statement

Given a square matrix, calculate the absolute difference between the sums of its diagonals.



For example, the square matrix $arr$ is shown below:


	1 2 3
    4 5 6
    9 8 9

  

The left-to-right diagonal = $1 + 5 + 9 = 15$.  The right to left diagonal = $3 + 5 + 9 = 17$.  Their absolute difference is $|15 - 17| = 2$.


**Function description**

Complete the $\textit{diagonalDifference}$ function in the editor below.


diagonalDifference takes the following parameter:



-	<em>int arr[n][m]</em>: an array of integers 
  

**Return**


-	<em>int</em>: the absolute diagonal difference

## Input Format

The first line contains a single integer, $n$,  the number of rows and columns in the square matrix $arr$.

Each of the next $n$ lines describes a row, $arr[i]$, and consists of $n$ space-separated integers $arr[i][j]$.

## Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

## Constraints

+ $-100 \le arr[i][j] \le 100$

## Sample Tests

### Test 1

```
1 2 3
4 5 6
9 8 9
```

### Test 2

```
3
11 2 4
4 5 6
10 8 -12
```

### Test 3

```
15
```

### Test 4

```
11
 5
 -12
```

### Test 5

```
4
 5
10
```
