# Left Rotation

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.924686406495994
- **Total Submissions:** 527833
- **Solved Count:** 488080
- **URL:** https://www.hackerrank.com/challenges/array-left-rotation

## Problem Statement

A $left\ rotation$ operation on a circular array shifts each of the array's elements $1$ unit to the left. The elements that fall off the left end reappear at the right end. Given an integer $d$, rotate the array that many steps to the left and return the result. 
 

**Example**  
$d=2$  
$arr = [1, 2, 3, 4, 5]$  

After $2$ rotations, $arr' = [3, 4, 5, 1, 2]$.

**Function Description**  

Complete the $rotateLeft$ function with the following parameters:  

- $int\ d$:  the amount to rotate by  
- $int\ arr[n]$: the array to rotate  

**Returns**  

- $int[n]$: the rotated array



## Input Format

The first line contains two space-separated integers that denote $n$, the number of integers, and $d$, the number of left rotations to perform. 	
The second line contains $n$ space-separated integers that describe $arr[]$.  

## Constraints

- $1 \le n \le 10^5$  
- $1 \le d \le n$  
- $1 \le a[i] \le 10^6$

## Sample Input

STDIN      Function
-----      --------
5 4         n = 5 d = 4
1 2 3 4 5  arr = [1, 2, 3, 4, 5]

## Sample Output

5 1 2 3 4

## Explanation

To perform  left rotations, the array undergoes the following sequence of changes:
