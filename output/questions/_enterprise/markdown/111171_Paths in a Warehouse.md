# Paths in a Warehouse

## Metadata

- **ID:** 111171
- **Type:** code
- **Difficulty:** 10.0
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Dynamic Programming, Hard, Algorithms, Data Structures, Problem Solving, Theme:  Automotive, Interviewer Guidelines
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates dynamic programming, algorithms, and problem-solving concepts, ideal for senior-level roles. The problem requires calculating the number of distinct paths through a matrix representing an automotive warehouse, considering open and blocked sections.

## Problem Statement

Count the number of paths through a matrix

A forklift operator navigates products within an automotive parts warehouse. The dashboard displays a real-time map showing open and blocked sections as an n x m matrix of 1's (open) and 0's (blocked). The operator starts at the top-left corner of the map at warehouse[0][0] and aims to reach the bottom-right corner at warehouse[n-1][m-1]. Movements can only be made to the right or downward. Given the warehouse map, calculate the number of distinct paths from warehouse[0][0] to warehouse[n-1][m-1]. Return the result modulo (109+7).

 

Example

warehouse = [1, 1, 0, 1], [1, 1, 1, 1]

 

The matrix below is drawn from the warehouse array showing open and blocked sections of the warehouse. 1 indicates an open section and 0 indicates a blocked section. It is only possible to travel through open sections, so no path can go through the section at (0, 2).

 

Example
-->

There are 2 possible paths from warehouse[0][0] to warehouse[1][3] and 2 modulo (109+7) = 2.

 

Function Description 

Complete the function numPaths in the editor with the following parameter(s):

    warehouse[n][m]:  a two dimensional array of integers of n rows and m columns

 

Returns

    int: the number of paths through the matrix, modulo (109 + 7).

n &times; m matrix, a. The function must return an integer denoting the total number of possible paths from cell (0, 0) to cell (n &mdash; 1, m &mdash; 1), modulo (109 + 7).

Input Format

	
- The first line contains an integer, n, denoting the number of rows in matrix a.
	
- The second line contains an integer, m, denoting the number of columns in matrix a.
	
- Each line i of the n subsequent lines contains m space-separated integers describing the respective values of ai,0, ai,1, &hellip;, ai,m-1.

-->

 

Constraints

	
- 1 ≤ n, m ≤ 1000
	
- Each cell in matrix a contains either a 0 or a 1.

 

 DO NOT REMOVE THIS LINE-->

Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the number of rows in the matrix warehouse.

The next line contains an integer m, the number of columns in the matrix warehouse.

The next n lines each contain a string warehouse[i] where 0 ≤ i < n and |warehouse[i]| = m.

Sample Case 0

Sample Input 0

STDIN       Function
-----       --------
3       →   warehouse[][] size n=3 m=4 
4 
1 1 1 1 →   warehouse = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
1 1 1 1  
1 1 1 1 
```

Sample Output 0

10
```

Explanation 0

-->

 

There are 10 possible paths from warehouse[0][0] to warehouse[2][3] and 10 modulo (109 +7) = 10.

Sample Case 1

Sample Input 1

STDIN      Function
-----      --------
2      →   warehouse[][] size n=2 m=2
2
1 1    →   warehouse = [[1, 1], [0, 1]]
0 1      

```

Sample Output 1

1
```

Explanation 1

-->

 

There is 1 possible path from warehouse[0][0] to warehouse[1][1] and 1 modulo (109 + 7) = 1.

## Sample Input/Output

## Preview

Count the number of paths through a matrix
