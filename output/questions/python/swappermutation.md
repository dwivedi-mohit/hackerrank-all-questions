# Swap Permutation

- **Domain:** python
- **Difficulty:** Medium
- **Max Score:** 85
- **Success Ratio:** 0.7602739726027398
- **Total Submissions:** 2628
- **Solved Count:** 1998
- **URL:** https://www.hackerrank.com/challenges/swappermutation

## Problem Statement

You are given an array _A = [1, 2, 3, ..., n]_:     

1. How many sequences _(S<sub>1</sub>)_ can you get after exact _k_ adjacent swaps on _A_? 

2. How many sequences _(S<sub>2</sub>)_ can you get after at most _k_ swaps on _A_?  

An adjacent swap can be made between two elements of the Array A, A[i] and A[i+1] or A[i] and A[i-1].  
A swap otherwise can be between any two elements of the array A[i] and A[j] &forall; 1 &le; i, j &le; N, i &ne; j.


## Input Format

First and only line contains _n_ and _k_ separated by space.    


## Output Format

Output _S<sub>1</sub> % MOD_ and _S<sub>2</sub> % MOD_ in one line, where `MOD = 1000000007`.    


## Constraints

1 &le; n &le; 2500       
1 &le; k &le; 2500      


## Sample Input

3 2

## Sample Output

3 6

## Explanation

Original array: [1, 2, 3]
1. After 2 adjacent swaps:
We can get [1, 2, 3], [2, 3, 1], [3, 1, 2] ==> S1 == 3

2. After at most 2 swaps:
1) After 0 swap: [1, 2, 3]
2) After 1 swap: [2, 1, 3], [3, 2, 1], [1, 3, 2].
3) After 2 swaps: [1, 2, 3], [2, 3, 1], [3, 1, 2]
==> S2 == 6
