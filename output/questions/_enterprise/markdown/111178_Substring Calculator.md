# Substring Calculator

## Metadata

- **ID:** 111178
- **Type:** code
- **Difficulty:** 9.444444444444445
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Strings, Dynamic Programming, Data Structures, Hard, Algorithms, Problem Solving, Interviewer Guidelines
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, dynamic programming, and data structures concepts, ideal for senior-level roles. The problem requires counting the number of distinct substrings that can be derived from a given string.

## Problem Statement

Find the number of substrings.

Count the number of distinct substrings that can be derived from a given string.

 

Given a string s, a substring is defined as a non-empty string that can be obtained by:

	
- Removing zero or more characters from the left side of s

	
- Removing zero or more characters from the right side of s

	
- Removing zero or more characters from both the left and right sides of s

 

Example

s = "abc"

 

The distinct substrings are:

	
- "abc"
	
- "ab"
	
- "bc"
	
- "a"
	
- "b"
	
- "c"

Return 6.

 

Function Description 

Complete the function substringCalculator in the editor with the following parameter(s):

    string s:  the string to analyze

 

Returns

    int: the number of distinct substrings of string s

Constraints

	
- String s consists of lowercase English letters.
	
- 0 ≤ length of s ≤ 105

 

 DO NOT REMOVE THIS LINE-->

Input Format for Custom Testing

A single line with string s.

Sample Case 0

Sample Input 0

kincenvizh
```

Sample Output 0

53
```

Explanation 0

The distinct substrings are:

	
- "kincenvizh"
	
- "kincenviz"
	
- "kincenvi"
	
- "kincenv"
	
- "kincen"
	
- "kince"
	
- "kinc"
	
- "kin"
	
- "ki"
	
- "k"
	
- "incenvizh"
	
- "incenviz"
	
- "incenvi"
	
- "incenv"
	
- "incen"
	
- "ince"
	
- "inc"
	
- "in"
	
- "i"
	
- "ncenvizh"
	
- "ncenviz"
	
- "ncenvi"
	
- "ncenv"
	
- "ncen"
	
- "nce"
	
- "nc"
	
- "n"
	
- "cenvizh"
	
- "cenviz"
	
- "cenvi"
	
- "cenv"
	
- "cen"
	
- "ce"
	
- "c"
	
- "envizh"
	
- "enviz"
	
- "envi"
	
- "env"
	
- "en"
	
- "e"
	
- "nvizh"
	
- "nviz"
	
- "nvi"
	
- "nv"
	
- "vizh"
	
- "viz"
	
- "vi"
	
- "v"
	
- "izh"
	
- "iz"
	
- "zh"
	
- "z"
	
- "h"

## Sample Input/Output

## Preview

Find the number of substrings.
