# Is Possible

## Metadata

- **ID:** 132087
- **Type:** code
- **Difficulty:** 10.0
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Recursion, Algorithms, Arrays, Graphs, Interviewer Guidelines
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates recursion, algorithms, and problem-solving concepts, ideal for junior-level roles. The problem requires determining if a pair of integers can be transformed into another pair through specified operations.

## Problem Statement

Determine if (a, b) can be converted to (c, d) through some number of operations.

You start with a pair of integers (a, b).

 

You are allowed to repeatedly perform these operations, in any order and as many times as you want:

	
- Replace the pair with (a + b, b)

	
- Replace the pair with (a, a + b)

Your task is to determine whether you can transform (a, b) into another pair (c, d) using these operations.

 

Return:

	
- "Yes" if it is possible
	
- "No" if it is not

Example 1

Suppose (a, b) = (1, 1) and (c, d) = (5, 2).

Output: "Yes"

Perform the operations (1, 1 + 1) to get (1, 2), (1 + 2, 2) to get (3, 2), and (3+2, 2) to get (5, 2). Alternatively, the first operation could be (1+1, 1) to get (2, 1) and so on. The diagram below demonstrates the example that represents the pairs as Cartesian coordinates:

 

The goal can be reached.

 

Example 2

Suppose (a, b) = (1, 2) and (c, d) = (3, 6)

Output: "No"

Two possible paths are shown. It is not possible to reach the goal.

 

Constraints

	
- 1 ≤ a, b, c, d ≤ 1000

## Sample Input/Output

## Preview

Determine if (a, b) can be converted to (c, d) through some number of operatio
