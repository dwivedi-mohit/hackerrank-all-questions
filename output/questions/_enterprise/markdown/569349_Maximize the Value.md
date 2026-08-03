# Maximize the Value

## Metadata

- **ID:** 569349
- **Type:** code
- **Difficulty:** 10.0
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Math, Problem Solving, Algorithms, Interviewer Guidelines
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, algorithms, and mathematical concepts, ideal for junior-level roles. The task requires rearranging an integer array to maximize a calculated value using alternating multiplication and division operations.

## Problem Statement

Given an array arr of integers, rearrange its elements to maximize a value U, which is calculated using an alternating sequence of multiplication and division.

	
- The operations always start with multiplication.
	
- Multiplication and division alternate at each step.
	
- The last operation depends on whether the array length is odd or even.

The value U is calculated as follows:

	
- If n is odd:

	
		
- U = arr[1] × arr[2] × (1 ÷ arr[3]) × arr[4] × ... × arr[n-1] × (1 ÷ arr[n])
	
	
	
- If n is even:
	
		
- U = arr[1] × arr[2] × (1 ÷ arr[3]) × arr[4] × ... × (1 ÷ arr[n-1]) × arr[n]
	
	

Among all rearrangements that produce the maximum possible value of U:

	
- Return the array with the smallest numerical (lexicographical) order.

 

Example

Suppose arr = [21, 34, 5, 7, 9]

Output: [9, 21, 5, 34, 7]

Explanation: With this arrangement, U = 9 × 21 × (1÷5) × 34 × (1÷7) = 183.6. Another order that produces the same U is [21, 9, 7, 34, 5], but [9, 21, 5, 34, 7] < [21, 9, 7, 34, 5].

 

 

Constraints

	
- 1 ≤ n ≤ 105

	
- 1 ≤ arr[i] ≤ 109

Test Case Input Format

The first line contains the integer n, the size of arr[].

The next n lines contain an integer element of arr[].

## Sample Input/Output

## Preview

Given an array arr of integers, rearrange its elements to maximize a value U,
