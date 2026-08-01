# Day 1: Quartiles

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9181246841839312
- **Total Submissions:** 63328
- **Solved Count:** 58143
- **URL:** https://www.hackerrank.com/challenges/s10-quartiles

## Problem Statement

**Objective** <br>
In this challenge, we practice calculating *quartiles*. Check out the [Tutorial](/challenges/s10-quartiles/tutorial) tab for learning materials and an instructional video!

**Task** <br>
Given an array, $arr$, of $n$ integers, calculate the respective first quartile ($Q_1$), second quartile ($Q_2$), and third quartile ($Q_3$). It is guaranteed that $Q_1$, $Q_2$, and $Q_3$ are integers.  

**Example**   
$arr = [9, 5, 7, 1, 3]$   

The sorted array is $[1, 3, 5, 7, 9]$ which has an odd number of elements.  The lower half consists of $[1, 3]$, and its median is $\frac{1+3}{2} = 2$.  The middle element is $5$ and represents the second quartile.  The upper half is $[7, 9]$ and its median is $\frac{7 + 9}{2} = 8$.  Return $[2, 5, 8]$.   

----------------

$arr = [1, 3, 5, 7]$  

The array is already sorted.  The lower half is $[1,3]$ with a median = $\frac{1 + 3}{2} = 2$.  The median of the entire array is $\frac{3 + 5}{2} = 4$, and of the upper half is $\frac{5 + 7}{2} = 6$.  Return $[2, 4,6]$.  

**Function Description**   

Complete the *quartiles* function in the editor below.  

*quartiles* has the following parameters:  

- *int arr[n]:* the values to segregate   

**Returns**  

- *int[3]:* the medians of the left half of $arr$, $arr$ in total, and the right half of $arr$.  

## Input Format

The first line contains an integer, $n$, the number of elements in $arr$. 	
The second line contains $n$ space-separated integers, each an $arr[i]$.

## Constraints

- $5 \le n \le 50$  
- $0 \lt arr[i]  \le 100$, where $arr[i]$ is the $i^{th}$ element of the array.

## Sample Input

STDIN                   Function
-----                   --------
9                       arr[] size n = 9
3 7 8 5 12 14 21 13 18  arr = [3, 7, 8, 5, 12, 14, 21, 13,18]

## Sample Output

12
16

## Explanation

. There is an odd number of elements, and the middle element, the median, is .

As there are an odd number of data points, we do not include the median (the central value in the ordered list) in either half:

  Lower half (L): 3, 5, 7, 8

  Upper half (U): 13, 14, 18, 21

Now find the quartiles:

-  is the . So, .

-  is the . So, .

-  is the . So, .
