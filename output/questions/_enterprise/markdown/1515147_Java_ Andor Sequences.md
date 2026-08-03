# Java: Andor Sequences

## Metadata

- **ID:** 1515147
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Bitwise Operations, Medium, Greedy, Combinatorics
- **Skills:** Java (Intermediate)
- **Languages:** j, a, v, a, ,, j, a, v, a, 1

## Summary

This coding question evaluates bitwise operations, greedy algorithms, and combinatorics concepts, ideal for mid-level roles. The problem requires finding the number of valid Andor sequences and the lexicographically maximum sequence within a specified integer range.

## Problem Statement

An "Andor" sequence is a special sequence of integers with the following properties:

	
- (arr[i] & arr[i + 1]) * 2 < arr[i] | arr[i + 1], where & and | denote bitwise AND and OR operations
	
- arr[i] < arr[i + 1]

These properties apply when the sequence has more than one element. A single element is also considered a valid Andor sequence.

 

Given two integers x and y, find:

	
- The number of different possible Andor sequences with maximum length using only integers in range [x, y], inclusive
	
- The lexicographically maximum Andor sequence in the given range

The number of sequences can be very large, so return the value modulo (109 + 7).

 

Note: Lexicographical order is like dictionary order. Array a < b if the first element where they differ satisfies a[i] < b[i]. If a is a prefix of b and b is longer, then a < b.

 

Example

x = 1

y = 4

 

Analysis of sequence [1, 3, 4]:

 

	
		
			i
			arr[i]
			arr[i + 1]
			(arr[i] & arr[i + 1]) * 2
			arr[i] | arr[i + 1]
			Valid
		
	
	
		
			0
			1
			3
			(1 & 3) * 2 = 2
			(1 | 3) = 3
			Yes
		
		
			1
			3
			4
			(3 & 4) * 2 = 0
			(3 | 4) = 7
			Yes
		
	

 

The sequence [1, 3, 4] satisfies all conditions and is an Andor sequence. Another valid sequence is [1, 2, 4].

There are 2 valid Andor sequences, and the lexicographically maximum is [1, 3, 4].

 

Function Description

Complete the function findSequences in the editor with the following parameters:

    long int x: the lower bound of the range

    long int y: the higher bound of the range

 

Returns

    Return object consists of:

	
- 
int count: the number of Andor sequences
	
- 
long[] maxSequence: the lexicographically maximum Andor sequence

 

Constraints

	
- 1 ≤ x ≤  y  ≤ 1018

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, x, denoting the lower bound of the range.

The second line contains an integer, y, denoting the higher bound of the range.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
1        →    x = 1
5        →    y = 5

```

Sample Output

4
1
3
5

```

Explanation

The different possible Andor sequences of maximum possible lengths are [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5].

The lexicographically maximum Andor sequence is [1, 3, 5].

	
		
			i
			arr[i]
			arr[i + 1]
			(arr[i] & arr[i + 1]) * 2
			arr[i] | arr[i + 1]
			Valid
		
	
	
		
			0
			1
			3
			(1 & 3) * 2 = 2
			(1 | 3) = 3
			Yes
		
		
			1
			3
			5
			(3 & 5) * 2 = 1
			(3 | 4) = 7
			Yes
		
	

 

Sample Case 1

Sample Input For Custom Testing

STDIN         FUNCTION 
-----         -------- 
2        →    x = 2
10       →    y = 10 

```

Sample Output

24
3
7
10

```

Explanation

There are 24 different possible Andor sequences that contain 3 values, the maximum length possible. The lexicographically maximum sequence is [3, 7, 10].

	
		
			i
			arr[i]
			arr[i + 1]
			(arr[i] & arr[i + 1]) * 2
			arr[i] | arr[i + 1]
			Valid
		
	
	
		
			0
			3
			7
			(3 & 7) * 2 = 6
			(3 | 7) = 7
			Yes
		
		
			1
			7
			10
			(7 & 10) * 2 = 4
			(7 | 10) = 15
			Yes

## Sample Input/Output

## Preview

An "Andor" sequence is a special sequence of integers with the following prope
