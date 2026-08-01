# Sherlock and Square

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 30
- **Success Ratio:** 0.6623076923076923
- **Total Submissions:** 1300
- **Solved Count:** 861
- **URL:** https://www.hackerrank.com/challenges/sherlock-and-square

## Problem Statement

Watson gives a square of side length 1 to Sherlock. Now, after each second, each square of some arbitrary side $L$ will break into four squares each of side $L/2$(as shown in the image below). 

![img][123]

Now, Watson asks Sherlock: What will be the sum of length of solid lines after $N$ seconds?  

As the number can be large print result mod $(10^9 + 7)$.

For example, after 0 seconds, the length is 4.    
After 1 second, the length is 6.

**Input Format**    
First line contains $T$, the number of testcases. Each testcase contains $N$ in one line.   

**Output Format**

For each testcase, print the required answer in a new line. 

**Constraints**   
$1 \le T \le 10^5$    
$0 \le N \le 10^9$

**Sample input**

    3
    0
    1
    5
    
**Sample output**

    4
    6
    66

[123]: http://i.imgur.com/yXME9kL.png

## Input Format

First line contains , the number of testcases. Each testcase contains  in one line.

## Output Format

For each testcase, print the required answer in a new line.

## Constraints

Sample input

3
0
1
5

Sample output

4
6
66
