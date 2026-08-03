# Sorted Reduction

## Metadata

- **ID:** 1185711
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Binary Search, Greedy Algorithms, Hard
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates arrays, greedy algorithms, and binary search concepts, ideal for senior-level roles. The problem requires determining the minimum number of iterations needed to sort an array using a specific algorithm involving element removal and summation.

## Problem Statement

Some developers have created a new algorithm that takes an array arr and returns a sorted array by performing the following steps:

	
- Select any two indices i and j such that 1 ≤ i, j ≤ length of arr.

	
- Remove the elements arr[i] and arr[j] from the array.
	
- Insert arr[i] + arr[j] at any position in the array.

These steps are repeated until the array is sorted. Given an array arr of n integers, determine the minimum number of iterations required to sort the array.

 

Example

Given n = 5, arr =[2, 4, 1, 3, 5].

In this case, the answer is 1.

 

Optimally, remove elements 1 and 3 from the array and add their sum, 4, just after the second element. Thus, the array becomes [2, 4, 4, 5], which is sorted. 

 

Function Description

Complete the function getMinIterations in the editor with the following parameters:

    arr[n]: an array of integers

 

Returns

    int: the minimum number of iterations required to sort the array in non-descending order

 

Constraints

	
- 1 ≤ n ≤ 2 x 105

	
- 1 ≤ arr[i] ≤ 109

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, denoting the length of the array arr.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer denoting arr[i].

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
4        →    n = 4
1        →    arr = [1, 3, 3, 4]
3
3
4

```

Sample Output

0
```

Explanation

Here n = 4, arr = [1, 3, 3, 4]. The array is already sorted.

Sample Case 1

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
6        →    n = 6
6        →    arr = [6, 5, 4, 3, 1, 2]
5
4
3
1
2

```

Sample Output

2
```

Explanation

Given n = 6, arr =[6, 5, 4, 3, 1, 2].

Optimally:

	
- We can remove 6 and 5 from the array and put their sum, 11, at the last position. The new array is [4, 3, 1, 2, 11].
	
- We can remove the first two elements, 4 and 3, from the array and add their sum, 7, to the second-to-last position. The new array is [1, 2, 7, 11], which is sorted.

## Sample Input/Output

## Preview

Some developers have created a new algorithm that takes an array arr and retur
