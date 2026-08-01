# Concave Polygon

- **Domain:** cpp
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.8127802690582959
- **Total Submissions:** 892
- **Solved Count:** 725
- **URL:** https://www.hackerrank.com/challenges/lambda-march-concave-polygon

## Problem Statement

You are given the cartesian coordinates of a set of points in a $\text{2D}$ plane (in no particular order). Each of these points is a corner point of some Polygon, $P$, which is not self-intersecting in nature. Can you determine whether or not $P$ is a [concave polygon](https://en.wikipedia.org/wiki/Concave_polygon)?

## Input Format

The first line contains an integer, $N$, denoting the number of points.		
The $N$ subsequent lines each contain $2$ space-separated integers denoting the respective $x$ and $y$ coordinates of a point.  

## Output Format

Print $\scriptsize{\texttt{YES}}$ if $P$ is a concave polygon; otherwise, print $\scriptsize{\texttt{NO}}$.

## Constraints

- $3 \le N \le 1000$
- $0 \le x,y \le 1000$

## Sample Input

0 0
0 1
1 1
1 0

## Sample Output

NO

## Explanation

The given polygon is a square, and each of its  internal angles are . As none of these are over , the polygon is not concave and we print .

Scoring

The percentage score awarded for your submission will be:

    100 - 2*(percentage of tests which you solve incorrectly)

If this value is negative, the percentage score for your submission will be 0.

So if you get half or more of the tests incorrect, your score will be a zero.
