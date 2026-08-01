# Manasa and Pizza

- **Domain:** data-structures
- **Difficulty:** Medium
- **Max Score:** 80
- **Success Ratio:** 0.7592592592592593
- **Total Submissions:** 270
- **Solved Count:** 205
- **URL:** https://www.hackerrank.com/challenges/manasa-and-pizza

## Problem Statement

With the college fest approaching soon, Manasa is following a strict dieting regime . Today, she just cannot resist her temptation for having a pizza. An inner conflict ensues, and she decides that she will have a pizza, only if she comes up with a solution to the problem stated below. Help her get the pizza for herself.

Given a list _L_ of _N_ numbers, where  
_L = { a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, a<sub>4</sub> ....  , a<sub>N</sub>}_  
Find the value of _M_ that is computed as described below.  

![im1](https://hr-challenge-images.s3.amazonaws.com/2434/2434.jpg)  


**Input Format**  
The first line contains an integer _N_ i.e. size of the list _L_.  
The next line contains _N_ space separated integers, each representing an element of the list _L_.  

**Output Format**  
Print the value of _M_ _modulo (10<sup>9</sup> + 7)_. 

**Constraints**  
1 &le; _N_ &le; 5100<br>
0 &le; _a<sub>i</sub>_ &le; 10<sup>15</sup> , where _i &isin; [1 .. N]_

**Sample Input 00**  

    3
    1 2 3

    
**Sample Output 00**  

    40392
    
**Explanation**

There are 8 subsets of given set,

1. S = {1,2,3} and L - S  ={0} value of F(6) = 19601
2. S = {1,2} and L - S  ={3} value of F(0) = 1
3. S = {1,3} and L - S  ={2} value of F(2) = 17
4. S = {2,3} and L - S  ={1} value of F(4) = 577
5. S = {1} and L - S  ={2,3} value of F(4) = 577
6. S = {2} and L - S  ={1,3} value of F(2) = 17
7. S = {3} and L - S  ={1,2} value of F(0) = 1
8. S = {} and L - S  ={1,2,3} value of F(6) = 19601

Adding all these values, we get M = 40392.


## Input Format

The first line contains an integer N i.e. size of the list L.

The next line contains N space separated integers, each representing an element of the list L.

## Output Format

Print the value of M _modulo (109 + 7)_.

## Constraints

1 ≤ N ≤ 5100

0 ≤ ai ≤ 1015 , where i ∈ [1 .. N]

## Sample Input

3
1 2 3

## Sample Output

40392

## Explanation

There are 8 subsets of given set,

- S = {1,2,3} and L - S  ={0} value of F(6) = 19601

- S = {1,2} and L - S  ={3} value of F(0) = 1

- S = {1,3} and L - S  ={2} value of F(2) = 17

- S = {2,3} and L - S  ={1} value of F(4) = 577

- S = {1} and L - S  ={2,3} value of F(4) = 577

- S = {2} and L - S  ={1,3} value of F(2) = 17

- S = {3} and L - S  ={1,2} value of F(0) = 1

- S = {} and L - S  ={1,2,3} value of F(6) = 19601

Adding all these values, we get M = 40392.
