# Array Reduction 4

## Metadata

- **ID:** 1251014
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Data Structures, Problem Solving, Hard
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates array manipulation, MEX calculation, and greedy algorithms concepts, ideal for senior-level roles. The problem requires developing an algorithm to produce the lexicographically largest array from a given integer array using specific reduction steps.

## Problem Statement

Developers are working on an array reduction algorithm that processes an array of n integers, referred to as arr, using the following steps until the array is empty:

	
- Initialize an empty array called result.
	
- Select an integer k such that 1 ≤ k ≤ length of the array arr.
	
- Append the MEX (Minimum Excluded Value) of the first k elements of arr to the result array.
	
- Remove the first k elements from arr.

Given an array arr, determine the lexicographically largest array result that can be obtained using the algorithm.

 

Definitions:

	
- An array x is lexicographically greater than an array y if either:

	
		
- At the first position where x and y differ, x[i] > y[i]

		
- |x| > |y| and y is a prefix of x where |x| denotes the length of array x.

	
	
	
- The MEX of a set of non-negative integers is the smallest non-negative integer not present in the set. For example, MEX({1,2,3}) = 0 and MEX({0,1,2,4,5}) = 3.

Example

Given n = 4, arr = [0,1,1,0], one of the optimal ways to make the array result lexicographically maximum is as follows:

	
- Take k = 2, the MEX of the 1st and 2nd elements of arr is 2. So arr = [1,0] and result = [2].
	
- Take k = 2, the MEX of the 1st and 2nd elements of arr is 2. So arr = [] and result = [2,2].

arr is now empty, and the answer is [2,2].

 

Function Description

Complete the function getMaxArray in the editor with the following parameters:

    arr[n]:  An array of integers

 

Returns

    int[]: The lexicographically maximum array result that can be obtained using the algorithm

 

Constraints

	
- 1 ≤ n ≤ 105

	
- 0 ≤ arr[i] ≤ n

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, the number of elements in arr.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, arr[i].

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
8        →    n = 8
2        →    arr = [2, 2, 3, 4, 0, 1, 2, 0] 
2 
3 
4 
0 
1 
2 
0
```

Sample Output

5
1

```

Explanation

Given n = 8, arr = [2,2,3,4,0,1,2,0]

 

	
- Take k = 6, the MEX of the first 6 elements of arr is 5. So arr = [2,0] and  result= [5].
	
- Take k = 2, the MEX of the 1st and 2nd elements of arr is 1. So arr = [] and  result = [5,1].

 

Sample Case 1

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
6        →    n = 6
0        →    arr = [0, 1, 2, 3, 4, 6]
1
2
3
4
6

```

Sample Output

5
0

```

Explanation

Given n = 6, arr = [0,1,2,3,4,6]

 

	
- Take k = 5, the MEX of the first 5 elements of arr is 5. So arr = [6] and result = [5].
	
- Take k = 2, the MEX of the 1st element of arr is 0. So arr = [] and result = [5,0].

## Sample Input/Output

## Preview

Developers are working on an array reduction algorithm that processes an array
