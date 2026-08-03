# No Pairs Allowed

## Metadata

- **ID:** 311408
- **Type:** code
- **Difficulty:** 9.444444444444445
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Strings, Easy, Algorithms, Problem Solving, Interviewer Guidelines
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates string manipulation, character replacement, and algorithmic problem-solving concepts, ideal for junior-level roles. The task is to determine the minimum number of character replacements needed to ensure no two adjacent characters in a string are the same.

## Problem Statement

Determine the minimum number of character replacements necessary such that no two adjacent characters in a string are the same.

You are given a list of words. For each word, determine the minimum number of character replacements required so that:

	
- No two adjacent characters are the same.

You may replace any character with any other character.

 

Return an array where each element represents the number of replacements needed for that word.

 

Example

Suppose words = [ "ab","aab","abb", "abab","abaaaba" ]

Output: [0, 1, 1, 0, 1]

	
- "ab": no change needed (0 changes)
	
- "aab": change one 'a' (1 change)
	
- "abb": change one 'b' (1 change)
	
- "abab": no change needed (0 changes)
	
- "abaaaba": change the middle 'a' (1 change)

Constraints

	
- 1 ≤ n ≤ 100
	
- 2 ≤ length of words[i] ≤ 105

	
- Each letter of words[i] is in the range ascii[a-z].

Test Case Input Format

The first line contains an integer n.

The next n lines contain a string element of words.

## Sample Input/Output

## Preview

Determine the minimum number of character replacements necessary such that no
