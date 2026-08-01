# Sherlock and the Valid String

- **Domain:** mathematics
- **Difficulty:** Medium
- **Max Score:** 35
- **Success Ratio:** 0.671248542061525
- **Total Submissions:** 219488
- **Solved Count:** 147331
- **URL:** https://www.hackerrank.com/challenges/sherlock-and-valid-string

## Problem Statement

Sherlock considers a string to be *valid* if all characters of the string appear the same number of times.  It is also *valid* if he can remove just $1$ character at $1$ index in the string, and the remaining characters will occur the same number of times.  Given a string $s$, determine if it is *valid*.  If so, return `YES`, otherwise return `NO`.

**Example**  
$s=abc$

This is a valid string because frequencies are $\{a: 1, b: 1, c: 1\}$.  

$s=abcc$  

This is a valid string because we can remove one $c$ and have $1$ of each character in the remaining string.  

$s=abccc$  

This string is not *valid* as we can only remove $1$ occurrence of $c$.  That leaves character frequencies of $\{a: 1, b: 1, c: 2\}$.  

**Function Description**  

Complete the *isValid* function in the editor below.  

isValid has the following parameter(s):  

- *string s*: a string  

**Returns**  

- *string:* either `YES` or `NO`


## Input Format

A single string $s$.

## Constraints

- $1 \le |s| \le 10^5$   
- Each character $s[i] \in ascii[a-z]$

## Sample Input

aabbcd

## Sample Output

NO

## Explanation

Given , we would need to remove two characters, both c and d  aabb or a and b  abcd, to make it valid. We are limited to removing only one character, so  is invalid.
