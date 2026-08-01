# Divisor Exploration

- **Domain:** sql
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.8249336870026526
- **Total Submissions:** 377
- **Solved Count:** 311
- **URL:** https://www.hackerrank.com/challenges/divisor-exploration

## Problem Statement

You are given $D$ datasets where each dataset is in the form of two integers, $m$ and $a$, such that:
$$n = \prod\limits_{i = 1}^{m} p_i^{a+i} \text{, where } p_i \text{ is the } i^{th} \text{ prime.}$$

For each dataset, find and print the following on a new line: 

$$\sum\limits_{d|n} \sigma_{0}(d)$$  

where $\sigma_{0}(x)$ is the count of divisors of $x$. As the answer can be quite large, print the result of this value modulo $(10^9 + 7)$.  

## Input Format

The first line contains an integer, $D$, denoting the number of datasets. 		
Each line $i$ of the $D$ subsequent lines contains two space-separated integers describing the respective values of $m_i$ and $a_i$ for dataset $i$.  

## Output Format

For each dataset, print a single integer denoting the result of the summation above modulo $(10^9 + 7)$ on a new line.

## Constraints

+ $1 \le D \le 10^5$  
+ $1 \le m \le 10^5$  
+ $0 \le a \le 10^5$

## Sample Input

2 0
3 0
2 4

## Sample Output

180
588

## Explanation

For the first dataset where  and ,

 has the following divisors: . Therefore, the result is:

Thus we print the value of  on a new line.
