# Count Between

## Metadata

- **ID:** 314967
- **Type:** code
- **Difficulty:** 9.444444444444445
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Binary Search, Data Structures, Easy, Algorithms, Arrays, Problem Solving
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates binary search, data structures, and algorithms concepts, ideal for junior-level roles. The problem requires counting elements in an array that fall within specified score ranges for multiple queries.

## Problem Statement

Determine the number of candidates a company will choose for each range of scores.

You are given an integer array arr and two integer arrays low and high of the same length, representing q range queries.

 

For each query i, count how many elements in arr have values within the inclusive range:

	
- 
low[i] ≤ arr[j] ≤ high[i]

 

Your task is to return an array result of length q, where result[i] is the count for query i.

 

Example 1

Suppoise arr = [1, 3, 5, 6, 8], low = [2], and high = [6]

Output: [3]

Explanation:

Query 0: There are 3 elements in the inclusive range [2, 6]: [3, 5, 6] so store 3 in index 0 of the return array.

 

Example 2

Suppose arr = [4, 8, 7], low = [2, 4], and high = [8, 4].

Output: [3, 1]

Explanation:

Query 0: There are 3 elements in the inclusive range [2, 8]: [4, 7, 8] so store 3 in index 0 of the return array.

Query 1: There is 1 element in the inclusive range [4, 4]: [4] so store 1 in index 1 of the return array.

 

Constraints

	
- 1 ≤ n ≤ 105

	
- 1 ≤ arr[j] ≤ 109

	
- 1 ≤ q ≤ 105

	
- 1 ≤ low[i] ≤ high[i] ≤ 109

Test Case Input Format

The first line contains the integer n.

The next n lines contain an integer element of arr[].

The next line contains the integer q.

The next q lines contain an integer element of low[].

The next line contains the integer q.

The next q lines contain an integer element of high[].

## Sample Input/Output

## Preview

Determine the number of candidates a company will choose for each range of sco
