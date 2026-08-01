# Equalize the Array

- **Domain:** shell
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9516500875208129
- **Total Submissions:** 187384
- **Solved Count:** 178324
- **URL:** https://www.hackerrank.com/challenges/equality-in-a-array

## Problem Statement

Given an array of integers, determine the minimum number of elements to delete to leave only elements of equal value.
  
**Example**  

$arr = [1, 2, 2, 3]$  

Delete the $2$ elements $1$ and $3$ leaving $arr = [2, 2]$. If both twos plus either the $1$ or the $3$ are deleted, it takes $3$ deletions to leave either $[3]$ or $[1]$.  The minimum number of deletions is $2$.

**Function Description**  

Complete the *equalizeArray* function in the editor below.  

equalizeArray has the following parameter(s):  

- *int arr[n]:* an array of integers   

**Returns**  

- *int:* the minimum number of deletions required  

## Input Format

The first line contains an integer $n$, the number of elements in $arr$.  		
The next line contains $n$ space-separated integers $arr[i]$.


## Constraints

- $1 \leq n \leq 100$
- $1 \le arr[i] \le 100$

## Sample Input

STDIN       Function
-----       --------
5           arr[] size n = 5
3 3 2 1 3   arr = [3, 3, 2, 1, 3]

## Explanation

Delete  and  to leave . This is minimal.  The only other options are to delete  elements to get an array of either  or .
