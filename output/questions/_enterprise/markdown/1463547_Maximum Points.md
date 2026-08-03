# Maximum Points

## Metadata

- **ID:** 1463547
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Arrays, Easy, Greedy Algorithms, Real-World
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, dynamic programming, and greedy algorithms concepts, ideal for junior-level roles. The problem requires determining the optimal starting position on a game board to maximize points accumulated through specified jumps.

## Problem Statement

You are given a game board with spaces arranged in a straight line, each space worth a different number of points, either positive or negative. The goal of the game is to accumulate as many points as possible.

 

Your game piece can start at any point on the board, and it can jump exactly k number of spaces at a time, only moving to the right, accumulating the number of points written on each space your piece lands on. Once your piece jumps past the final space, the game ends.

 

Given a game board, and a jump length, choose the ideal starting space to maximize the number of points gained. Return the total points.

 

Example

Suppose game_val = [2, -3, 4, 6, 1] and k = 2.

Output: 7

 

 

Constraints

	
- 1 ≤ size of game_val ≤ 106 
	
- -103 ≤ game_val[i] ≤ 103

	
- 1 ≤ k ≤ size of game_val 

Test Case Input Format

The first line contains the integer n, the size of game_val[].

The next n lines contain an integer element of game_val[].

The last line contains the integer k.

## Sample Input/Output

## Preview

You are given a game board with spaces arranged in a straight line, each space
