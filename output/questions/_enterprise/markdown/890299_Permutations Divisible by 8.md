# Permutations Divisible by 8

## Metadata

- **ID:** 890299
- **Type:** code
- **Difficulty:** 9.444444444444445
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Number Theory, Math, Algorithms, Problem Solving, Hard
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates number theory, algorithms, and problem-solving concepts, ideal for senior-level roles. The problem requires determining if any permutation of a number's digits is evenly divisible by 8 for a given array of integer strings.

## Problem Statement

Determine if any permutation of a number's digits is evenly divisible by 8.

Given an array of integer strings, for each string, your task is to determine if any permutation of its digits is evenly divisible by 8. Create all possible permutations of the digits and check if at least one permutation yields a value that is divisible by 8. Return an array of strings where element i is the answer to the ith string, either "YES" or "NO".

 

Example

arr = ["123"]

	
- All permutations: p = {123, 132, 213, 231, 312, 321}
	
- Check divisibility by 8 for each:
	
		
- 123 ÷ 8 = 15 remainder 3 (not divisible)
		
- 132 ÷ 8 = 16 remainder 4 (not divisible)
		
- 213 ÷ 8 = 26 remainder 5 (not divisible)
		
- 231 ÷ 8 = 28 remainder 7 (not divisible)
		
- 312 ÷ 8 = 39 remainder 0 (divisible)
		
- 321 ÷ 8 = 40 remainder 1 (not divisible)
	
	

Since 312 is divisible by 8 (312 mod 8 = 0), the answer is ["YES"].

 

Function Description 

Complete the function checkDivisibility in the editor with the following parameter(s):

    string arr[n]:  an array of integer strings

 

Returns

    string[n]: each element i is "YES" or "NO", denoting whether a permutation of arr[i] is divisible by 8

 

Constraints

	
- 1 ≤ n ≤ 45
	
- 0 ≤ arr[i] ≤ 10110

	
- 
arr[i] contains only digits in the range [0-9]

 DO NOT REMOVE THIS LINE-->

Input Format for Custom Testing

The first line contains an integer n, the size of the array arr.

Each of the next n lines contains an integer as a string, arr[i], where 0 ≤ i < n.

Sample Case 0

Sample Input 0

STDIN   Function Parameters 
-----   -------------------
2    →  arr[] Size = 2
61   →  arr = [ 61, 75 ]
75                 

```

Sample Output 0

YES
NO

```

Explanation 0

Check the following n = 2 values:

	
- 
arr[0] = 61. The permutation p = 16 is divisible by 8 so store YES in index 0 of the return array.
	
- 
arr[1] = 75. The only permutations are p = 75 and p = 57, but neither of them is divisible by 8. Store NO in index 1 of the return array.

## Sample Input/Output

## Preview

Determine if any permutation of a number's digits is evenly divisible by 8.
