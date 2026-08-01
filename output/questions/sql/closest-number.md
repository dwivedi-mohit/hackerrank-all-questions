# Closest Number

- **Domain:** sql
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.7274762509832395
- **Total Submissions:** 16527
- **Solved Count:** 12023
- **URL:** https://www.hackerrank.com/challenges/closest-number

## Problem Statement

You are given 3 numbers *a*, *b* and *x*. You need to output the multiple of *x* which is closest to *a<sup>b</sup>*. If more than one answer exists , display the smallest one. 



## Input Format

The first line contains *T*, the number of testcases.  
*T* lines follow, each line contains 3 space separated integers (*a*, *b* and *x* respectively)

## Output Format

For each test case , output the multiple of *x* which is closest to *a<sup>b</sup>* 

## Constraints

1 &le; *T* &le; 10<sup>5</sup>  
1 &le; *x* &le; 10<sup>9</sup>  
0 &lt; *a<sup>b</sup>* &le; 10<sup>9</sup>    
1 &le; *a* &le; 10<sup>9</sup>    
-10<sup>9</sup> &le; *b* &le; 10<sup>9</sup> 

## Sample Input

3
349 1 4
395 1 7
4 -2 2

## Sample Output

348
392
0

## Explanation

The closest multiple of 4 to 349 is 348.

The closest multiple of 7 to 395 is 392.

The closest multiple of 2 to 1/16 is 0.
