# Highest Value Palindrome

- **Domain:** shell
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.89375
- **Total Submissions:** 1280
- **Solved Count:** 1144
- **URL:** https://www.hackerrank.com/challenges/three-month-preparation-kit-richie-rich

## Problem Statement

Palindromes are strings that read the same from the left or right, for example <em>madam</em> or <em>0110</em>.  
  
You will be given a string representation of a number and a maximum number of changes you can make.  Alter the string, one digit at a time, to create the string representation of the largest number possible given the limit to the number of changes.  The length of the string may not be altered, so you must consider $0$'s left of all higher digits in your tests.  For example $0110$ is valid, $0011$ is not.  

Given a string representing the starting number, and a maximum number of changes allowed, create the largest palindromic string of digits possible or the string '-1' if it is not possible to create a palindrome under the contstraints.  

**Example**  
$s = \text{'1231'}$  
$k = 3$  

Make $3$ replacements to get $\text{'9339'}$.  

$s = \text{'12321'}$  
$k = 1$  

Make $1$ replacement to get $\text{'12921'}$.  

**Function Description**  

Complete the *highestValuePalindrome* function in the editor below.     

highestValuePalindrome has the following parameter(s):  

- *string s:* a string representation of an integer    
- *int n:* the length of the integer string  
- *int k:* the maximum number of changes allowed  

**Returns**  

- *string:* a string representation of the highest value achievable or `-1`  

## Input Format

The first line contains two space-separated integers, $n$ and $k$, the number of digits in the number and the maximum number of changes allowed.	
The second line contains an $n$-digit string of numbers.  

## Output Format

**Sample Input 0**
	
	STDIN	Function
    -----	--------
	4 1		n = 4, k = 1
	3943	s = '3943'
    
**Sample Output 0**
    
	3993
    

**Sample Input 1**

	6 3
	092282
    
**Sample Output 1**
    
	992299
    
**Sample Input 2**

	4 1
    0011
    
**Sample Output 2**
    
	-1

## Constraints

* $0 \lt n \le 10^5$
* $0 \le k \le 10^5$
* Each character $i$ in the number is an integer where $0 \le i \le 9$.

## Sample Input

STDIN   Function
-----   --------
4 1     n = 4, k = 1
3943    s = '3943'

## Sample Output

3993

## Explanation

Sample 0

There are two ways to make  a palindrome by changing no more than  digits:

-

-
