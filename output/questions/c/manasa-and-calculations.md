# Manasa and Calculations 

- **Domain:** c
- **Difficulty:** Medium
- **Max Score:** 60
- **Success Ratio:** 0.7147239263803681
- **Total Submissions:** 326
- **Solved Count:** 233
- **URL:** https://www.hackerrank.com/challenges/manasa-and-calculations

## Problem Statement

Manasa is a student in the department of Mathematics. She is pretty good at doing calculations involving small numbers, but large numbers scare her. So she wants you to help her in the following calculations.

Given two numbers in the following manner:

$$ A = p_1 ^{a_1} \times p_2 ^{a_2}  \times  p_3 ^{a_3} \times  \cdots \times p_N ^{a_N}  $$
$$ B = p_1 ^{b_1} \times p_2 ^{b_2}  \times  p_3 ^{b_3} \times  \cdots \times p_N ^{b_N}   $$

($p_i$ is a prime number, and all the $p_i$'s are distinct)

She wants you to calculate $S$ for her, where $S$ is the sum of $m+n$ for all pairs of numbers  where $ m \le n$, $\gcd(m,n) = B$ and $\text{lcm}(m,n) = A$. In other words:

$$ S = \sum_{\substack{\gcd(m,n)=B \\\ \text{lcm}(m,n) = A \\\ m\le n}} (m+n) $$ 

As the value of $S$ can be very large, she wants you to print $S \bmod 10^9+7$.

**Input Format**  
The first line contains an integer $N$, the number of prime factors.  
Each of the next $N$ lines contains three numbers: $p_i$, $b_i$ and $a_i$.

**Output Format**  
Print the value of $S \bmod 10^9+7$.

**Constraints**  

$ 1\le N \le 500$  
$ 2\le p_i \le 5000$  
$ 1\le a_i \le 10^{9}$  
$ 1\le b_i \le 10^{9}$  
$ b_i \le a_i$  


**Sample Input**

	2
    2 1 2 
    3 1 2


**Sample Output**

	72

**Explanation**

We have $B = 6$ and $A = 36$. There are two pairs of integers $(m,n)$ with $\gcd$ equal to $6$ and $\text{lcm}$ equal to $36$, and such that $m \le n$. These are $(12,18)$ and $(6,36)$:

- $\gcd(12,18) = 6$ and $\text{lcm}(12,18) = 36$  
- $\gcd(6,36) = 6$ and $\text{lcm}(6,36) = 36$  

Hence, $S = (12+18)+(6+36) = 72$


## Input Format

The first line contains an integer , the number of prime factors.

Each of the next  lines contains three numbers: ,  and .

## Output Format

Print the value of .

## Sample Input

2 1 2
3 1 2

## Explanation

We have  and . There are two pairs of integers  with  equal to  and  equal to , and such that . These are  and :

-  and

-  and

Hence,
