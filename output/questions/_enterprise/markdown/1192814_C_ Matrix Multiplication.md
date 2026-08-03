# C: Matrix Multiplication

## Metadata

- **ID:** 1192814
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** PThread, Medium, Arrays, References
- **Skills:** C (Intermediate)
- **Languages:** c

## Summary

This coding question evaluates matrix multiplication, threading, and memory management concepts, ideal for mid-level roles. The problem requires implementing functions to initialize and multiply two matrices using threads.

## Problem Statement

Given two threads, efficiently multiply two matrices.

 

Example

`[[1 2], [3 4], [5 6]] * [[7 8], [9 10]]`

`= [[25 28], [57 64], [89 100]]`

 

Function Description

 

Complete the following functions:

	
- 
initializeFirstMatrix() to initialize first matrix: m1
	
- 
initializeSecondMatrix() to initialize second matrix: m2
	
- 
readFirstMatrix() to read elements of first matrix: m1
	
- 
readSecondMatrix() to read elements of second matrix: m2
	
- 
initializeResultMatrix() to initialize result matrix: res
	
- 
multiplyMatrix() to multiply m1 and m2 and store result in res

 

Constraints

	
- 1 ≤ matrix1[i][j] < 2000
	
- 1 ≤ matrix2[i][j] < 2000

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first 2 lines correspond to the shapes of the matrices.

The last two lines correspond two their values.

The output shows the product of row of n[i] and column n[j].

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

3 3                  
3 2
2 2 5 5 4 31 4 4 2 
6 5 5 4 9

```

Sample Output

Sizes of matrices:
3 3
3 2

Matrix 1:
2 2 5 
5 4 31 
4 4 2 

Matrix 2:
6 5 
5 4 
9 0 

Product of the 2 matrices:
67 18 
329 41 
62 36 

```

Explanation

Multiply a 3x3 and 3x2 matrix.

Sample Case 1

Sample Input For Custom Testing

2 2
2 4
19 59 59 97 
79 89 2 61 79 2 53 53

```

Sample Output

Sizes of matrices:
2 2
2 4

Matrix 1:
19 59 
59 97 

Matrix 2:
79 89 2 61 
79 2 53 53 

Product of the 2 matrices:
6162 1809 3165 4286 
12324 5445 5259 8740 

```

Explanation

Multiply a 2x2 and 2x4 matrix.

## Sample Input/Output

## Preview

Given two threads, efficiently multiply two matrices.
