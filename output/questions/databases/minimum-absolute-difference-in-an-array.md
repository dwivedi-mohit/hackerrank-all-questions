# Minimum Absolute Difference in an Array

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.8763970706627653
- **Total Submissions:** 180109
- **Solved Count:** 157847
- **URL:** https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array

## Problem Statement

The absolute difference is the positive difference between two values $a$ and $b$, is written $|a-b|$ or $|b-a|$ and they are equal.  If $a = 3$ and $b = 2$, $|3-2| = |2-3| = 1$. Given an array of integers, find the minimum absolute difference between any two elements in the array.  

**Example**. 
$arr=[-2,2,4]$ 

There are $3$ pairs of numbers: $[-2,2], [-2,4]$ and $[2,4]$.  The absolute differences for these pairs are $|(-2) - 2| = 4$, $|(-2)-4| = 6$ and $|2 - 4| = 2$.  The minimum absolute difference is $2$.

**Function Description**  

Complete the *minimumAbsoluteDifference* function in the editor below.  It should return an integer that represents the minimum absolute difference between any pair of elements.  

minimumAbsoluteDifference has the following parameter(s):  

- *int arr[n]:* an array of integers  

**Returns**  

- *int:*  the minimum absolute difference found

## Input Format

The first line contains a single integer $n$, the size of $arr$.		
The second line contains $n$ space-separated integers, $arr[i]$.   

## Constraints

+ $2 \le n \le 10^5$  
+ $-10^9 \le arr[i] \le 10^9$  


## Sample Input

3
3 -7 0

## Sample Output

3

## Explanation

The first line of input is the number of array elements.  The array,   There are three pairs to test: , , and . The absolute  differences are:

-

-

-

Remember that the order of values in the subtraction does not influence the result.   The smallest of these absolute differences is .
