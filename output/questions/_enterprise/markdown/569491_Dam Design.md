# Dam Design

## Metadata

- **ID:** 569491
- **Type:** code
- **Difficulty:** 10.0
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Algorithms, Problem Solving, Arrays
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates algorithms, problem solving, and arrays concepts, ideal for junior-level roles. The problem requires determining the maximum height of mud segments that can be placed between walls while adhering to specific height constraints.

## Problem Statement

You are given:

	
- 
wallPositions: the positions of the walls along the stream
	
- 
wallHeights: the height of each wall at the corresponding position

Mud can be placed only in the integer positions between two walls:

	
- Each unit gap between adjacent wall positions holds one mud segment
	
- The height of a mud segment can increase or decrease by at most 1 compared to each adjacent wall or mud segment

Your task is to determine:

	
- The maximum possible height of any mud segment that can be built while following the rule above

Return 0 if there is no space between any two walls to place mud.

 

Example 1

Suppose wallPositions = [1, 2, 4, 7]  and wallHeights = [4, 6, 8, 11].

Output: 10

 

Explanation: Mud segments have heights 7, 9, and 10. They are never more than one unit higher than an adjacent segment.

 

 

 

Example 2

Suppose wallPositions = [1, 10]  and wallHeights = [1, 5].

Output: 7

 

Explanation: Adjacent mud walls are at positions 2 through 9.

 

Constraints

	
- 1 < n ≤ 105

	
- 1 ≤ wallPositions[i], wallHeights[i] ≤ 109 (where 0 ≤ i < n)

 

Test Case Input Format

The first line contains the integer n, the size of wallPositions[].

The next n lines contain an integer element of wallPositions[].

The next line contains the integer n.

The next n lines contain an integer element of wallHeights[].

## Sample Input/Output

## Preview

You are given:
