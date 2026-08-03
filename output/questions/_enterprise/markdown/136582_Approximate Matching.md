# Approximate Matching

## Metadata

- **ID:** 136582
- **Type:** code
- **Difficulty:** 9.722222222222221
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Strings, Medium, Algorithms, Problem Solving, Interviewer Guidelines
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates string manipulation, algorithm design, and problem-solving concepts, ideal for mid-level roles. The task requires finding a substring with the highest textScore based on matching prefix and suffix conditions from given strings.

## Problem Statement

Find the substring having a maximal textScore.

Given three strings - text, prefixString, and suffixString - find:

	
- 
prefixScore: the length of the longest substring of text that matches the end of prefixString

	
- 
suffixScore: the length of the longest substring of text that matches the beginning of suffixString

The textScore is the sum of prefixScore and suffixScore. Your task is to find the substring of text that begins with the matching prefix and ends with the matching suffix, and has the highest textScore. If multiple substrings have the same highest textScore, return the alphabetically lowest one.

 

Example

text = "engine"

prefixString = "raven"

suffixString = "ginkgo"

 

For prefixScore, "en" in "engine" matches the end of "raven", so prefixScore = 2. For suffixScore, "gin" in "engine" matches the beginning of "ginkgo", so suffixScore = 3.

textScore = prefixScore + suffixScore = 2 + 3 = 5. The substring of text with the highest textScore is "engin".

 

Note: If the prefix and suffix overlap, return only the substring of text, not the combined prefix and suffix.

 

Example

text = "banana"

prefixString = "bana"

suffixString = "nana"

For prefixScore, "bana" in "banana" matches "bana", so prefixScore = 4. For suffixScore, "nana" in "banana" matches "nana", so suffixScore = 4.

textScore = prefixScore + suffixScore = 4 + 4 = 8. The substring of text with the highest textScore is "banana".

 

Function Description

Complete the calculateScore function in the editor with the following parameters:

    str text: the text to compare

    str prefixString: the prefix to match

    str suffixString: the suffix to match

 

Return

    str: the longest substring of text that begins with an ending substring of prefixString and ends with a beginning substring of suffixString as described

 

Constraints

	
- 
text, prefixString, and suffixString contain lowercase English alphabetic letters ascii[a-z] only.
	
- 
1 ≤ |text|, |prefixString|, |suffixString| ≤ 50 (Here | | means length of.)

	
- It is guaranteed that there is a substring of text that matches at least one of the following:
	
		
- One or more characters at the end of prefixString.
		
- One or more characters at the beginning of suffixString.
	
	

 

 DO NOT REMOVE THIS LINE-->

Input Format for Custom Testing

The first line contains a string text.

The next line contains a string prefixString.

The last line contains a string suffixString.

Sample Case 0

Sample Input

STDIN        Function
-----        -----
nothing   →  text = "nothing"
bruno     →  prefixString = bruno
ingenious →  suffixString = ingenious
```

 

Sample Output

nothing
```

 

Explanation

	
- 
nothing matches bruno, so prefixScore = 2
	
- nothing matches ingenious, so suffixScore = 3
	
- 
textScore = prefixScore + suffixScore = 2 + 3 = 5

The substring of text with the highest textScore begins with the prefix "no" and ends with the suffix "ing": "nothing".

 

Sample Case 1

Sample Input

STDIN    Function
-----    -----
ab   →   text = "ab"
b    →   prefixString = "b"
a    →   suffixString = "a"
```

 

Sample Output

a
```

 

Explanation

Given text = "ab", our possible substrings are sub = "a", sub = "b", and sub = "ab".

	
- 
sub = "a"

	
		
- 
prefixString = "b": The beginning of sub does not match the end of prefixString, so prefixScore = 0.
		
- 
suffixString = "a": The last character of sub matches the first character of suffixString, so suffixScore = 1.
		
- 
textScore = prefixScore + suffixScore = 0 + 1 = 1
	
	
	
- 
sub = "b"
	
		
- 
prefixString = "b": The first character of sub matches the last character of prefixString, so prefixScore = 1.
		
- 
suffixString = "a": The end of sub doesn't match the beginning of suffixString, so suffixScore = 0.
		
- 
textScore = prefixScore + suffixScore = 1 + 0 = 1
	
	
	
- 
sub = "ab"
	
		
- 
prefixString = "b": The beginning of sub does not match the end of prefixString, so prefixScore = 0.
		
- 
suffixString = "a": The last character of sub does not match the first character of suffixString, so suffixScore = 0.
		
- 
textScore = prefixScore + suffixScore = 0 + 0 = 0
	
	

 

Two of these have a textScore of 1, so return the alphabetically smaller one, "a".

## Sample Input/Output

## Preview

Find the substring having a maximal textScore.
