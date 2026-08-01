# Java Subarray

- **Domain:** regex
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9723974441862226
- **Total Submissions:** 171687
- **Solved Count:** 166948
- **URL:** https://www.hackerrank.com/challenges/java-negative-subarray

## Problem Statement

We define the following:

- A *subarray* of an $n$-element array is an array composed from a contiguous block of the original array's elements. For example, if $array = [1, 2, 3]$, then the subarrays are $[1]$, $[2]$, $[3]$, $[1, 2]$, $[2, 3]$, and $[1, 2, 3]$. Something like $[1, 3]$ would *not* be a subarray as it's not a contiguous subsection of the original array.
- The *sum* of an array is the total sum of its elements.
	- An array's sum is *negative* if the total sum of its elements is negative.
    - An array's sum is *positive* if the total sum of its elements is positive.

Given an array of $n$ integers, find and print its number of *negative subarrays* on a new line.

## Input Format

The first line contains a single integer, $n$, denoting the length of array $A = [a_0, a_1, \ldots, a_{n - 1}]$.	
The second line contains $n$ space-separated integers describing each respective element, $a_i$, in array $A$. 

## Output Format

Print the number of subarrays of $A$ having negative sums.

## Constraints

- $1 \le n \le 100$
- $-10^4 \le a_i \le 10^4$

## Sample Input

1 -2 4 -5 1

## Explanation

There are nine negative subarrays of :

-

-

-

-

-

-

-

-

-

Thus, we print  on a new line.
