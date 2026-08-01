# Closest Numbers

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 100
- **Success Ratio:** 0.969576314446146
- **Total Submissions:** 9795
- **Solved Count:** 9497
- **URL:** https://www.hackerrank.com/challenges/three-month-preparation-kit-closest-numbers

## Problem Statement

Sorting is useful as the first step in many different tasks. The most common task is to make finding things easier, but there are other uses as well.  In this case, it will make it easier to determine which pair or pairs of elements have the smallest absolute difference between them.

**Example**   
$arr = [5, 2, 3, 4, 1]$   

Sorted, $arr' = [1, 2, 3, 4, 5]$.  Several pairs have the minimum difference of $1$: $[(1,2), (2,3), (3,4), (4,5)]$.  Return the array $[1,2,2,3,3,4,4,5]$.

**Note**  
As shown in the example, pairs may overlap.  

Given a list of unsorted integers, $arr$, find the pair of elements that have the smallest absolute difference between them. If there are multiple pairs, find them all.

**Function Description**  

Complete the *closestNumbers* function in the editor below.   

closestNumbers has the following parameter(s):  

- *int arr[n]:* an array of integers   

**Returns**  
- *int[]:* an array of integers as described   

## Input Format

The first line contains a single integer $n$, the length of $arr$.  
The second line contains $n$ space-separated integers, $arr[i]$.


## Output Format

**Sample Input 0**

    10
    -20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 


**Sample Output 0**

	-20 30


**Explanation 0**  
_(30) - (-20) = 50_, which is the smallest difference.  


**Sample Input 1**

    12
    -20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 -520 -470 


**Sample Output 1**

	-520 -470 -20 30


**Explanation 1**  
_(-470) - (-520) = 30 - (-20) = 50_, which is the smallest difference. 

**Sample Input 2**

    4
    5 4 3 2


**Sample Output 2**

	2 3 3 4 4 5


**Explanation 2**  
Here, the minimum difference is _1_. Valid pairs are _(2, 3)_, _(3, 4)_, and _(4, 5)_.  

## Constraints

- $2 \le n \le 200000$
- $-10^7 \le arr[i] \le 10^7$
- All $a[i]$ are unique in $arr$.


## Sample Input

10
-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854

## Sample Output

-20 30

## Explanation

(30) - (-20) = 50, which is the smallest difference.
