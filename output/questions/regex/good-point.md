# Good Point

- **Domain:** regex
- **Difficulty:** Hard
- **Max Score:** 70
- **Success Ratio:** 0.7777777777777778
- **Total Submissions:** 90
- **Solved Count:** 70
- **URL:** https://www.hackerrank.com/challenges/good-point

## Problem Statement

**The scoring system for this challenge is binary. Your score is zero unless you pass all tests.**

Given $n$ *strictly convex* simple polygons and $m$ ellipses on a plane, find any point lying in their intersection. Then print two lines of output, where the first line contains the point's $x$ coordinate and the second line contains its $y$ coordinate. The point lying on the boundary of an ellipse or polygon is considered to be an *inner* point. 

## Input Format

The first line contains an integer, $n$, denoting the number of polygons.	
The next set of lines defines $n$ polygons, where each polygon $i$ is described as follows:

- The first line contains an integer, $v_i$, denoting the number of vertices in polygon $i$.
- Each of the $v_i$ subsequent lines contains two space-separated integers denoting the respective $x$ and $y$ coordinates for one of polygon $i$'s vertices. The list of vertices is given in *counterclockwise* order.		

The next line contains an integer, $m$, denoting the number of ellipses.		
Each of the $m$ subsequent lines contains five space-separated integers denoting the respective values of $x_1$, $y_1$, $x_2$, $y_2$, and $a$, which are the coordinates of the two focal points and the semi-major-axis for an [Ellipse](https://en.wikipedia.org/wiki/Ellipse).


## Output Format

Print two lines describing an $(x, y)$ point inside the intersection. The first line must be a real number denoting the point's $x$ coordinate, and the second line must be a real number denoting its $y$ coordinate. Your answer is considered to be correct if there is a point, $(x_0, y_0)$, inside the intersection such that the distance between $(x, y)$ and $(x_0, y_0)$ is *at most* $10^{-4}$.

## Constraints

- $1 \le n \le 500$
- $3 \le v_i \le 1500$
- $3 \le \sum\limits_{i=0}^{n-1} v_i \le 1500$
- $1 \le m \le 1500$
- The coordinates of points are integers in the inclusive range $[-10^4, 10^4]$.
- All semi-major-axes are integers $\le 10^4$.
- It's guaranteed that a solution exists.  
- This challenge has binary scoring.  

## Sample Input

4
0 0
2 0
2 1
0 1
3
-1 -1
5 1
0 5
1
1 2 1 4 2

## Sample Output

0.999998
1

## Explanation

The intersection consists of only one point: . As its distance to  is , this is a correct answer. Thus, we print the  coordinate, , on the first line and the  coordinate, , on the second line.
