# Text Wrap

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9862191637364167
- **Total Submissions:** 509911
- **Solved Count:** 502884
- **URL:** https://www.hackerrank.com/challenges/text-wrap

## Problem Statement

<sub>Check [Tutorial](https://www.hackerrank.com/challenges/text-wrap/tutorial) tab to know how to to solve.</sub>  

You are given a string $S$ and width $w$.  
Your task is to wrap the string into a paragraph of width $w$.  

**Function Description**   

Complete the *wrap* function in the editor below.  

*wrap* has the following parameters:   

- *string string:* a long string   
- *int max_width:* the width to wrap to   

**Returns**   

- *string:* a single string with newline characters ('\n') where the breaks should be   

## Input Format

The first line contains a string, $string$.  
The second line contains the width, $max_width$.



## Constraints

+ $0 < len(string) < 1000$  
+ $0 < max_width < len(string)$



## Sample Input

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

## Sample Output

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
