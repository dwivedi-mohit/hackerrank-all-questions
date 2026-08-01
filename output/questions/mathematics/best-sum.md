# Best Sum

- **Domain:** mathematics
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.43582089552238806
- **Total Submissions:** 335
- **Solved Count:** 146
- **URL:** https://www.hackerrank.com/challenges/best-sum

## Problem Statement

You are given two arrays *A* and *B* of length **N**. Let S be the set of integers from 1 to **N**. Can you find the maximum possible value of (A<sub>i1</sub>+A<sub>i2</sub>+...+A<sub>ik</sub>)<sup>2</sup>+(B<sub>i1</sub>+B<sub>i2</sub>+...+B<sub>ik</sub>)<sup>2</sup> where {i1,i2...ik} is a non-empty subset of S?

**Input Format**  
The first line contains a single integer **T**, denoting the number of test cases.  
T testcases follow, each test case given in following format.  

    N  
    A1 A2 ... AN  
    B1 B2 ... BN  

**Output Format**  
For each test case, output the maximum possible value in one line.  

**Constraints**  
1 <= T <= 10  
1 <= N <= 1000  
-10<sup>6</sup> <= A<sub>i</sub>, B<sub>i</sub> <= 10<sup>6</sup>  

**Sample Input**  

    1  
    2  
    -1 5  
    4 -5  

**Sample Output**  

    50

**Explanation**  
All possible non-empty subsets for N = 2 of S = {1,2} are {1}, {2} and {1,2}. The maximum possible values of the above equation now are 

+ (-1)<sup>2</sup> + (4)<sup>2</sup> = 17  
+ (5)<sup>2</sup> + (-5)<sup>2</sup> = 50  
+ (-1 + 5)<sup>2</sup> + (4 - 5)<sup>2</sup> = 17

hence 50. 

**Timelimits**

Timelimits for this challenge can be seen [here](https://www.hackerrank.com/environment)

## Input Format

The first line contains a single integer T, denoting the number of test cases.

T testcases follow, each test case given in following format.

N
A1 A2 ... AN
B1 B2 ... BN

## Output Format

For each test case, output the maximum possible value in one line.

## Constraints

1 <= T <= 10

1 <= N <= 1000

-106 <= Ai, Bi <= 106

## Sample Input

2
-1 5
4 -5

## Explanation

All possible non-empty subsets for N = 2 of S = {1,2} are {1}, {2} and {1,2}. The maximum possible values of the above equation now are

- (-1)2 + (4)2 = 17

- (5)2 + (-5)2 = 50

- (-1 + 5)2 + (4 - 5)2 = 17

hence 50.

Timelimits

Timelimits for this challenge can be seen here
