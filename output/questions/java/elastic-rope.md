# Elastic rope

- **Domain:** java
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.6788990825688074
- **Total Submissions:** 109
- **Solved Count:** 74
- **URL:** https://www.hackerrank.com/challenges/elastic-rope

## Problem Statement

There is an obstacle on a 2D plane in the form of a simple polygon with vertices at points $(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)$. Vertex $a$ connects with vertex $b$ via a rope. Each point on the rope is outside the polygon, but the points can be on the boundary. The rope is *elastic*, meaning it always tries to minimize its length and the friction force between the obstacle and the rope is zero. The ends of the rope are fixed at points $(x_a, y_a)$ and $(x_b, y_b)$ and no other point on the rope is fixed.

If the shape of the rope is a line that has never intersects with or overlaps itself, what's the _maximum_ possible length of the rope? 

## Input Format

The first line contains three space-separated integers describing the respective values of $n$, $a$, and $b$.		
Each line $i$ of the $n$ subsequent lines contains two space-separated integers denoting the respective values of $x_i$ and $y_i$ corresponding to the polygon's vertices in clockwise or counterclockwise order. 

## Output Format

Print a single floating-point number denoting the maximum possible length of the rope. The answer is considered to be correct if it has an *absolute* error of *at most* $10^{-6}$.

**Sample Input 0**

    4 2 4
    100 100
    200 100
    200 200
    100 200

**Sample Output 0**

	200

**Explanation 0**			
In the diagram below, the red line depicts the rope:		
![sample1.png](https://s3.amazonaws.com/hr-challenge-images/23835/1471029864-8313d0e7df-sample1.png)

**Sample Input 1**		

    6 4 1
    167 84
    421 84
    283 192
    433 298
    164 275
    320 133


**Sample Output 1**		

	468.3361845326

**Explanation 1**			
In the diagram below, the red line depicts the rope:		
![sample2.png](https://s3.amazonaws.com/hr-challenge-images/23835/1471029898-57eb4626a4-sample2.png)

## Constraints

* $3 \le n \le 500$
* $1 \le x_i, y_i \le 500$
- $1 \le a, b \le n$
- $a \ne b$
- It's guaranteed that the input polygon is simple.

## Sample Input

4 2 4
100 100
200 100
200 200
100 200

## Sample Output

200

## Explanation

In the diagram below, the red line depicts the rope:
