# The Power Sum

- **Domain:** fp
- **Difficulty:** Medium
- **Max Score:** 20
- **Success Ratio:** 0.9025968526078634
- **Total Submissions:** 59033
- **Solved Count:** 53283
- **URL:** https://www.hackerrank.com/challenges/the-power-sum

## Problem Statement

Find the number of ways that a given integer, $X$, can be expressed as the sum of the $N^{th}$ powers of unique, natural numbers. 

For example, if $X=13$ and $N=2$, we have to find all combinations of unique squares adding up to $13$.  The only solution is  $2^2+3^2$.  

**Function Description**

Complete the *powerSum* function in the editor below.  It should return an integer that represents the number of possible combinations.  

powerSum has the following parameter(s):  

- *X*: the integer to sum to  
- *N*: the integer power to raise numbers to  

## Input Format

The first line contains an integer $X$.  
The second line contains an integer $N$.  

 

## Output Format

Output a single integer, the number of possible combinations caclulated.   

## Constraints

- $1 \le X \le 1000$   
- $2 \le N \le 10$  

## Sample Input

10
2

## Sample Output

1

## Explanation

If  and , we need to find the number of ways that  can be represented as the sum of squares of unique numbers.

This is the only way in which  can be expressed as the sum of unique squares.
