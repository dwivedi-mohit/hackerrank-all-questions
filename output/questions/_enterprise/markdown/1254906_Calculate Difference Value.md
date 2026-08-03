# Calculate Difference Value

## Metadata

- **ID:** 1254906
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Hard, Binary Search, Prefix Sum
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates binary search, prefix sums, and subsequence concepts, ideal for senior-level roles. The problem requires finding the minimum difference value when transforming one string into a subsequence of another by removing characters.

## Problem Statement

Given two strings firstString of length n and secondString of length m, the goal is to make secondString a subsequence of firstString by applying an operation any number of times.

 

Any single character can be removed from secondString in one operation. The goal is to find the minimum possible difference value, calculated as (the maximum index of all removed characters—the minimum index of all removed characters) + 1.

 

Note:

	
- Removing a character does not affect the indices of other characters.
	
- An empty string is always a subsequence of firstString.
	
- A subsequence maintains the relative positions of the remaining characters.

 

Example

n = 10, firstString = HACKERRANK 

m = 9, secondString = HACKERMAN 

 

Remove the character at index 7 to change secondString to "HACKERAN", a subsequence of firstString. The difference value is 7 - 7 + 1 = 1. Return 1.

 

Function Description 

Complete the function findDifferenceValue in the editor withs the following parameter(s):

    string firstString: the first string

    string secondString: the second string

 

Returns

    int: the difference between the maximum and minimum indices of the characters removed from secondString

 

Constraints

	
- 1 ≤ n ≤ 105

	
- 1 ≤ m ≤ 105

	
- The strings consist of uppercase English letters 'A'-'Z'.

 

Input Format for Custom Testing

The first line contains a string firstString. 

The second line contains a string secondString.

Sample Case 0

Sample Input 0

STDIN	    FUNCTION
-----	    --------
ABACABA →   firstString = "ABACABA"
ABA     →   secondString = "ABA"

```

Sample Output 0

0
```

Explanation

secondString is already a subsequence of firstString. 

Sample Case 1

Sample Input 1

STDIN	    FUNCTION
-----	    --------
ABA     →   firstString = "ABA"
ABACCA  →   secondString = "ABACCA" 

```

Sample Output 1

3

```

Explanation

Remove characters at indices 4, 5, 6, and 6 - 4 + 1 = 3.

## Sample Input/Output

## Preview

Given two strings firstString of length n and secondString of length m, the go
