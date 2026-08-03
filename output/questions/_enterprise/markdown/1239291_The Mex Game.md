# The Mex Game

## Metadata

- **ID:** 1239291
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Sorting, Greedy Algorithms
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, sorting, and greedy algorithms concepts, ideal for junior-level roles. The problem requires determining the maximum possible MEX of an array after performing specific operations on its elements.

## Problem Statement

You are given an array arr of n integers. You may perform the following operation any number of times:

	
- Choose an index i and reduce arr[i] to any integer x such that 0 ≤ x ≤ arr[i].

The MEX (Minimum Excluded) of an array is defined as the smallest non-negative integer not present in the array.

	
- For example, the MEX of [1, 0, 3, 2, 5] is 4.
	
- The MEX of [1, 2] is 0.

Determine the maximum possible MEX that can be achieved after performing the allowed operations.

 

Example

Suppose n = 3 and arr = [3, 2, 3].

Output: 3

 

One optimal set of operations:

	
- Reduce arr[0] to 0
	
- Reduce arr[1] to 1
	
- Reduce arr[2] to 2

 

Now, arr = [0, 1, 2], and its MEX is 3, which is the maximum possible MEX.

 

Constraints

	
- 1 ≤ n ≤ 105

	
- 0 ≤ arr[i] ≤ n

Test Case Input Format

The first line contains an integer, n, the number of elements in arr.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, arr[i].

## Sample Input/Output

## Preview

You are given an array arr of n integers. You may perform the following operat
