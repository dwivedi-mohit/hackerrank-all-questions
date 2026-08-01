# The Letter N

- **Domain:** mathematics
- **Difficulty:** Advanced
- **Max Score:** 80
- **Success Ratio:** 0.6886792452830188
- **Total Submissions:** 106
- **Solved Count:** 73
- **URL:** https://www.hackerrank.com/challenges/n-letter

## Problem Statement

Little Nina is learning to read. Her favorite letter is `N`, and she looks for it everywhere.

There is a set of $N$ points on the plane. Let's consider four different points from the set and name them $A$, $B$, $C$, and $D$ (in that order). Nina says that these four points form the letter `N` if all the following conditions are met:

1. $A$ is located strictly to the right of ray $\overrightarrow{BC}$ (in this order).
2. $D$ is located strictly to the left of ray $\overrightarrow{BC}$ (in this order).
3. Angle $\angle ABC \le 90°$ 
4. Angle $\angle BCD \le 90°$

How many `N`s can she find? We consider letters to be sets of four points, and two letters differ if the value of one or more of the points (i.e., $A, B, C$, or $D$) differs between the two corresponding sets of points. For example, if two sets of points have differing $A$ values, then they are different letters. In addition, letters that can be transformed into each other only by reversing point order are considered to be the same letter. 

## Input Format

The first line contains a single integer, $N$, denoting the number of points.		
Each line $i$ of the $N$ subsequent lines contain two space-separated integers, $x_i$ and $y_i$, describing the respective coordinates of point $(x_i, y_i)$. *No two points coincide.*

## Output Format

Print a single integer denoting the number of different `N`s.

## Constraints

- $4 \le N \le 2318$
- $-10^4 \le x_i, y_i \le 10^4$

## Sample Input

0 0
0 2
2 0
2 2

## Explanation

To make this easier to read, we'll label our points as , , , and .

There are two different letter Ns:

-

-

Sets  and  (as well as their reversed variants) don't meet conditions  and  (we get a reversed N, like the Russian letter И).

Sets  and  are reversed variants of  and , so we don't add them to our answer.
