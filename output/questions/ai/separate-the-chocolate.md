# Separate the chocolate

- **Domain:** ai
- **Difficulty:** Expert
- **Max Score:** 250
- **Success Ratio:** 0.732108687332568
- **Total Submissions:** 2613
- **Solved Count:** 1913
- **URL:** https://www.hackerrank.com/challenges/separate-the-chocolate

## Problem Statement

[Chinese Version](https://hr-testcases.s3.amazonaws.com/1776/1776-chinese.md)<br/>
[Russian Version](https://hr-testcases.s3.amazonaws.com/1776/1776_rus.md)<br/>

Tom and Derpina have a rectangular shaped chocolate bar with chocolates labeled T, D and U. They want to split the bar into exactly two pieces such that:

* Tom's piece can not contain any chocolate labeled D and similarly, Derpina's piece can not contain any chocolate labeled T and U can be used by either of the two.  
* All chocolates in each piece must be connected (two chocolates are connected if they share an edge), i.e. the chocolates should form one connected component
* The absolute difference between the number of chocolates in pieces should be at most K
* After dividing it into exactly two pieces, in any piece, there should not be 4 adjacent chocolates that form a square, i.e. there should not be a fragment like this:  
    XX  
    XX


## Input Format

The first line of the input contains 3 integers M, N and K separated by a single space.  
M lines follow, each of which contains N characters. 
Each character is 'T','D' or 'U'.


## Output Format

A single line containing the number of ways to divide the chocolate bar.


## Constraints

0≤ M, N ≤8   
0≤ K ≤ M * N


## Sample Input

2 2 4
UU
UU

## Explanation

Note: In the explanation T and D are used to represent, which parts belong to Tom and Derpina respectively.
There are 24 = 16 possible separations.  The 4 invalid are:

TT
TT

DD
DD

DT
TD

TD
DT

Some of the valid ones are:

TD
TD

TT
DD

DD
TT

DT
DT
