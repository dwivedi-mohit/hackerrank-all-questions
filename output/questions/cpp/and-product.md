# AND Product

- **Domain:** cpp
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.6276543371951819
- **Total Submissions:** 30469
- **Solved Count:** 19124
- **URL:** https://www.hackerrank.com/challenges/and-product

## Problem Statement

Consider two non-negative long integers, $a$ and $b$, where $a \le b$. The [bitwise AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND) of all long integers in the inclusive range between $a$ and $b$ can be expressed as $a \text{ & } (a + 1) \text{ & }  \ldots \text{ & } (b - 1) \text{ & } b$, where $\text{&}$ is the bitwise AND operator. 

Given $n$ pairs of long integers, $a[i]$ and $b[i]$, compute and print the bitwise AND of all natural numbers in the inclusive range between $a[i]$ and $b[i]$.

For example, if $a=10$ and $b=14$, the calculation is $10\ \&\ 11\ \&\ 12\ \&\ 13\ \&\ 14=8$.  

**Function Description**  

Complete the *andProduct* in the editor below.  It should return the computed value as an integer.  

andProduct has the following parameter(s):  

- *a*: an integer  
- *b*: an integer  

## Input Format

The first line contains a single integer $n$, the number of intervals to test.   		
Each of the next $n$ lines contains two space-separated integers $a[i]$ and $b[i]$.

## Output Format

For each pair of long integers, print the bitwise AND of all numbers in the inclusive range between $a[i]$ and $b[i]$ on a new line.

## Constraints

- $1 \le n \le 200$  
- $0 \le a[i] \le b[i] \lt 2^{32}$

## Sample Input

3
12 15
2 3
8 13

## Sample Output

12
2
8

## Explanation

There are three pairs to compute results for:

-  and

, so we print  on a new line.

-  and

-  and
