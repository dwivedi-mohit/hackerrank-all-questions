# Missing Positive Integers

## Metadata

- **ID:** 1587821
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Arrays, Sorting, Binary Search
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates arrays, sorting, and binary search concepts, ideal for junior-level roles. The problem requires finding the kth smallest positive integer that does not appear in a given dataset, considering distinct values only.

## Problem Statement

You are given an integer array arr of size n, where arr[i] represents a value in a dataset.

Your task is to find the kth smallest positive integer that does not appear in the dataset.

	
- A positive integer is any integer ≥ 1.
	
- The smallest positive integer is 1.
	
- The array may contain duplicates, and the order of elements is not important.
	
- When counting missing integers, consider distinct values present in the array (duplicates don’t change what is missing).

Return the value of the kth missing positive integer (i.e., the kth smallest positive integer that is not in arr).

 

Example

Suppose n = 5, arr = [1, 4, 7, 3, 4], and k = 5.

Output: 9

 

The first five missing positive integers are [2, 5, 6, 8, 9].

The 5th smallest positive integer not in the dataset is 9.

 

Function Description

Complete the function findMissingInteger in the editor bwith the following parameter(s):

    int arr[n]: a machine learning dataset

    long k: find the kth smallest positive integer that is not present in the dataset

 

Returns

    long: the kth smallest positive integer that is not in the dataset

 

Constraints

	
- 1 ≤ n ≤ 2 * 105

	
- 1 ≤ arr[i] ≤ 109

	
- 1 ≤ k ≤ 1012

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer n, the number of elements in arr.

Each of the next n lines contains an integer arr[i].

The next line contains an integer k.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
4        →    arr[] size n = 4
4        →    arr = [4, 2, 7, 5]
2
7
5
7        →    k = 7
```

Sample Output

11
```

Explanation

The first seven missing positive integers are [1, 3, 6, 8, 9, 10, 11].

Sample Case 1

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
6        →    arr[] size n = 6
2        →    arr = [2, 5, 7, 15, 5, 13]
5
7
15
5
13
6        →    k = 6
```

Sample Output

9
```

Explanation

The first six missing positive integers are [1, 3, 4, 6, 8, 9].

## Sample Input/Output

## Preview

You are given an integer array arr of size n, where arr[i] represents a value
