# Compute the Perimeter of a Polygon

- **Domain:** cpp
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9766660075143365
- **Total Submissions:** 5057
- **Solved Count:** 4939
- **URL:** https://www.hackerrank.com/challenges/lambda-march-compute-the-perimeter-of-a-polygon

## Problem Statement

You are given the cartesian coordinates of a set of points in a $\text{2D}$ plane. When traversed sequentially, these points form a Polygon, $P$, which is not self-intersecting in nature. Can you compute the perimeter of polygon $P$? 


## Input Format

The first line contains an integer, $N$, denoting the number of points.		
The $N$ subsequent lines each contain $2$ space-separated integers denoting the respective $x$ and $y$ coordinates of a point.  

## Output Format

For each test case, print the perimeter of $P$ (correct to a scale of one decimal place). 

**Note:** Do not add any leading/trailing spaces or units.

## Constraints

- No $2$ points are *coincident*, and polygon $P$ is obtained by traversing the points in a clockwise direction.
- $3 \le N \le 1000$    
- $0 \le x,y \le 1000$

## Sample Input

0 0
0 1
1 1
1 0

## Explanation

The given polygon is a square, and each of its sides are  unit in length. , so we print  on a new line.
