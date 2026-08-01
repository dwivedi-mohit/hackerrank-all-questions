# The Longest Increasing Subsequence

- **Domain:** data-structures
- **Difficulty:** Advanced
- **Max Score:** 60
- **Success Ratio:** 0.4661962212610972
- **Total Submissions:** 30751
- **Solved Count:** 14336
- **URL:** https://www.hackerrank.com/challenges/longest-increasing-subsequent

## Problem Statement

**An Introduction to the Longest Increasing Subsequence Problem**  

The task is to find the length of the longest subsequence in a given array of integers such that all elements of the subsequence are sorted in strictly ascending order. This is called the Longest Increasing Subsequence (LIS) problem.

For example, the length of the LIS for $[15, 27, 14, 38, 26, 55, 46, 65, 85]$ is $6$ since the longest increasing subsequence is $[15, 27, 38, 55, 65, 85]$.  

Here's a great YouTube video of a lecture from MIT's Open-CourseWare covering the topic.  

[(iframe youtube 4fQJGoeW5VE 560 315)]  

This is one approach which solves this in quadratic time using dynamic programming. A more efficient algorithm which solves the problem in $O(n \log n)$ time is [available here](http://www.geeksforgeeks.org/construction-of-longest-monotonically-increasing-subsequence-n-log-n/). 

Given a sequence of integers, find the length of its longest strictly increasing subsequence.

**Function Description**  

Complete the *longestIncreasingSubsequence* function in the editor below.  It should return an integer that denotes the array's LIS.  

longestIncreasingSubsequence has the following parameter(s):  

- *arr*: an unordered array of integers  

## Input Format

The first line contains a single integer $n$, the number of elements in $arr$.  
Each of the next $n$ lines contains an integer, $arr[i]$

## Output Format

Print a single line containing a single integer denoting the length of the longest increasing subsequence.

## Constraints

- $1 \le n \le 10^6$  
- $1 \le arr[i] \le 10^5$  

## Sample Input

5
2
7
4
3
8

## Sample Output

3

## Explanation

In the array , the longest increasing subsequence is .  It has a length of .
