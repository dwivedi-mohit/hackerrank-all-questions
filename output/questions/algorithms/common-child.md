# Common Child

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 60
- **Success Ratio:** 0.6267451409800164
- **Total Submissions:** 116896
- **Solved Count:** 73264
- **URL:** https://www.hackerrank.com/challenges/common-child

## Problem Statement

A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string.  Letters cannot be rearranged.  Given two strings of equal length, what's the longest string  that can be constructed such that it is a child of both?  

**Example**   

$s1 =\text{ 'ABCD'}$   
$s2 =\text{ 'ABDC'}$   

These strings have two children with maximum length 3, `ABC` and `ABD`.  They can be formed by eliminating either the `D` or `C` from both strings.  Return $3$.  

**Function Description**

Complete the *commonChild* function in the editor below.  

commonChild has the following parameter(s):

- *string s1:*  a string
- *string s2:*  another string   

**Returns**   

- *int:* the length of the longest string which is a common child of the input strings 


## Input Format

There are two lines, each with a string, $s1$ and $s2$. 

## Output Format

  

## Constraints

- $1 \le |s1|,\ |s2| \le 5000$ where $|s|$ means "the length of $s$"     
- All characters are upper case in the range ascii[A-Z].
 

## Sample Input

HARRY
SALLY

## Explanation

The longest string that can be formed by deleting zero or more characters from  and  is , whose length is 2.
