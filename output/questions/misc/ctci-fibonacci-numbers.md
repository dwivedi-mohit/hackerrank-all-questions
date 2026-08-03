# Recursion: Fibonacci Numbers

---

| Field | Value |
|---|---|
| **Slug** | `ctci-fibonacci-numbers` |
| **Domain** |  |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/ctci-fibonacci-numbers |

---

## Preview

Compute the n'th Fibonacci number.

## Problem Statement

*The Fibonacci Sequence*  		

The Fibonacci sequence appears in nature all around us, in the arrangement of seeds in a sunflower and the spiral of a nautilus for example.


The Fibonacci sequence begins with $fibonacci(0) = 0$ and $fibonacci(1) = 1$ as its first and second terms. After these first two elements, each subsequent element is equal to the sum of the previous two elements. 

Programmatically:
	
- $fibonacci(0) = 0$
- $fibonacci(1) = 1$
- $fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)$

		
Given $n$, return the $n^{th}$ number in the sequence.

**Example** 

$n = 5$ 


The Fibonacci sequence to $6$ is $fs = [0,1,1,2,3,5,8]$.  With zero-based indexing, $fs[5] = 5$.

**Function Description**

Complete the recursive function $fibonacci$ in the editor below. 


fibonacci has the following parameter(s):

- *int n:* the index of the sequence to return 


**Returns** 

- *int:* the $n^{th}$ element in the Fibonacci sequence

## Input Format

The integer $n$.

## Constraints

- $0 \lt n \le 30$

## Sample Tests

### Test 1

```
STDIN Function
----- --------
3 n = 3
```

### Test 2

```
2
```
