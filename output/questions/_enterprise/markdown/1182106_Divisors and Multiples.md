# Divisors and Multiples

## Metadata

- **ID:** 1182106
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Math, Algorithms, Medium, Implementation, Interviewer Guidelines
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, arrays, and mathematical concepts, ideal for mid-level roles. The task requires counting divisors and multiples for each element in an array, returning the counts as an output array.

## Problem Statement

Given an array arr of length n, for each index i from 1 to n, count how many indices j (where j is not equal to i) satisfy either of the following conditions:

	
- 
arr[j] is a divisor of arr[i]

	
- 
arr[j] is a multiple of arr[i]

Definitions:

	
- 
x is a divisor of y if y is divisible by x (y % x = 0).
	
- 
x is a multiple of y if x is divisible by y (x % y = 0).

Return an array where the ith element represents the count for the ith element of the input array.

 

Example

arr = [1, 3, 4, 2, 6]

	 
	
		
			i
			arr[i]
			Divisors
			Multiples
			Count
		
	
	
		
			0
			1
			0
			4
			0 + 4 = 0
		
		
			1
			3
			1
			1
			1 + 1 = 2
		
		
			2
			4
			2
			0
			2 + 0 = 0
		
		
			3
			2
			1
			2
			1 + 2 = 3
		
		
			4
			6
			3
			0
			3 + 0 = 3
		
	

 

For arr[0] = 1, there are no divisors in the array, and the other 4 elements are multiples of 1. Return the counts as an array, [4, 2, 2, 3, 3].

 

Function Description

Complete the function getCount in the editor with the following parameter(s):

    int arr[n]: an array of integers

 

Returns

    int[n]: the answers at each index

 

Constraints

	
- 1 ≤ n ≤ 105

	
- 1 ≤ arr[i] ≤ 105

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, denoting the number of elements in arr.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing arr[i].

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN    FUNCTION
-----    --------
5     →  arr size n = 5
5     →  arr = [5, 2, 4, 3, 7]
2
4
3
7
```

 

Sample Output

0
1
1
0
0
```

Explanation

The number of divisors and multiples of 5, 3, and 7 are 0.

The number of divisors and multiples of 2, 4 are 1

Sample Case 1

Sample Input For Custom Testing

STDIN    FUNCTION 
-----    -------- 
4     →  arr size n = 4 
2     →  arr = [2, 4, 8, 16]
4
8
16

```

Sample Output

3
3
3
3

```

Explanation

Every element in the array is either a divisor or a multiple of another element.

## Sample Input/Output

## Preview

Given an array arr of length n, for each index i from 1 to n, count how many i
