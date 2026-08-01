# Yet Another Minimax Problem

- **Domain:** cpp
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.4613686534216336
- **Total Submissions:** 6795
- **Solved Count:** 3135
- **URL:** https://www.hackerrank.com/challenges/yet-another-minimax-problem

## Problem Statement

You are given $n$ non-negative integers, $a_0, a_1, \ldots, a_{n-1}$. We define the *score* for some permutation ($p$) of length $n$ to be the maximum of $a_{p_{i}} \oplus a_{p_{i+1}}$ for $0 \le i \lt n-1$. 

Find the permutation with the minimum possible score and print its score.

**Note:** $\oplus$ is the [exclusive-OR](https://en.wikipedia.org/wiki/Exclusive_or) (XOR) operator.

## Input Format

The first line contains single integer, $n$, denoting the number of integers. 	
The second line contains $n$ space-separated integers, $a_0, a_1, \ldots, a_{n-1}$, describing the respective integers.

## Output Format

Print a single integer denoting the minimum possible score.

**Sample Input 0**

	4
    1 2 3 4
    
**Sample Output 0**

	5

**Sample Input 1**

    3
    1 2 3
    
**Sample Output 1**

	2

## Constraints

- $2 \le n \le 3000$
- $0 \le a_i \le 10^9$

## Sample Input

4
1 2 3 4

## Sample Output

5

## Explanation

Sample Case 0:

The permutation with the minimum score is :

Because the permutation's score is the maximum of these values, we print  on a new line.

Sample Case 1:

The permutation with the minimum score is :

Because the permutation's score is the maximum of these values, we print  on a new line.
