# Maximum Index

## Metadata

- **ID:** 135929
- **Type:** code
- **Difficulty:** 10.0
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Loops, Algorithms, Problem Solving, Interviewer Guidelines
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates loops, algorithms, and problem-solving concepts, ideal for junior-level roles. The problem requires determining the maximum index Jumping Jack can reach in a series of steps while avoiding a specified bad index.

## Problem Statement

Find the maximum step number that Jumping Jack can reach.

You are working with an infinite array of integers starting at index 0. A pointer begins at index 0.

 

At each step:

	
- You may move forward from index i to index i + j, or
	
- You may stay at the same index
	
- The value of j starts at 1 and increases by 1 after every step

 

There is one index, badElement, that must never be visited.

 

Given:

	
- The total number of steps steps

	
- The index to avoid badElement

Your task is to determine the maximum index that the pointer can reach within the given number of steps without ever landing on badElement.

 

Example 1

Suppose steps = 4 and badElement = 6.

Output: 9

 

The pointer is limited to 4 steps and should avoid the bad item 6.

	
- Scenario 1:
	
		
- In the first step, j starts at 1.  Move 1 unit to index 0 + 1 = 1 and j = 2.
		
- At step 2,  move 2 units to index 1 + 2 = 3, and j = 3.  
		
- At step 3, do not move.  Otherwise, the pointer will move 3 units to the bad item 6.  Now j = 4.

		
- At step 4, move 4 units to item 3 + 4 = 7. 
	
	
	
- Scenario 2:
	
		
- At step 1, remain at index 0. Now j = 2.

		
- At step 2,  move 2 units to index 0+2= 2 and j = 3. 
		
- At step 3, move 3 units to index 2+3= 5 and j = 4.
		
- At step 4, move 4 units to index 5 + 4 = 9.
	
	

 

 Example 2

Suppose steps = 3 and badElement = 3

Output: 5

 

Move 3 steps and avoid index number 3.

	
- Scenario 1:
	
		
- At step 1, move 1 unit to index 0 + 1 = 1.
		
- At step 2,  remain at index 1.  Otherwise, the pointer will move to the bad index number 3. 
		
- At step 3,  move 3 units to index 1 + 3 = 4.
	
	
	
- Scenario 2:
	
		
- At step 1, remain at index 0.
		
- At step 2,  move 2 units to index 0 + 2 = 2.  
		
- At step 3, move 3 units to index 2 + 3 = 5. 
	
	

 

Constraints

	
- 1 ≤ steps ≤ 2 × 103

	
- 1 ≤ badIndex ≤ 4 × 106

## Sample Input/Output

## Preview

Find the maximum step number that Jumping Jack can reach.
