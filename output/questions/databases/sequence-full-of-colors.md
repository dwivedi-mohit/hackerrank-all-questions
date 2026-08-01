# Sequence full of colors

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9243329350856233
- **Total Submissions:** 2511
- **Solved Count:** 2321
- **URL:** https://www.hackerrank.com/challenges/sequence-full-of-colors

## Problem Statement

You are given a sequence of $N$ balls in 4 colors: _red, green, yellow and blue_. The sequence is _full of colors_ if and only if all of the following conditions are true:

- There are as many red balls as green balls.
- There are as many yellow balls as blue balls.
- Difference between the number of red balls and green balls in every _prefix_ of the sequence is at most 1.
- Difference between the number of yellow balls and blue balls in every _prefix_ of the sequence is at most 1.

Your task is to write a program, which for a given sequence prints `True` if it  is _full of colors_, otherwise it prints `False`.

**Input**  
In the first line there is one number $T$ denoting the number of tests cases.   
$T$ lines follow. In each of them there is a sequence of letters $\{R, G, Y, B\}$ denoting the input sequence ($R$ - red, $G$ - green, $Y$ - yellow, $B$ - blue).

**Output**  
For each test case, print `True` if this is a sequence _full of colors_, otherwise print `False`.  

**Constraints**  
$1 \le T \le 10$  
Sequence will only consists of letters $\{R, G, Y, B\}$.   
Sum of length of all sequences will not exceed $10^6$.  

**Notes**  
A prefix of a string $T = t_1 \dots t_n$ is a string $\widehat T = t_1 \dots t_{m}$, where $0 \leq m \leq n$. 


**Sample Input**

	4
	RGGR
	RYBG
	RYRB
	YGYGRBRB

**Sample Output**

    True
    True
    False
    False

**Explanation**  
In the first two test cases, all four conditions are satisfied.  
In the third test case, condition #1 fails as there are more red balls than green balls and condition #3 also fails for prefix "RYR" as the difference between the number of red and green balls is more than 1.
In the fourth test, for a prefix "YGYG" condition 4<sup>th</sup> fails.
    
---
**Tested by** [Abhiranjan](/abhiranjan)


## Constraints

Sequence will only consists of letters .

Sum of length of all sequences will not exceed .

Notes

A prefix of a string  is a string , where .

## Sample Input

RGGR
RYBG
RYRB
YGYGRBRB

## Sample Output

True
True
False
False

## Explanation

In the first two test cases, all four conditions are satisfied.

In the third test case, condition #1 fails as there are more red balls than green balls and condition #3 also fails for prefix "RYR" as the difference between the number of red and green balls is more than 1.
In the fourth test, for a prefix "YGYG" condition 4th fails.

Tested by Abhiranjan
