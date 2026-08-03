# Reach the End in Time

## Metadata

- **ID:** 852900
- **Type:** code
- **Difficulty:** 10.0
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Graphs, Algorithms, Problem Solving, Medium, Breadth First Search
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, breadth-first search, and algorithmic concepts, ideal for mid-level roles. The problem requires determining if a pointer can reach the bottom-right corner of a grid within a specified time limit.

## Problem Statement

A 2-D grid made up of some blocked (denoted as '#') and some unblocked (denoted as '.') cells is provided. The pointer starts in the top-left corner of the grid, which is always unblocked, and it is guaranteed that the bottom-right cell is also unblocked. Each cell can be connected to its adjacent cells on the right, left, top, and bottom (if they exist). The pointer takes 1 second to move from one cell to an adjacent cell. If the pointer can reach the bottom-right corner of the grid within the given maximum time (maxTime) seconds, return 'Yes'. Otherwise, return 'No'.

 

Example

rows = 3

grid = ['..##', '#.##', '#...']

maxTime = 5

..##
#.##
#...
```

It will take the pointer 5 seconds to reach the bottom right corner. As long as maxTime ≥ 5, return 'Yes'.

 

Function Description

Complete the function reachTheEnd in the editor withs the following parameter(s):

    string grid[r]: the rows of the grid

    int maxTime: the maximum time to complete the traversal

 

Returns:

    string: the final string; either 'Yes' or 'No'

 

Constraints

	
- 1 ≤ rows ≤ 500
	
- 0 ≤ maxTime ≤ 106

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, rows, that denotes the number of rows of the 2-D grid

In each of the next rows lines, the ith line contains a string denoting the configuration of the ith row of the grid.

The last line contains an integer, maxTime, that represents the maximum time in seconds the pointer has to reach the bottom right cell.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input

STDIN     Function
-----     -----
2      →  size of grid[] rows = 2
..     →  grid = ['..', '..']
..
3      →  maxTime = 3
```

 

Sample Output

Yes
```

 

Explanation

The grid has 2 rows and 2 columns and the time within which the pointer needs to reach the bottom-right cell is 3 seconds. Starting from the top-left cell, the pointer can either move to the top-right unblocked cell or bottom-left unblocked cell then to the bottom-right cell. It takes 2 seconds to reach the bottom-right cell on either path. Thus, the pointer reaches the bottom-right cell within the 3 seconds allowed, and 'Yes' is returned.

Sample Case 1

Sample Input

STDIN     Function
-----     -----
2      →  grid[] size rows = 2
.#     →  grid = ['.#', '#.']       
#.
2      →  maxTime = 2
```

 

Sample Output

No
```

 

Explanation

The grid has 2 rows and 2 columns and the time within which the pointer needs to reach the bottom-right cell is 2 seconds. It can neither move to the top-right cell nor to the bottom-left cell and so the pointer cannot reach the bottom-right cell, regardless of the time constraint.

## Sample Input/Output

## Preview

A 2-D grid made up of some blocked (denoted as '#') and some unblocked (denote
