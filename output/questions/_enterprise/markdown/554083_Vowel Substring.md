# Vowel Substring

## Metadata

- **ID:** 554083
- **Type:** code
- **Difficulty:** 9.722222222222221
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Dynamic Programming, Problem Solving, Hard, Strings
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates dynamic programming, problem solving, and string manipulation concepts, ideal for senior-level roles. The problem requires determining the number of substrings containing all vowels from a given string of lowercase letters.

## Problem Statement

Given a string of lowercase letters, determine the number of substrings that contain only vowels, and each vowel appears at least once. The vowels are ['a', 'e', 'i', 'o', 'u']. A substring is a contiguous segment of a string.

 

Example 1

Input: s = "aeioaexaaeuiou"

Output: 4

Explanation:

	
- The segments of vowels include "aeioae"  and "aaeuiou". 
	
- The first segment does not include all vowels. 
	
- The second segment contains four substrings with all vowels: "aaeuiou", "aaeuio", "aeuiou", and "aeuio".

Example 2

Input: s = "aaeiouxa"

Output: 2

Explanation:

	
- The segments of vowels include "aaeiou"  and "a". 
	
- The first segment contains two substrings with all vowels: "aaeiou", "aeuio".
	
- The second segment does not include all vowels. 

 

Constraints

	
- 1 ≤ size_of s ≤ 105

	
- 
s[i] is in the range ascii['a'-'z'] (where 0 ≤ i < size_of s ) 

 

 DO NOT REMOVE THIS LINE-->

Test Case Input Format

The only line contains a string, s.

## Sample Input/Output

## Preview

Given a string of lowercase letters, determine the number of substrings that
