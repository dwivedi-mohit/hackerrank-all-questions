# Subsequence Removal

## Metadata

- **ID:** 712515
- **Type:** code
- **Difficulty:** 8.333333333333334
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Algorithms, Hash Map
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, algorithms, and hash map concepts, ideal for mid-level roles. The task is to find the minimum length ascending subsequence that, when removed, leaves only unique integers in the array.

## Problem Statement

Given an array of positive integers, find the minimum length ascending subsequence such that after removing this subsequence from the array, the remaining array contains only unique integers.

 

Only one subsequence will have the minimum length (no ties). If there is no such subsequence, return [-1].

 

Example

n = 7

arr = [2, 1, 3, 1, 4, 1, 3]

 

After removing the subsequence [1, 1, 3], the remaining array of distinct integers is [2, 3, 4, 1]. The subsequence [1, 1, 3] is the shortest ascending subsequence with this property, so it is returned.

 

Function Description

Complete the function findSubsequence in the editor with the following parameters:

      int arr[n]: an array of positive integers

 

Returns

    int[]: Return the minimum length ascending subsequence, if it exists. If no such subsequence exists, return an array containing a single integer, [-1].

 

Constraints

	
- 1 ≤ n ≤ 105

	
- 1 ≤ arr[i] ≤ 106

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, the number of elements in the array arr.

Each of the next n lines contains an integer, arr[i].

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN     Function 
-----     -------- 
4    →    arr[] size n = 4 
1    →    arr[] = [1, 1, 1, 3]
1
1
3

```

Sample Output

1 
1

```

Explanation

The input array is [1, 1, 1, 3]. After removing the subsequence [1, 1], the remaining array is [1, 3] which contains only unique integers. There is no shorter subsequence with that property.

Sample Case 1

Sample Input For Custom Testing

STDIN     Function
-----     --------
5    →    arr[] size n = 5
3    →    arr[] = [3, 2, 2, 1, 1]
2 
2 
1 
1

```

Sample Output

-1
```

Explanation

The input array is [3, 2, 2, 1, 1]. The example does not contain any ascending subsequence such that after removing it, the array contains only unique integers.

## Sample Input/Output

## Preview

Given an array of positive integers, find the minimum length ascending subsequ
