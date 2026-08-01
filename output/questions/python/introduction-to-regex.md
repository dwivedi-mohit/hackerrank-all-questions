# Detect Floating Point Number

- **Domain:** python
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.929980157207538
- **Total Submissions:** 91217
- **Solved Count:** 84830
- **URL:** https://www.hackerrank.com/challenges/introduction-to-regex

## Problem Statement

<sub>Check [Tutorial](https://www.hackerrank.com/challenges/introduction-to-regex/tutorial) tab to know how to to solve.</sub>  

You are given a string $N$.  
Your task is to verify that $N$ is a floating point number.  

In this task, a valid float number must satisfy *all* of the following requirements:  

$\gt$ Number can start with **`+`**, **`-`** or **`.`** symbol.  
$ \ \ \ \ $For example:  
$ \ \ \ \ ✔ \ $+4.50   
$ \ \ \ \ ✔ \ $-1.0   
$ \ \ \ \ ✔ \ $.5   
$ \ \ \ \ ✔ \ $-.7   
$ \ \ \ \ ✔ \ $+.4   
$ \ \ \ \ ✖ $ __`-+4.5`__    

$\gt$ Number must contain *at least* $1$ decimal value.  
$ \ \ \ \ $For example:  
$ \ \ \ \ ✖ $ __`12.`__  
$ \ \ \ \ ✔ \ $12.0     

$\gt$ Number must have exactly one __`.`__ symbol.  
$\gt$ Number must not give any exceptions when converted using $float(N)$.

## Input Format

The first line contains an integer $T$, the number of test cases.  
The next $T$ line(s) contains a string $N$.




## Output Format

Output *True* or *False* for each test case.

## Constraints

+ $ 0 < T < 10$

## Sample Input

4
4.0O0
-1.00
+4.54
SomeRandomStuff

## Sample Output

False
True
True
False

## Explanation

: O is not a digit.

: is valid.

: is valid.

SomeRandomStuff: is not a number.
