# Cyber Beacon Detection

## Metadata

- **ID:** 1470786
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Greedy, Binary Search, Real-World
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, binary search, and greedy algorithm concepts, ideal for mid-level roles. The task is to determine how many nodes in a rectangular grid are completely illuminated by a beacon's signal based on given coordinates and radius.

## Problem Statement

A network security administrator has identified a rogue signal originating from coordinates (xl, yl) that illuminates nodes within a radius R. The network is represented as a rectangular grid with a bottom left coordinate (x1, y1) and a top right coordinate (x2, y2).

 

A point (x,y) is considered completely illuminated if its distance from the beacon's center is less than or equal to R.

 

Your task is to determine how many nodes in a network are completely illuminated by a beacon's signal.

 

Example

Given, x1 = 0, y1 = 0, x2 = 1, y2 = 1, xl = 0, yl = -7 and R = 8

 

 

The left image shows the network from high above. The circle represents the range of the beacon and the 3 affected nodes are large dots. The node at (1, 1) is just outside of range as shown in the close-up image on the right. The answer is 3.

The following nodes are completely illuminated

	
- (0,0)
	
- (1,0)
	
- (0,1)

Hence the answer returned is 3.

-->

 

Function Description

Complete the function beacon_signal in the editor below.

beacon_signal has the following parameters:

    int x1: the x coordinate of the bottom left corner of the rectangular network grid

   int y1: the y coordinate of the bottom left corner

   int x2: the x coordinate of the top right corner

    int y2: the y coordinate of the top right corner

    int xl: the x coordinate of the beacon

    int yl: the y coordinate of the beacon

    int R: the radius of the beacon's range

 

Returns

    long int: the number of nodes inside the rectangular grid that are completely illuminated

 

Constraints

	
- -105 ≤ x1, x2, y1, y2, xl, yl ≤ 105

	
- 1 ≤ R ≤ 109

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, x1.

The first line contains an integer, y1.

The first line contains an integer, x2.

The first line contains an integer, y2.

The first line contains an integer, xl.

The first line contains an integer, yl.

The first line contains an integer, R,.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN    Function
-----    --------
0     →  x1 = 0
0     →  y1 = 0
1     →  x2 = 1
2     →  y2 = 2
0     →  xl = 0
0     →  yl = 0
1     →  R = 1

```

Sample Output

3
```

Explanation

 

The following nodes are completely illuminated:

	
- (0,0)
	
- (1,0)
	
- (0,1)

Sample Case 1

Sample Input For Custom Testing

STDIN    Function 
-----    -------- 
0     →  x1 = 0
0     →  y1 = 0
2     →  x2 = 2
2     →  y2 = 2
0     →  xl = 0
0     →  yl = 0
3     →  R = 3 
```

Sample Output

9
```

Explanation

## Sample Input/Output

## Preview

A network security administrator has identified a rogue signal originating fro
