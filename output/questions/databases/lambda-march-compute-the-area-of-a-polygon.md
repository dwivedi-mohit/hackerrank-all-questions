# Compute the Area of a Polygon

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9483521888834235
- **Total Submissions:** 4066
- **Solved Count:** 3856
- **URL:** https://www.hackerrank.com/challenges/lambda-march-compute-the-area-of-a-polygon

## Problem Statement

You are given the cartesian coordinates of a set of points in a $\text{2D}$ plane. When traversed sequentially, these points form a Polygon, $P$, which is not self-intersecting in nature. Can you compute the area of polygon $P$?

## Input Format

The first line contains an integer, $N$, denoting the number of points.		
The $N$ subsequent lines each contain $2$ space-separated integers denoting the respective $x$ and $y$ coordinates of a point.

## Output Format

For each test case, print the area of $P$ (correct to a scale of one decimal place). 

**Note:** Do not add any leading/trailing spaces or units; it is assumed that your result is in square units.

## Constraints

- No $2$ points are *coincident*, and polygon $P$ is obtained by traversing the points in a counter-clockwise direction.
- $4 \le N \le 1000$    
- $0 \le x,y \le 1000$

## Sample Input

0 0
0 1
1 1
1 0

## Explanation

The given polygon is a square, and each of its sides are  unit in length.

, so we print  on a new line.
