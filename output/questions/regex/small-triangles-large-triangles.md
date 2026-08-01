# Small Triangles, Large Triangles

- **Domain:** regex
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.8866732965522484
- **Total Submissions:** 157871
- **Solved Count:** 139980
- **URL:** https://www.hackerrank.com/challenges/small-triangles-large-triangles

## Problem Statement

You are given $n$ triangles, specifically, their sides $a_i$, $b_i$ and $c_i$. Print them in the same style but sorted by their areas from the smallest one to the largest one. It is guaranteed that all the areas are different.

The best way to calculate a area of a triangle with sides $a$, $b$ and $c$ is Heron's formula:

$S = \sqrt{p \times (p-a) \times (p-b) \times (p-c)}$ where $p={\frac {a+b+c} 2}$.


## Input Format

The first line of each test file contains a single integer $n$. $n$ lines follow with three space-separated integers, $a_i$, $b_i$ and $c_i$.

## Output Format

Print exactly $n$ lines. On each line print $3$ space-separated integers, the $a_i$, $b_i$ and $c_i$ of the corresponding triangle.

## Constraints

+ $1 \leq n \leq 100$
+ $1 \leq a_i,b_i,c_i \leq 70$
+ $a_i+b_i>c_i$,$a_i+c_i>b_i$ and $b_i+c_i>a_i$

## Sample Input

3
7 24 25
5 12 13
3 4 5

## Sample Output

3 4 5
5 12 13
7 24 25

## Explanation

The area of the first triangle is . The area of the second triangle is . The area of the third triangle is . So the sorted order is the reverse one.
