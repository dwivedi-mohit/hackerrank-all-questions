# Bucket Fill

## Metadata

- **ID:** 568819
- **Type:** code
- **Difficulty:** 10.0
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Problem Solving, Algorithms, Flood Fill, Theme:  E-commerce, Interviewer Guidelines
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, depth-first search, and graph traversal concepts, ideal for junior-level roles. The problem requires determining the minimum number of fill operations needed to repaint a 2D grid of colors based on connected regions.

## Problem Statement

You are given a picture represented as a 2D grid of letters, where each letter is a cell’s color.

 

A fill operation works like a bucket tool:

	
- Choose any cell
	
- Recolor all cells in its connected region
	
- A region consists of cells that:
	
		
- Have the same color
		
- Are connected horizontally or vertically (not diagonally)
	
	

Your task is to determine the minimum number of fill operations needed to completely repaint the picture.

 

Example

Suppose picture= ["aabba", "aabba", "aaacb"]

Output: 5

Explanation:

Each string represents a row of the picture, and each letter represents a cell's color. The diagram shows the 5 fills needed to repaint the picture. It takes two fills each for a and b, and one for c. The array picture is shown below.

 

 

	
- 
h and w refer to height and width of the graph.
	
- 1 ≤ h ≤ 105

	
- 1 ≤ w ≤ 105

	
- 1 ≤ h*w ≤ 105

	 -->
	
- 
length(picture[i]) = w (where 0 ≤ i < h)

	
- 
picture[i][j] is in the set  {'a', 'b', 'c'} (where 0 ≤ i < h and 0 ≤ j < w)

Test Case Input Format

The first line contains the integer n, the size of picture[].

The next n lines contain a string element of picture[].

## Sample Input/Output

## Preview

You are given a picture represented as a 2D grid of letters, where each letter
