# String Modification

## Metadata

- **ID:** 1258595
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Dynamic Programming, Hard, Strings
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates dynamic programming, string manipulation, and problem-solving concepts, ideal for senior-level roles. The problem requires calculating the minimum moves to modify a string so that every character has at least one equal adjacent character.

## Problem Statement

Modify a string of lowercase English letters ('a'-'z') by performing specific character adjustments. The goal is to transform the string so every character has at least one equal adjacent character.

 

Two types of moves can be performed on any character:

	
- Decrement by 1 (e.g., 'f' to 'e'). Note that 'a' cannot be decremented.
	
- Increment by 1 (e.g., 'f' to 'g'). Note that 'z' cannot be incremented.

 

For characters at the beginning and end of the string, which only have one adjacent character, that adjacent character must match them. Calculate the minimum number of moves required to modify the string into an acceptable form.

 

Example

 

s = "aca"

 

We can decrement 'c' twice to get "aaa". This requires a minimum of 2 moves.

 

Function Description

Complete the function getMinMoves in the editor with the following parameter(s):

    string s: the string

 

Returns

    int: the minimum moves required

 

Constraints

	
- 2 ≤ length of s ≤ 105

 

Input Format for Custom Testing

The first and only line contains a string s.

Sample Case 0

Sample Input 0

STDIN      FUNCTION
-----      --------
abab   →   s = "abab"

```

Sample Output 0

2
```

Explanation

Increment s[0] by 1 and decrement s[3] by 1 to get "bbaa".

Sample Case 1

Sample Input 1

STDIN        FUNCTION
-----        --------
abcdef  →    s = "abcdef"

```

Sample Output 1

3
```

Explanation

Increment s[0] by 1, decrement s[3] by 1, and increment s[4] by 1 to get "bbccff".

## Sample Input/Output

## Preview

Modify a string of lowercase English letters ('a'-'z') by performing specific
