# k-balance number

- **Domain:** sql
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.6697247706422018
- **Total Submissions:** 218
- **Solved Count:** 146
- **URL:** https://www.hackerrank.com/challenges/k-balance

## Problem Statement

Your task is to calculate the sum (indicated by S) of all the k-balanced integers between [L, R]. An integer is called k-balanced when either of #1 or #2 below holds true.

1. The length of the integer <= k     
2. Sum of the first k digits (with no leading zeros) is equal to the sum of the last k digits.    

**Input format**  
L R k

**Output format**  
S % 1000000007

**Constraints**  
0 < L <= R < 10^18  
0 < k <= 18

**Sample Input**  
9 23 1

**Sample Output**  
42

**Explanation**  
9, 11 and 22 are the only 3 integers between 9 and 23 ( both included ) that are k-balanced. Hence, the answer is 9+11+22=42


## Constraints

0 < L <= R < 10^18

0 < k <= 18

## Sample Input

9 23 1

## Explanation

9, 11 and 22 are the only 3 integers between 9 and 23 ( both included ) that are k-balanced. Hence, the answer is 9+11+22=42
