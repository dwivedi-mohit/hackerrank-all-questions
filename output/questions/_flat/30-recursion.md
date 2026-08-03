# Day 9: Recursion 3  

---

| Field | Value |
|---|---|
| **Slug** | `30-recursion` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/30-recursion |

---

## Preview

Use recursion to compute the factorial of number.

## Problem Statement

**Objective**	
Today, we are learning about an algorithmic concept called *recursion*. Check out the [Tutorial](/challenges/30-recursion/tutorial) tab for learning materials and an instructional video.

**Recursive Method for Calculating Factorial**	
$$factorial(N) = \begin{cases}1 &N \le 1\\N \times factorial(N - 1) &otherwise\end{cases}$$

**Function Description**	
Complete the *factorial* function in the editor below.  Be sure to use recursion. 


*factorial* has the following paramter:


- *int n:* an integer


**Returns**


- *int:* the factorial of $n$



**Note:** If you fail to use recursion or fail to name your recursive function *factorial* or *Factorial*, you will get a score of $0$.

## Input Format

A single integer, $n$ (the argument to pass to *factorial*).

## Constraints

- $2 \le n \le 12$
- Your submission must contain a recursive function named *factorial*.

## Sample Tests

### Test 1

```
3
```

### Test 2

```
6
```
