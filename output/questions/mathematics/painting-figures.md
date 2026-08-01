# Painting Figures

- **Domain:** mathematics
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.6666666666666666
- **Total Submissions:** 63
- **Solved Count:** 42
- **URL:** https://www.hackerrank.com/challenges/painting-figures

## Problem Statement

Carl is an abstract artist painting $n$ figures. Each figure $i$ is described as a segment on a plane with ends in $(x_{1}, y_{1})$ and $(x_{2}, y_{2})$ having radius $r$; this means every point with a distance $\le r$ from the segment is part of figure $i$. Carl wants to make sure he has enough paint for all the figures, so he wants to know the *total area* they will cover.

Given the locations for all the figures, find and print a real number denoting the total area covered by all $n$ figures with an absolute or relative error of *at most* $10^{-6}$.

## Input Format

The first line contains single integer, $n$, denoting the number of figures.		
Each line $i$ of the $n$ subsequent lines contains five space-separated integers describing the respective values of $x_{1}$, $y_{1}$, $x_{2}$, $y_{2}$, and $r$ for figure $i$. 

## Output Format

Print a real number denoting the total area covered by all $n$ figures with an absolute or relative error of *at most* $10^{-6}$.

## Constraints

+ $1 \le n \le 200$
- $0 \le |x_{1}|, |y_{1}|, |x_{2}|, |y_{2}|, r \le 10^3$. 
- It's guaranteed that each segment's length and $r$ values are positive.

## Sample Input

2
0 1 1 1 1
1 1 1 0 1

## Sample Output

6.9269908170

## Explanation

The diagram below depicts the locations of the two figures on the canvas:

We then calculate the total area covered, which is , and print it as our answer.
