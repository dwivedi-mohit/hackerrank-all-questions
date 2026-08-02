# Lily's Homework

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.8248045486851457
- **Total Submissions:** 2814
- **Solved Count:** 2321
- **URL:** https://www.hackerrank.com/challenges/three-month-preparation-kit-lilys-homework

## Problem Statement

Whenever George asks Lily to hang out, she's busy doing homework. George wants to help her finish it faster, but he's in over his head! Can you help George understand Lily's homework so she can hang out with him?

Consider an array of $n$ distinct integers, $arr = [a[0], a[1], \ldots, a[n-1]]$. George can swap any two elements of the array any number of times. An array is *beautiful* if the sum of $|arr[i] - arr[i-1]|$ among $0 < i \lt n$ is minimal.

Given the array $arr$, determine and return the minimum number of swaps that should be performed in order to make the array *beautiful*.

**Example**   

$arr = [7, 15, 12, 3]$   

One minimal array is $[3, 7, 12, 15]$.  To get there, George performed the following swaps:

<pre>
	Swap      Result
    	  [7, 15, 12, 3]
	3 7   [3, 15, 12, 7]
    7 15  [3, 7, 12, 15]
   </pre>
    
It took $2$ swaps to make the array beautiful. This is minimal among the choices of beautiful arrays possible.

**Function Description**  

Complete the *lilysHomework* function in the editor below.   

lilysHomework has the following parameter(s):  

- *int arr[n]:* an integer array   

**Returns**  

- *int:* the minimum number of swaps required   

## Input Format

The first line contains a single integer, $n$, the number of elements in $arr$.	
The second line contains $n$ space-separated integers, $arr[i]$.

## Constraints

- $1 \le n \le 10^5$
- $1 \le arr[i] \le 2 \times 10^9$

## Sample Input

STDIN       Function
-----       --------
4           arr[]size n = 4
2 5 3 1     arr = [2, 5, 3, 1]

## Explanation

Define  to be the beautiful reordering of .  The sum of the absolute values of differences between its adjacent elements is minimal among all permutations and only two swaps ( with  and then  with ) were performed.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
