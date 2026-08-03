# String Chains

## Metadata

- **ID:** 116345
- **Type:** code
- **Difficulty:** 9.444444444444445
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Strings, Data Structures, Hard, Algorithms, Depth First Search, Problem Solving, Interviewer Guidelines, Hash Map
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, string manipulation, and dynamic programming concepts, ideal for senior-level roles. The problem requires determining the longest string chain achievable from a given dictionary of words by removing one character at a time.

## Problem Statement

Find the maximum number of chained character removals whose resultant string is in the set of words.

You are given an array of words representing a dictionary. A string chain is formed by taking a word and removing one character at a time, with each resulting word also being present in the dictionary.

 

Determine the longest string chain achievable for the given dictionary.

 

Example

n = 4

words = ["a", "and", "an", "bear"]:

	
- "and" can be reduced to "an" (length 2) and then to "a" (length 3)
	
- "an" can be reduced to "a" (length 2)
	
- "a" cannot be reduced further (length 1)
	
- "bear" cannot be reduced to form a chain (length 1)

The longest string chain has a length of 3.

 

Function Description

Complete the function longestChain in the editor with the following parameter(s):

    string words[n]: the strings to test

 

Returns

    int: the length of the longest string chain

 

Constraints

	
- 1 ≤ n ≤ 50000
	
- 1 ≤ length of words[i] ≤ 60, where 0 ≤ i < n

	
- Each words[i] is composed of lowercase letters in the range ascii[a-z].

 

Input Format for Custom Testing

The first line contains an integer n, the size of the words array.

The next n lines each contain a value, words[i], where 0 ≤ i < n.

Sample Case 0

Sample Input 0

STDIN      Function
-----      --------
6      →   words[] size n = 6
a      →   arr = ['a', 'b', 'ba', 'bca', 'bda', 'bdca']
b
ba
bca
bda
bdca
```

 

Sample Output 0

4
```

 

Explanation 0

	
- Since "a" and "b" are single-character words, they cannot be reduced. That would result in the empty string, so the length for both of these string chains is 1.
	
- The word "ba" can create two different string chains each with a length of 2: ("ba" → "a" and "ba" → "b"). This means the current longest string chain is 2.
	
- The word "bca" can create two different string chains of length 3: ("bca" → "ba" → "a" and "bca" → "ba" → "b"). This means the current longest string chain is now 3.
	
- The word "bda" can create two different string chains of length 3: ("bda" → "ba" → "a" and "bda" → "ba" → "b"). At this point, the current longest string chain is still 3.
	
- The word "bdca" can create four different string chains of length: 4 ("bdca" → "bda" → "ba" → "a", "bdca" → "bda" → "ba" → "b", "bdca" → "bca" → "ba" → "a", and "bdca" → "bca" → "ba" → "b"). The current longest string chain is now 4.

 

The longest string chain is 4.

## Sample Input/Output

## Preview

Find the maximum number of chained character removals whose resultant string i
