# Most Distant

- **Domain:** sql
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.7459110473457676
- **Total Submissions:** 6970
- **Solved Count:** 5199
- **URL:** https://www.hackerrank.com/challenges/most-distant

## Problem Statement

Keko has $N$ dots in a 2-D coordinate plane. He wants to measure the gap between the most distant two dots. To make the problem easier, Keko decided to change each dot's $x$ *or* $y$ coordinate to zero.   

Help Keko calculate the distance!

## Input Format

The first line contains an integer, $N$, the number of dots.  
The next $N$ lines each contain the integer coordinates of the dots in $(x, y)$ fashion.  

**Constraints**  
$2\leq N \leq 10^6$  
$-10^9\leq x_i,\,y_i \leq 10^9$

It is guaranteed that all dots are distinct, and either their $x$ or $y$ coordinate is equal to $0$.  


## Output Format

Print the distance between the most distant dots with an absolute error of, at most, $10^{-6}$.


## Constraints

It is guaranteed that all dots are distinct, and either their  or  coordinate is equal to .

## Sample Input

-1 0
1 0
0 1
0 -1

## Sample Output

2.000000

## Explanation

In the sample, the most distant dots are located at  and .

The distance between them is .
