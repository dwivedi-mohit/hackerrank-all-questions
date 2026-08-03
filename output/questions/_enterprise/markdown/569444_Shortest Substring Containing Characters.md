# Shortest Substring Containing Characters

## Metadata

- **ID:** 569444
- **Type:** code
- **Difficulty:** 9.722222222222221
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Algorithms, Strings, Data Structures, Problem Solving, Easy, Sets, Hash Map
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates algorithms, strings, and data structures concepts, ideal for junior-level roles. The problem requires finding the length of the shortest substring that contains every distinct character in a given string.

## Problem Statement

You are given a string s containing lowercase letters (a–z).

 

Your task is to find the length of the shortest substring that contains every distinct character that appears in s at least once.

 

In other words:

	
- Identify all unique letters in s

	
- Find the smallest window of s that includes all of those letters
	
- Return the length of that window

 

Example 1

Input: s = "dabbcabcd"

Output: 4

Explanation:

	
-  All characters in the string: [a, b, c, d]
	
- Two of the substrings that contain all letters are "dabbc" and "abcd".

	
- "abcd" is the shorter of the two.

Example 2

Input: s = "asdfkjeghfalawefhaef"

Output: 13

Explanation:

	
-  All characters in the string: [a, d, e, f, g, h, j, k, l, s, w]
	
- The shortest substring that contains all letters is  "sdfkjeghfalaw".

 

Constraints

	
- 1 ≤ size of s ≤ 105

	
- 
s contains letters in the range ascii[a-z]

 

Test Case Input Format

The only line contains a string, s.

## Sample Input/Output

## Preview

You are given a string s containing lowercase letters (a–z).
