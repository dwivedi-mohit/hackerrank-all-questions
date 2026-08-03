# Wave Generation

## Metadata

- **ID:** 1249571
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Hard, Dynamic Programming, Prefix Sum
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates dynamic programming, arrays, and problem-solving concepts, ideal for senior-level roles. The problem requires determining the number of ways to replace -1s in an array to form a wave pattern, returning the result modulo (10^9 + 7).

## Problem Statement

The physicists in Hackerland are developing an algorithm to generate wave patterns. An array is considered to form a wave if it satisfies one of these conditions:

	
- Elements alternate as: a[1] > a[2] < a[3] > a[4] < a[5]... 
	
- Elements alternate as: a[1] < a[2] > a[3] < a[4] > a[5]... 

 

Given an array arr of n integers, where values are either within the range 1 to m inclusive or -1, determine how many ways you can replace all the -1s in the array with integers from 1 to m such that the resulting array forms a wave. Return the result modulo (109 + 7).

 

Example

Suppose n = 3, arr = [-1, 3, -1], m = 3

The possible ways to replace all -1s in the array such that the resulting array is a wave array are-

	
- [1, 3, 2]
	
- [1, 3, 1]
	
- [2, 3, 1]
	
- [2, 3, 2]

Hence the answer is 4.

 

Function Description

Complete the function countWaysToCreateWave in the editor with the following parameters:

    arr[n]:  an array of integers

    m: an integer

 

Returns

    int: the number of ways to replace -1s in the array to make it a wave array, modulo (109 + 7).

 

Constraints

	
- 3 ≤ n ≤ 2500
	
- 1 ≤ m ≤ 2500
	
- 
arr[i]  = -1 or 1 ≤ arr[i] ≤ m

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, denoting the number of elements in arr.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing arr[i].

The last line contains an integer, m.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
4        →    n = 4
-1       →    arr = [-1, -1, 2, -1]
-1
2
-1
3        →    m = 3 
```

Sample Output

4
```

Explanation

Given n = 4, arr = [-1, -1, 2, -1], m = 3

Possible ways to replace all -1s are-

	
- [1, 3, 2, 3]
	
- [2, 3, 2, 3]
	
- [3, 1, 2, 1]
	
- [2, 1, 2, 1]

Hence the answer is 4.

Sample Case 1

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
5        →    n = 5
2        →    arr = [2, 3, 2, 1, -1]
3
2
1
-1
10       →    m = 10 

```

Sample Output

0
```

Explanation

Given n = 5, arr = [2, 3, 2, 1, -1], m = 10

There is no way to replace the -1 in the array such that the resulting array is a wave array. Hence the answer is 0.

## Sample Input/Output

## Preview

The physicists in Hackerland are developing an algorithm to generate wave patt
