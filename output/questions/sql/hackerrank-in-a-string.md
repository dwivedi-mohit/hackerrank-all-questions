# HackerRank in a String!

- **Domain:** sql
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9285237770655373
- **Total Submissions:** 137906
- **Solved Count:** 128049
- **URL:** https://www.hackerrank.com/challenges/hackerrank-in-a-string

## Problem Statement

We say that a string contains the word `hackerrank` if a [subsequence](https://en.wikipedia.org/wiki/Subsequence) of its characters spell the word `hackerrank`.  Remeber that a subsequence maintains the order of characters selected from a sequence.   

More formally, let $p[0], p[1], \cdots, p[9]$ be the respective indices of `h`, `a`, `c`, `k`, `e`, `r`, `r`, `a`, `n`, `k` in string $s$. If $p[0] < p[1] < p[2] < \cdots < p[9]$ is true, then $s$ contains `hackerrank`.

For each query, print `YES` on a new line if the string contains `hackerrank`, otherwise, print `NO`.  

**Example**  
$s=\text{haacckkerrannkk}$  

This contains a subsequence of all of the characters in the proper order.  Answer `YES`  

$s=\text{haacckkerannk}$  

This is missing the second 'r'.  Answer `NO`.  

$s = \text{hccaakkerrannkk}$  

There is no 'c' after the first occurrence of an 'a', so answer `NO`.  


**Function Description**  

Complete the *hackerrankInString* function in the editor below.   

hackerrankInString has the following parameter(s):  

- *string s:* a string   

**Returns**  

- *string:* `YES` or `NO`

## Input Format

The first line contains an integer $q$, the number of queries.	
Each of the next $q$ lines contains a single query string $s$.  

## Constraints

+ $2 \le q \le 10^2$  
+ $10 \le \text{ length of }s \le 10^4$

## Sample Input

2
hereiamstackerrank
hackerworld

## Sample Output

YES
NO

## Explanation

We perform the following  queries:

-

The characters of hackerrank are bolded in the string above. Because the string contains all the characters in hackerrank in the same exact order as they appear in hackerrank, we return YES.

-  does not contain the last three characters of hackerrank, so we return NO.
