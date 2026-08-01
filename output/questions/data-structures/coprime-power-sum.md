# Coprime Power Sum

- **Domain:** data-structures
- **Difficulty:** Advanced
- **Max Score:** 75
- **Success Ratio:** 0.6466666666666666
- **Total Submissions:** 150
- **Solved Count:** 97
- **URL:** https://www.hackerrank.com/challenges/coprime-power-sum

## Problem Statement

Given two integers, $m$ and $k$, Alice loves to calculate their power sum using the following formula:
$$ PowerSum(m, k) \equiv \sum_{i=1}^{m} i^k $$

Bob has a set, $s$, of $n$ distinct *pairwise coprime* integers. Bob hates multiples of these integers, so he subtracts $i^k$ from Alice's power sum for each $i$ $\in$ $[1,m]$ whenever there exists at least one $j \in [1,n]$ such that $ i \bmod s_j \equiv 0$.

Alice and Bob are now confused about the final value of the power sum and decide to turn to Eve for help. Can you write a program that helps Eve solve this problem? Given $q$ queries consisting of $n$, $m$, and $k$, print the value of the power sum modulo $10^9 + 7$ on a new line for each query.

## Input Format

The first line contains an integer, $q$, denoting the number of queries. The $2 \cdot q$ lines describe each query over two lines:

1. The first line contains three space-separated integers denoting the respective values of $n$ (the number of integers in Bob's set), $k$ (the exponent variable in the power sum formula), and $m$ (the upper range bound in the power sum formula). 
2. The second line contains $n$ distinct space-separated integers describing the respective elements in set $s$. 

## Output Format

For each query, print the resulting value of the power sum after Bob's subtraction, modulo $10^9 + 7$.

## Constraints

* $1 \leq q \leq 2$  
* $1 \leq n \leq 50$  
* $0 \leq k \leq 10$  
* $1 \leq m \leq 10^{12}$  
* $1 \leq s_j \leq 10^{12}$		
* $s_i \ne s_j \text{, where } i \ne j$  	
* $gcd(s_i, s_j) \equiv 1 \text{, where } i \ne j$  

## Sample Input

2 1 10
2 3
3 2 18
4 13 9

## Sample Output

1055

## Explanation

We perform the following  queries:

- Alice first calculates the sum . Bob's set contains  and  only, so he subtracts the power of all numbers that are multiples of  and/or  from Alice's sum to get: . We then print the result of  on a new line.

- Alice first calculates the sum . Bob then subtracts multiples of , , and  from Alice's sum to get: . We then print the result of  on a new line.
