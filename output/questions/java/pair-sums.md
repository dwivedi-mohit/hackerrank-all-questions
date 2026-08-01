# Pair Sums

- **Domain:** java
- **Difficulty:** Expert
- **Max Score:** 80
- **Success Ratio:** 0.6372198765833063
- **Total Submissions:** 3079
- **Solved Count:** 1962
- **URL:** https://www.hackerrank.com/challenges/pair-sums

## Problem Statement

Given an array, we define its *value* to be the value obtained by following these instructions:

- Write down all pairs of numbers from this array.  
- Compute the product of each pair.  
- Find the sum of all the products.

For example, for a given array, for a given array [$7$, $2$, $-1$, $2$], 


| Pairs                 | (7, 2), (7, -1), (7, 2), (2, -1), (2, 2), (-1, 2) |
|-----------------------|---------------------------------------------------|
| Products of the pairs | 14, -7, 14, -2, 4, -2                             |
| Sum of the products   | 14 + (-7) + 14 + (-2) + 4 + (-2) = $\color{green}\texttt{21}$ |

Note that $(7, 2)$ is listed twice, one for each occurrence of $2$.  

Given an array of integers, find the largest *value* of any of its nonempty subarrays.

*Note*: A subarray is a contiguous subsequence of the array.

Complete the function `largestValue` which takes an array and returns an integer denoting the largest *value* of any of the array's nonempty subarrays.  

## Input Format

The first line contains a single integer $n$, denoting the number of integers in array $A$.  
The second line contains $n$ space-separated integers $A_i$ denoting the elements of array $A$.  

## Output Format

Print a single line containing a single integer denoting the largest *value* of any of the array's nonempty subarrays.

## Constraints

- $3 \le n \le 5\cdot 10^5$  
- $-10^3 \le A_i \le 10^3$  

**Subtasks**  

- $n \le 5000$ for 20% of the points.  
- $n \le 2\cdot 10^5$ for 70% of the points.


## Sample Input

6
-3 7 -2 3 5 -2

## Sample Output

41

## Explanation

In this case, we have . The largest-valued subarray turns out to be  with value .
