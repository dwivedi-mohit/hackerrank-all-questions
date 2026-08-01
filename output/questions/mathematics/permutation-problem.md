# Permutation Problem

- **Domain:** mathematics
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.4088586030664395
- **Total Submissions:** 587
- **Solved Count:** 240
- **URL:** https://www.hackerrank.com/challenges/permutation-problem

## Problem Statement

How many n-digit numbers (without leading zeros) are there such that no digit occurs more than k times?  

As the count of such n-digit numbers can be very large, print the answer mod (10<sup>9</sup>+7)  

**Input Format**  

The first line contains an integer, _T_ , the number of test cases. This is followed by _T_ lines each containing 2 space separated integers, _n_ and _k_  


**Constraints**  

_T_ &le; 100000  
1 &le; _n_ &le; 1000  
1 &le; _k_ &le; 10<sup>9</sup>

**Sample Input**

    2
    2 3
    2 1

**Sample Output**

    90
    81

**Explanation**  
Case 1: A number can appear three times. So we have 9 (all except 0) numbers for first digit and 10 numbers for the second digit.  
Case 2: A number can appear only once. So we have 9 choices for the first digit and 9(all except the first one) for the second digit. 



## Input Format

The first line contains an integer, T , the number of test cases. This is followed by T lines each containing 2 space separated integers, n and k

## Constraints

T ≤ 100000

1 ≤ n ≤ 1000

1 ≤ k ≤ 109

## Sample Input

2 3
2 1

## Sample Output

81

## Explanation

Case 1: A number can appear three times. So we have 9 (all except 0) numbers for first digit and 10 numbers for the second digit.

Case 2: A number can appear only once. So we have 9 choices for the first digit and 9(all except the first one) for the second digit.
