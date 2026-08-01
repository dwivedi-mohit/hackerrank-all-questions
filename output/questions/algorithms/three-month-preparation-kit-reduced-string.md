# Super Reduced String

- **Domain:** algorithms
- **Difficulty:** Easy
- **Max Score:** 100
- **Success Ratio:** 0.970970206264324
- **Total Submissions:** 3927
- **Solved Count:** 3813
- **URL:** https://www.hackerrank.com/challenges/three-month-preparation-kit-reduced-string

## Problem Statement

Reduce a string of lowercase characters in range `ascii[‘a’..’z’]`by doing a series of operations.  In each operation, select a pair of adjacent letters that match, and delete them.  

Delete as many characters as possible using this method and return the resulting string.  If the final string is empty, return `Empty String`

**Example**. 

$s = \text{'aab'}$  

`aab` shortens to `b` in one operation: remove the adjacent `a` characters. 

$s =\text{'abba'}$  

Remove the two 'b' characters leaving 'aa'.  Remove the two 'a' characters to leave ''.  Return 'Empty String'.


**Function Description**

Complete the *superReducedString* function in the editor below.   

superReducedString has the following parameter(s):  

- *string s:* a string to reduce  

**Returns**  

- *string:* the reduced string or `Empty String`  

## Input Format

A single string, $s$.

## Constraints

- $1 \le \text{ length of }s \le 100$
