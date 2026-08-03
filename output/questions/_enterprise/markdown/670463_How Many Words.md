# How Many Words

## Metadata

- **ID:** 670463
- **Type:** code
- **Difficulty:** 10.0
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Strings, Filtering, Problem Solving, Interviewer Guidelines, CPCE Questions
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates string manipulation, filtering, and problem-solving concepts, ideal for junior-level roles. The problem requires parsing a sentence to count valid words while excluding numeric substrings and handling punctuation.

## Problem Statement

Parse a string into words, drop any numeric substrings and count the words.

You are given a sentence and must count how many valid words it contains.

 

A valid word:

	
- Consists only of letters (a–z, A–Z)
	
- May contain hyphens, which join two letter sequences into one word
	
- May end with punctuation (., ,, ?, !), which should be removed before counting
	
- Must not contain digits or any other symbols
	
- Words are separated by one or more whitespace characters

 

Your task is to:

	
- Identify all valid words according to these rules
	
- Exclude any numeric substrings
	
- Return the total number of valid words in the sentence

 

Example 1

Suppose s = "How many eggs are in a half-dozen, 13?""

Output: 7

Explanation:

The words identified are: ["How", "many", "eggs", "are", "in", "a", "half-dozen"]

 

Note that the numeric string "13" is not counted as a word because it contains only digits, which are not in the allowed character set.

 

Example 2

Suppose s = "jds dsaf lkdf kdsa fkldsf, adsbf ldka ads? asd bfdal ds bf[l. akf dhj ds 878  dwa WE DE 7475 dsfh ds  RAMU 748 dj."

Output: 21

Explanation:

The words identified are: ["jds", "dsaf", "lkdf", "kdsa", "fkldsf", "adsbf", "ldka", "ads", "asd", "bfdal", "ds", "akf", "dhj", "ds",  "dwa", "WE", "DE", "dsfh", "ds", "RAMU", "dj"]

Not counted: ["bf[l", "878", "7475", "748"]

 

The string "bf[l" is not counted as a word because it contains '['. Others not counted contain digits.

 

Constraints

	
- 0 < length of sentence ≤ 105

## Sample Input/Output

## Preview

Parse a string into words, drop any numeric substrings and count the words.
