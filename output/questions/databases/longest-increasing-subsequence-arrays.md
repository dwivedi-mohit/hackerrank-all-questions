# Longest Increasing Subsequence Arrays

- **Domain:** databases
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.5095785440613027
- **Total Submissions:** 261
- **Solved Count:** 133
- **URL:** https://www.hackerrank.com/challenges/longest-increasing-subsequence-arrays

## Problem Statement

We define the following:

- A *subsequence* of an array is an ordered subset of the array's elements having the same sequential ordering as the original array. For example, the subsequences of array $[1, 2, 3]$ are $\{1\}$, $\{2\}$, $\{3\}$, $\{1, 2\}$, $\{2, 3\}$, $\{1, 3\}$, and $\{1, 2, 3\}$.
- The [longest increasing subsequence](https://en.wikipedia.org/wiki/Longest_increasing_subsequence) of an array of numbers is the longest possible subsequence that can be created from its elements such that all elements are in increasing order.

Victoria has two integers, $m$ and $n$. She builds unique arrays satisfying the following criteria:

- Each array contains $m$ integers.
- Each integer is $\in [1, n]$.
- The longest increasing subsequence she can create from the array has length $n$.

Given $p$ pairs of $m$ and $n$ values, print the number of arrays Victoria creates for each pair on a new line. As this number can be quite large, print your answer modulo $(10^9+7)$.

## Input Format

The first line contains a single positive integer, $p$, denoting the number of pairs. 		
Each line $i$ of the $p$ subsequent lines contains two space-separated integers describing the respective $m$ and $n$ values for a pair.

## Output Format

On a new line for each pair, print a single integer denoting the number of different arrays Victoria creates modulo $(10^9+7)$.

## Constraints

- $1 \leq p \leq 50$
- $1 \leq m \leq 5 \times 10^5$
- $1 \leq n \leq 10^5$
- $n \leq m$

## Sample Input

4 2
4 3

## Sample Output

9

## Explanation

- Victoria wants to build arrays of integers having size  where each integer is  and each array has a longest increasing subsequence of length  (i.e., contains the subsequence ). She creates the following eleven arrays:
-

-

-

-

-

-

-

-

-

-

-

- Victoria wants to build arrays of integers having size  where each integer is  and each array has a longest increasing subsequence of length  (i.e., contains the subsequence ). She creates the following nine arrays:
-

-

-

-

-

-

-

-

-
