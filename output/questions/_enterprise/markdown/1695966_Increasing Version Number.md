# Increasing Version Number

## Metadata

- **ID:** 1695966
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Arrays
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, loops and counters, and greedy algorithm concepts, ideal for junior-level roles. The task is to determine the minimum number of operations needed to make an array of version numbers strictly increasing.

## Problem Statement

You are given an array versionNumbers of size n, where versionNumbers[i] represents the version number of the ith application.

Your task is to determine the minimum number of operations needed to make the array strictly increasing.

In one operation:

	
- Choose an index i and increase versionNumbers[i] by i using 1-based indexing

Note:

	
- The operation may be applied to any index any number of times.
	
- After all operations, the array must satisfy:
	
		
- versionNumbers[1] < versionNumbers[2] < ... < versionNumbers[n]
	
	

Return the minimum number of operations required.

 

Example

versionNumbers = [2, 1, 3]

 

	One optimal series of operations is shown.
	
		
			 
			Current Array
			Operation on ith index (1-based)
			Updated Array
		
	
	
		
			1.
			
versionNumbers = [2, 1, 3]
			Operation on the 2nd version number
			
versionNumbers =[2, 3, 3]  (versionNumbers[2] + 2 = 3)
		
		
			2.
			
versionNumbers = [2, 3, 3]
			Operation on the 3rd version number
			
versionNumbers= [2, 3, 6]  (versionNumbers[3] + 3 = 6)
		
	

 

After 2 operations, versionNumbers[] is strictly increasing. 

 

Function Description 

Complete the function getMinimumOperations in the editor with the following parameters:

    int versionNumbers[n]: the applications' version numbers

 

Returns

    long: the minimum number of operations required to make versionNumbers[] strictly increasing

 

Constraints

	
- 1 ≤ n ≤ 2 * 105

	
- 1 ≤ versionNumbers[i] ≤ 109 

 

## Input Format for Custom Testing

The first line contains an integer n, the size of array versionNumbers.

Each of the next n lines contains an integer versionNumbers[i].

## Sample Case 0

Sample Input 0

STDIN     Function  
-----     -------- 
3     →   versionNumbers[] size n = 3 
1     →   versionNumbers = [1, 1, 4] 
1 
4

```

Sample Output 0

1
```

Explanation

	Optimal operations are shown.
	
		
			 
			Current Array
			Operation on ith index (1-based)
			Updated Array
		
	
	
		
			1.
			
versionNumbers = [1, 1, 4]
			Operation on the 2nd version number
			
versionNumbers =[1, 3, 4]  (versionNumbers[2] + 2 = 3)
		
	

## Sample Case 1

Sample Input 1

STDIN     Function  
-----     -------- 
4     →   versionNumbers[] size n = 4 
7     →   versionNumbers = [7, 8, 9, 2] 
8 
9 
2
```

Sample Output 1

2
```

Explanation

	Optimal operations are shown.
	
		
			 
			Current Array
			Operation on ith index (1-based)
			Updated Array
		
	
	
		
			1.
			
versionNumbers = [7, 8, 9, 2]
			Operation on the 4th version number
			
versionNumbers =[7, 8, 9, 6]  (versionNumbers[4] + 4 = 6)
		
		
			2.
			
versionNumbers = [7, 8, 9, 6]
			Operation on the 4th version number
			
versionNumbers= [7, 8, 9, 10] (versionNumbers[4] + 4 = 10)

## Sample Input/Output

## Preview

You are given an array versionNumbers of size n, where versionNumbers[i] repre
