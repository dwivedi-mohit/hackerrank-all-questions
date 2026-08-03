# Biological Hazards

## Metadata

- **ID:** 561215
- **Type:** code
- **Difficulty:** 9.722222222222221
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Algorithms, Hard, Problem Solving, Theme:  Healthcare, Arrays, Binary Search
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates algorithms, problem solving, and binary search concepts, ideal for senior-level roles. The problem requires determining the number of valid intervals of bacteria samples that can coexist without any poisonous relationships.

## Problem Statement

A researcher is studying how bacteria interact when placed next to each other in a row. Some bacteria are poisonous to others, meaning they cannot coexist in the same interval of samples. These poisonous relationships are one-way: if one bacterium is toxic to another, the reverse is not assumed unless explicitly stated.

 

The goal is to determine how many intervals within the row contain only bacteria that can coexist peacefully.

 

Inputs

	
- 
`n`: the total number of samples, arranged consecutively and labeled from 1 to `n`

	
- 
`m`: the number of poisonous relationships
	
- two lists of length `m`:
	
		
- 
`vulnerable_bacteria`: each entry identifies the bacterium that is harmed
		
- 
`toxic_bacteria`: each entry identifies the bacterium that causes the harm
	
	

 

Example: if `toxic_bacteria[i] = 3` and `vulnerable_bacteria[i] = 2`, then bacterium 3 is poisonous to bacterium 2.

Output

	
- the total number of valid intervals, where a valid interval is a contiguous sequence of samples that does not contain any pair of bacteria in a poisonous relationship

 

Example 1

Input: n = 3, m = 3, `vulnerable_bacteria` = [2, 1, 3], `toxic_bacteria` = [3, 3, 1]

Output: 4

	
- Relationship interpretation:
	
		
- 
`toxic_bacteria`[0] → `vulnerable_bacteria`[0]: Bacteria 3 is poisonous to Bacteria 2
		
- 
`toxic_bacteria`[1] → `vulnerable_bacteria`[1]: Bacteria 3 is poisonous to Bacteria 1
		
- 
`toxic_bacteria`[2] → `vulnerable_bacteria`[2]: Bacteria 1 is poisonous to Bacteria 3
	
	
	
- The bacteria are arranged as: 1 2 3
	
- All possible intervals are: (1), (2), (3), (1, 2), (2, 3), (1, 2, 3)
	
- No intervals can contain bacteria 1 and 3 or bacteria 2 and 3.
	
- Valid intervals are: (1), (2), (3), (1, 2)

Example 2

Input: n = 4, m = 2, `vulnerable_bacteria` = [1, 2], `toxic_bacteria` = [3, 4]

Output: 7

Explanation:

	
- The bacteria are arranged as: 1 2 3 4
	
- All possible intervals are: (1), (2), (3), (4), (1, 2), (2, 3), (3, 4), (1, 2, 3), (2, 3, 4), (1, 2, 3, 4)
	
- No intervals can contain bacteria 1 and 3 or bacteria 2 and 4.
	
- Valid intervals are: (1), (2), (3), (4), (1, 2), (2, 3), (3, 4).

 

Constraints

	
- 1 ≤ n ≤ 105

	
- 1 ≤ m ≤ 106

	
- 1 ≤ `vulnerable_bacteria`[i], `toxic_bacteria`[i] ≤ n

 

 DO NOT REMOVE THIS LINE-->

Test Case Input Format

The first line contains an integer, n.

The second line contains an integer, m, the number of elements in `vulnerable_bacteria`.

Each of the next m lines contains an integer, `vulnerable_bacteria`[i].

The next line again repeats, m, now the number of elements in `toxic_bacteria`.

Each of the next m lines contains an integer, `toxic_bacteria`[i].

## Sample Input/Output

## Preview

A researcher is studying how bacteria interact when placed next to each other
