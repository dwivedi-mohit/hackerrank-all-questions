# Tower 3-coloring

- **Domain:** databases
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.6774193548387096
- **Total Submissions:** 434
- **Solved Count:** 294
- **URL:** https://www.hackerrank.com/challenges/tower-3-coloring

## Problem Statement

For a given integer $n$, there is a tower built from $3^n$ blocks stacked vertically. Each of these blocks can be colored in $3$ different colors: red, green or blue. How many different colorings of the tower can be created? Two colorings are considered different if and only if there exists at least one block with different colors in the colorings. Since the result can be a huge number, apply a modulo $10^9 + 7$ on the result.

## Input Format

The first line contains a single integer $n$.  

## Output Format

In a single line print a single integer denoting the number of different colorings of tower of the height $3^n$ calculated modulo $10^9+7$.  

## Constraints

+ $1 \leq n \leq 10^9$

## Sample Input

1

## Sample Output

27

## Explanation

In the sample we have , so the tower has height . Each of these three blocks can be colored with any of  available colors, so the total number of different colorings is .
