# Big Sorting

- **Domain:** sql
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.6800437250116051
- **Total Submissions:** 133562
- **Solved Count:** 90828
- **URL:** https://www.hackerrank.com/challenges/big-sorting

## Problem Statement

Consider an array of numeric strings where each string is a positive number with anywhere from $1$ to $10^6$ digits. Sort the array's elements in *non-decreasing*, or ascending order of their integer values and return the sorted array.

**Example**  
$unsorted = \text{['1', '200', '150', '3']}$  

Return the array ['1', '3', '150', '200']. 

**Function Description**  

Complete the *bigSorting* function in the editor below.  

bigSorting has the following parameter(s):  

- *string unsorted[n]:* an unsorted array of integers as strings  

**Returns**  

- *string[n]:*  the array sorted in numerical order  

## Input Format

The first line contains an integer, $n$, the number of strings in $unsorted$.		
Each of the $n$ subsequent lines contains an integer string, $unsorted[i]$.

## Constraints

* $1 \le n \le 2 \times 10^5$
* Each string is guaranteed to represent a positive integer.
* There will be no leading zeros.
* The total number of digits across all strings in $unsorted$ is between $1$ and $10^6$ (inclusive).

## Sample Input

6
31415926535897932384626433832795
1
3
10
3
5

## Sample Output

1
3
3
5
10
31415926535897932384626433832795

## Explanation

The initial array of strings is . When we order each string by the real-world integer value it represents, we get:

We then print each value on a new line, from smallest to largest.
