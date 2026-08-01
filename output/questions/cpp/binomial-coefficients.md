# Binomial Coefficients

- **Domain:** cpp
- **Difficulty:** Medium
- **Max Score:** 60
- **Success Ratio:** 0.7155405405405405
- **Total Submissions:** 1480
- **Solved Count:** 1059
- **URL:** https://www.hackerrank.com/challenges/binomial-coefficients

## Problem Statement

In mathematics, **binomial coefficients** are a family of positive integers that occur as coefficients in the binomial theorem.  
$$n\choose k$$
denotes the number of ways of choosing k objects from n different objects.

However when n and k are too large, we often save them after modulo operation by a prime number P. Please calculate how many binomial coefficients of n become to 0 after modulo by P.

**Input Format**  
The first of input is an integer $T$, the number of test cases.  
Each of the following $T$ lines contains 2 integers, $n$ and prime $P$.  

**Constraints**  
$T < 100$  
$n < 10^{500}$  
$P < 10^9$

**Output Format**

For each test case, output a line contains the number of   $n \choose k$s (0<=k<=n)  each of which after modulo operation by P is 0.

**Sample Input**

    3
    2 2
    3 2
    4 3

**Sample Output**

    1
    0
    1



## Input Format

The first of input is an integer , the number of test cases.

Each of the following  lines contains 2 integers,  and prime .

## Output Format

For each test case, output a line contains the number of   s (0<=k<=n)  each of which after modulo operation by P is 0.

## Sample Input

2 2
3 2
4 3

## Sample Output

0
1
