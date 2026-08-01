# Costly Intervals

- **Domain:** java
- **Difficulty:** Hard
- **Max Score:** 65
- **Success Ratio:** 0.8406805877803558
- **Total Submissions:** 2586
- **Solved Count:** 2174
- **URL:** https://www.hackerrank.com/challenges/costly-intervals

## Problem Statement

Given an array, your goal is to find, for each element, the largest subarray containing it whose cost is at least $k$.

Specifically, let $A = [A_1, A_2, \ldots, A_n]$ be an array of length $n$, and let $A_{l\ldots r} = [A_l, \ldots, A_r]$ be the subarray from index $l$ to index $r$. Also,

- Let $\mathrm{MAX}(l,r)$ be the largest number in $A_{l\ldots r}$.
- Let $\mathrm{MIN}(l,r)$ be the smallest number in $A_{l\ldots r}$.
- Let $\mathrm{OR}(l,r)$ be the [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR) of the elements of $A_{l\ldots r}$.
- Let $\mathrm{AND}(l,r)$ be the [bitwise AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND) of the elements of $A_{l\ldots r}$.

The *cost* of $A_{l\ldots r}$, denoted $\mathit{cost}(l,r)$, is defined as $$\mathit{cost}(l,r) = (\mathrm{OR}(l,r)-\mathrm{AND}(l,r))-(\mathrm{MAX}(l,r)-\mathrm{MIN}(l,r)).$$ The *size* of $A_{l \ldots r}$ is defined as $r - l + 1$.  

You are given the array $A$ and and an integer $k$. For each index $i$ from $1$ to $n$, your goal is to find the largest size of any subarray $A_{l\ldots r}$ such that $1 \le l \le i \le r \le n$ and $\mathit{cost}(l,r) \ge k$.

Consider, array $A = [2,4,3,1,7]$ and $k=6$. The possible sub-arrays and their costs would be as follows: 


![image](https://s3.amazonaws.com/hr-assets/0/1512116739-8dea10a9c6-costly-3.png)

Complete the function `costlyIntervals` which takes two integers $n$ and $k$ as first line of input, and array $A_1, A_2, \ldots, A_n$ in the second line of input. Return an array of $n$ integers, where the $i^\text{th}$ element contains the answer for index $i$ of the input array, $1 \le i \le n$. Every element of the output array denotes the largest size of a subarray containing $i$ whose cost is at least $k$, or $-1$ if there is no such subarray.

## Input Format

  

## Output Format

  

## Constraints

- $1 \le n \le 10^5$  
- $0 \leq A_i \leq 10^9$
- $0 \leq k \leq 10^9$

**Subtasks**  

- For $5\%$ of the maximum score, $n \leq 100$.
- For $15\%$ of the maximum score, $n \leq 5\cdot 10^3$.


## Sample Input

,

## Explanation

In this example, we have . There is only one subarray whose cost is at least , and that is , since . Its size is . Thus, for  and , the answer is , and for the others, .
