# Sherlock and Cost

- **Domain:** cpp
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.7151931713853255
- **Total Submissions:** 40301
- **Solved Count:** 28823
- **URL:** https://www.hackerrank.com/challenges/sherlock-and-cost

## Problem Statement

In this challenge, you will be given an array $B$ and must determine an array $A$.  There is a special rule:  For all $i$, $A[i] \le B[i]$.  That is, $A[i]$ can be any number you choose such that $1 \le A[i] \le B[i]$.  Your task is to select a series of $A[i]$ given $B[i]$ such that the sum of the absolute difference of consecutive pairs of $A$ is maximized.  This will be the array's *cost*, and will be represented by the variable $S$ below. 

The equation can be written:

$$S = \sum_\limits{i = 2}^{N} |A[i] - A[i-1]|$$

For example, if the array $B=[1,2,3]$, we know that $1 \le A[1] \le 1$, $1 \le A[2] \le 2$, and $1 \le A[3] \le 3$.  Arrays meeting those guidelines are:
```
[1,1,1], [1,1,2], [1,1,3]
[1,2,1], [1,2,2], [1,2,3]
```
Our calculations for the arrays are as follows:
```
|1-1| + |1-1| = 0	|1-1| + |2-1| = 1	|1-1| + |3-1| = 2
|2-1| + |1-2| = 2	|2-1| + |2-2| = 1	|2-1| + |3-2| = 2
```

The maximum value obtained is $2$.

**Function Description**

Complete the *cost* function in the editor below.  It should return the maximum value that can be obtained.  

cost has the following parameter(s):  

- *B*: an array of integers  

## Input Format

The first line contains the integer $t$, the number of test cases. 

Each of the next $t$ pairs of lines is a test case where:  
- The first line contains an integer $n$, the length of $B$  
- The next line contains $n$ space-separated integers $B[i]$  


## Output Format

For each test case, print the maximum sum on a separate line.   


## Constraints

- $1 \le t \le 20$ 
- $1 \lt n \le 10^5$
- $1 \le B[i] \le 100$


## Sample Input

5
10 1 10 1 10

## Explanation

The maximum sum occurs when A[1]=A[3]=A[5]=10 and A[2]=A[4]=1.  That is .
