# Simple One

- **Domain:** python
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.8
- **Total Submissions:** 580
- **Solved Count:** 464
- **URL:** https://www.hackerrank.com/challenges/simple-one

## Problem Statement

You are given the equation $\tan\alpha = \frac{p}{q}$ and a positive integer, $n$. Calculate $\tan n\alpha$. There are $T$ test cases.



## Input Format

The first line contains $T$, the number of test cases.   
The next $T$ lines contain three space separated integers: $p, q$ and $n$, respectively.  

**Constraints**  
$0 \leqslant p \leqslant 10^9$  
$1 \leqslant q \leqslant 10^9$  
$1 \leqslant n \leqslant 10^9$  
$T \leqslant 10^4$

## Output Format

If the result is defined, it is always a rational number. However, it can be very big.  
Output the answer modulo $(10^9 + 7)$.  
If the answer is $\frac{a}{b}$ and $b$ is not divisible by $(10^9+7)$, there is a unique integer $0 \leqslant x < 10^9 + 7$ where $a \equiv bx \mod (10^9 + 7)$.  
Output this integer, $x$.  
It is guaranteed that $b$ is not divisible by $(10^9 + 7)$ for all test cases.  

## Sample Input

2 1 2
5 6 7

## Sample Output

237627959

## Explanation

If  then  and
.

So, the answer is .
