# Max Transform

- **Domain:** java
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.7868181818181819
- **Total Submissions:** 2200
- **Solved Count:** 1731
- **URL:** https://www.hackerrank.com/challenges/max-transform

## Problem Statement

Transforming data into some other data is typical of a programming job. This problem is about a particular kind of transformation which we'll call the *max transform*.

Let $A$ be a zero-indexed array of integers. For $0 \le i \le j < \mathrm{length}(A)$, let $A_{i\ldots j}$ denote the subarray of $A$ from index $i$ to index $j$, inclusive.

Let's define the *max transform* of $A$ as the array obtained by the following procedure:

- Let $B$ be a list, initially empty.
- For $k$ from $0$ to $\mathrm{length}(A) - 1$:
    - For $i$ from $0$ to $\mathrm{length}(A) - k - 1$:
        - Let $j = i + k$.  
        - Append $\max(A_{i\ldots j})$ to the end of $B$.  
- Return $B$.  

The returned array is defined as the max transform of $A$. We denote it by $S(A)$. 

Complete the function `solve` that takes an integer array $A$ as input.

Given an array $A$, find the sum of the elements of $S(S(A))$, i.e., the *max transform* of the *max transform* of $A$. Since the answer may be very large, only find it modulo $10^9 + 7$.  

## Input Format

The first line of input contains a single integer $n$ denoting the length of $A$.  

The second line contains $n$ space-separated integers $A_0, A_1, \ldots, A_{n-1}$ denoting the elements of $A$.  

## Output Format

Print a single line containing a single integer denoting the answer.  

## Constraints

- $1 \le n \le 2\cdot 10^5$  
- $1 \le A_i \le 10^6$  

**Subtasks**  

- For $33.33\%$ of the total score, $1 \le n \le 4000$  

## Sample Input

3
3 2 1

## Sample Output

58

## Explanation

In the sample case, we have:

Therefore, the sum of the elements of  is .
