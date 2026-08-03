# River Records

## Metadata

- **ID:** 832718
- **Type:** code
- **Difficulty:** 9.444444444444445
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Algorithms, Arrays, Problem Solving, Easy
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates algorithms, arrays, and problem-solving concepts, ideal for junior-level roles. The problem requires determining the maximum rise in river water levels recorded in an array, ensuring earlier readings are strictly lower than later ones.

## Problem Statement

A meteorologist records river water levels over time in an array arr, where each value is a reading taken in chronological order.

Your task is to determine the maximum rise above a previously recorded lower level. Specifically, find the largest possible difference:

	
- arr[j] - arr[i]

subject to:

	
- 
i < j (the lower reading must occur earlier), and
	
- 
arr[i] < arr[j] (the earlier reading must be strictly smaller)

If no such pair of readings exists (i.e., no reading is higher than any earlier reading), return -1.

 

Example 1

Suppose arr = [5, 3, 6, 7, 4].

Output: 4

 

Explanation:

There are no earlier elements than arr[0].

There is no earlier reading with a value lower than arr[1].

There are two lower earlier readings with a value lower than arr[2] = 6:

	
- 
arr[2] - arr[1] = 6 - 3 = 3
	
- 
arr[2] - arr[0] = 6 - 5 = 1

There are three lower earlier readings with a lower value than arr[3] = 7:

	
- 
arr[3] - arr[2] = 7 - 6 = 1
	
- 
arr[3] - arr[1] = 7 - 3 = 4
	
- 
arr[3] - arr[0] = 7 - 5 = 2

There is one lower earlier reading with a lower value than arr[4] = 4:

	
- 
arr[4] - arr[1] = 4 - 3 = 1

 

Example 2

Suppose arr = [4, 3, 2, 1].

Output: -1

 

No item in arr has a lower earlier reading.

 

Constraints

	
- 1 ≤ size of arr[] ≤ 2 × 105

	
- −106 ≤ arr[i] ≤ 106  and  0 ≤ i < n

Test Case Input Format

The first line contains the integer n, the size of arr[].

The next n lines contain an integer element of arr[].

## Sample Input/Output

## Preview

A meteorologist records river water levels over time in an array arr, where eac
