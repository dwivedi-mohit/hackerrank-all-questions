# Anagram Difference

## Metadata

- **ID:** 307515
- **Type:** code
- **Difficulty:** 9.444444444444445
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Problem Solving, Algorithms, Data Structures, Strings, Medium, Interviewer Guidelines, Hash Map
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, algorithms, and string manipulation concepts, ideal for mid-level roles. The task requires determining the minimum modifications needed to make pairs of strings anagrams or returning -1 if impossible.

## Problem Statement

An anagram is a word whose characters can be rearranged to create another word. Given two strings, determine the minimum number of characters in either string that must be modified to make them anagrams. If it is not possible to make them anagrams, return -1.

 

Example

a = ["tea", "tea", "act"]

b = ["ate", "toe", "acts"]

	
- 
a[0] = "tea" and b[0] = "ate" are already anagrams, so 0 characters need modification.
	
- 
a[1] = "tea" and b[1] = "toe" need 1 character modified ('o' → 'a' or 'a' → 'o') to become anagrams.
	
- 
a[2] = "act" and b[2] = "acts" cannot become anagrams because they have different lengths, so return -1.

The answer array is [0, 1, -1].

 

Function Description

Complete the function getMinimumDifference in the editor with the following parameter(s):

    string a[n]:  an array of strings

    string b[n]:  an array of strings

 

Returns

    int[n]:  the minimum number of characters in either string that needs to be modified to make the two strings anagrams or -1 if it is not possible

 

Constraints

	
- Each string consists of lowercase characters ['a'-'z'].
	
- 1 ≤ n ≤ 100
	
- 0 ≤ |a[i]|, |b[i]| ≤ 104 where | string | means "length of string"
	
- 1 ≤ |a[i]| + |b[i]| ≤ 104

 

 DO NOT REMOVE THIS LINE-->

Input Format for Custom Testing

The first line contains an integer n, the number of strings in the array a.

The n subsequent lines each contain a string describing a[i ]where 0 ≤ i < n.

The next line contains an integer n, the number of strings in the array b.

The n subsequent lines each contain a string describing b[i] where 0 ≤ i < n.

 

Sample Case 0

 

Sample Input For Custom Testing

 

STDIN    Function
-----    --------
5    →   a[] size n = 5
a    →   a = ["a", "jk", "abb", "mn", "abc"]
jk
abb
mn
abc
5    →   b[] size n = 5
bb   →   b = ["bb", "kj", "bbc", "op", "def"]
kj
bbc
op
def

```

Sample Output

-1
0
1
2
3
```

 

Explanation

Perform the following n = 5 calculations:

	
- Index 0: "a" and "bb" cannot be anagrams because they contain different numbers of characters.
	
- Index 1: "jk" and "kj" are already anagrams because they both contain the same characters at the same frequencies.
	
- Index 2: "abb" and "bbc" differ by one character.
	
- Index 3: "mn" and "op" differ by two characters.
	
- Index 4: "abc" and "def" differ by three characters.

Return the array [-1, 0, 1, 2, 3] as the answer.

## Sample Input/Output

## Preview

An anagram is a word whose characters can be rearranged to create another word
