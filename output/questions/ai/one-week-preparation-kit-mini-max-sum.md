# Mini-Max Sum

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 100
- **Success Ratio:** 0.9446559383801125
- **Total Submissions:** 405843
- **Solved Count:** 383382
- **URL:** https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum

## Problem Statement

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.  

**Example**   
$arr = [1, 3, 5, 7, 9]$

The minimum sum is $1 + 3 + 5 + 7 = 16$ and the maximum sum is $3 + 5 + 7 + 9 = 24$.  The function prints

    16 24
    
**Function Description**  

Complete the *miniMaxSum* function in the editor below.  

miniMaxSum has the following parameter(s):

- *arr*: an array of $5$ integers  

**Print**   
  
Print two space-separated integers on one line: the minimum sum and the maximum sum of $4$ of $5$ elements.  

## Input Format

A single line of five space-separated integers.

## Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly *four* of the five integers. (The output can be greater than a 32 bit integer.)

## Constraints

$1 \le arr[i] \le 10^9$  

## Sample Input

1 2 3 4 5

## Sample Output

10 14

## Explanation

The numbers are , , , , and . Calculate the following sums using four of the five integers:

- Sum everything except , the sum is .

- Sum everything except , the sum is .

- Sum everything except , the sum is .

- Sum everything except , the sum is .

- Sum everything except , the sum is .

Hints: Beware of integer overflow! Use 64-bit Integer.

Need help to get started? Try the Solve Me First problem
