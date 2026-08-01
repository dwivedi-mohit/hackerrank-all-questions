# Non-Divisible Subset

- **Domain:** c
- **Difficulty:** Medium
- **Max Score:** 20
- **Success Ratio:** 0.7158723223727118
- **Total Submissions:** 157929
- **Solved Count:** 113057
- **URL:** https://www.hackerrank.com/challenges/non-divisible-subset

## Problem Statement

Given a set of distinct integers, print the size of a maximal subset of $S$ where the sum of any $2$ numbers in $S'$ is *not* evenly divisible by $k$.

**Example**   
$S = [19, 10, 12, 10, 24, 25, 22]$
$k = 4$

One of the arrays that can be created is $S'[0] = [10, 12, 25]$.  Another is $S'[1] = [19, 22, 24]$.  After testing all permutations, the maximum length solution array has $3$ elements.  

**Function Description**  

Complete the *nonDivisibleSubset* function in the editor below.  

nonDivisibleSubset has the following parameter(s):  

- *int S[n]*: an array of integers  
- *int k*: the divisor  

**Returns**   

- *int:* the length of the longest subset of $S$ meeting the criteria  

## Input Format

The first line contains $2$ space-separated integers, $n$ and $k$, the number of values in $S$ and the *non* factor.	
The second line contains $n$ space-separated integers, each an $S[i]$, the unique values of the set.

## Constraints

* $1 \leq n \leq 10^5$
* $1 \leq k \leq 100$
* $1 \leq S[i] \leq 10^9$
* All of the given numbers are distinct.

## Sample Input

STDIN    Function
-----    --------
4 3      S[] size n = 4, k = 3
1 7 2 4  S = [1, 7, 2, 4]

## Explanation

The sums of all permutations of two elements from  are:

1 + 7 = 8
1 + 2 = 3
1 + 4 = 5
7 + 2 = 9
7 + 4 = 11
2 + 4 = 6

Only  will not ever sum to a multiple of .
