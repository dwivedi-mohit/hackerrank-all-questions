# Common Prefix Length

## Metadata

- **ID:** 127858
- **Type:** code
- **Difficulty:** 10.0
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Strings, Algorithms, Hard, Problem Solving
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates string manipulation, algorithms, and problem-solving concepts, ideal for senior-level roles. The problem requires calculating the sum of common prefix lengths between a string and its suffixes.

## Problem Statement

Given a string, split the string into two substrings at every possible point. The rightmost substring is a suffix, and the beginning of the string is the prefix. Determine the lengths of the common prefix between each suffix and the original string. Sum and return the lengths of the common prefixes.

 

Example

inputs = ['abcabcd']

 

Each suffix is compared to the original string.

 

	
		
			Remove to leave suffix
			Suffix
			Common Prefix
			Length
		
	
	
		
			''
			'abcabcd'
			'abcabcd'
			7
		
		
			'a'
			'bcabcd'
			''
			0
		
		
			'ab'
			'cabcd'
			''
			0
		
		
			'abc'
			'abcd'
			'abc'
			3
		
		
			'abca'
			'bcd'
			''
			0
		
		
			'abcab'
			'cd'
			''
			
			
0

			
		
		
			'abcabc'
			'd'
			''
			
			
0

			
		
	

 

The sum is 7 + 0 + 0 + 3 + 0 + 0 + 0 = 10.

 

usernameDisparity  in the editor.

	
		
			Parameters
			
			
				
					
						Name
						Type
						Description
					
					
						inputs
						String Array
						each array element is a string to be processed
					
				
			
			
		
		
			Return
			The function returns an integer array of the sums of the similarities for each test case.
		
	

-->

Function Description

Complete the function commonPrefix in the editor with the following parameter(s):

    string inputs[n]:  an array of strings

 

Returns

    int[]: the sums of the common prefix lengths for each test case

 

Constraints

1 ≤ n ≤ 10

1 ≤ length of inputs[i] ≤ 105

Each inputs[i] contains only letters in the range ascii[a-z].

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains the number of test cases n.

Each of the next n lines contains a string, inputs[i], one for each test case.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input

STDIN     Function
-----     -----
1      →  number of test cases n = 1
ababaa →  inputs = ['ababaa']

```

 

Sample Output

11

```

 

Explanation

The suffixes are ['ababaa', 'babaa', 'abaa', 'baa', 'aa', 'a']. The common prefix lengths of each of these suffixes with the original string are [6, 0, 3, 0, 1, 1], respectively, and they sum to 11.

Sample Case 1

Sample Input

STDIN     Function
-----     -----
1      →  number of test cases n = 1
aa     →  inputs = ['aa']
```

 

Sample Output

3
```

 

Explanation

 

The suffixes are ['aa', 'a']. The common prefix lengths of each of these suffixes with the original string are [2, 1]  which sum to 3.

## Sample Input/Output

## Preview

Given a string, split the string into two substrings at every possible point.
