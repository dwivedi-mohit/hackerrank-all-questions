# Sam and substrings

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.6319900031240238
- **Total Submissions:** 35211
- **Solved Count:** 22253
- **URL:** https://www.hackerrank.com/challenges/sam-and-substrings

## Problem Statement

Samantha and Sam are playing a numbers game.  Given a number as a string, no leading zeros, determine the sum of all integer values of substrings of the string.   

Given an integer as a string, sum all of its substrings cast as integers.  As the number may become large, return the value modulo $10^9+7$.  

**Example**   
$n = \text{'42'}$  

Here $n$ is a string that has $3$ integer substrings: $4$, $2$, and $42$.  Their sum is $48$, and $48 \text{ modulo } (10^9+7) = 48$.

**Function Description**

Complete the *substrings* function in the editor below.   

substrings has the following parameter(s):  

- *string n:* the string representation of an integer   

**Returns**   

- *int:* the sum of the integer values of all substrings in $n$, modulo $10^9+7$

## Input Format

A single line containing an integer as a string, without leading zeros.  



## Constraints

+ $1 \le n cast as an integer \le 2 \times 10^5$



## Sample Input

16

## Sample Output

23

## Explanation

The substrings of 16 are 16, 1 and 6 which sum to 23.
