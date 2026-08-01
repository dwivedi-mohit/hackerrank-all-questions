# Array Pairs

- **Domain:** fp
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.267913841929117
- **Total Submissions:** 23306
- **Solved Count:** 6244
- **URL:** https://www.hackerrank.com/challenges/array-pairs

## Problem Statement

Consider an array of $n$ integers, $A = [a_1, a_2, \ldots, a_{n}]$. Find and print the total number of $(i,j)$ pairs such that $a_i \times a_j \le max(a_i, a_{i+1}, \ldots, a_j)$ where $i \lt j$. 

## Input Format

The first line contains an integer, $n$, denoting the number of elements in the array. 		
The second line consists of $n$ space-separated integers describing the respective values of $a_1, a_2, \ldots, a_{n}$.

## Output Format

Print a long integer denoting the total number $(i, j)$ pairs satisfying $a_i \times a_j \le max(a_i, a_{i+1}, \ldots, a_j)$ where $i \lt j$. 

## Constraints

- $1 \le n \le 5 \times 10^5$
- $1 \le a_i \le 10^9$

**Scoring** 

- $1 \le n \le 1000$ for $\text{25%}$ of the test cases.
- $1 \le n \le 10^5$ for $\text{50%}$ of the test cases.
- $1 \le n \le 5 \times 10^5$ for $\text{100%}$ of the test cases.


## Sample Input

1 1 2 4 2

## Explanation

There are eight pairs of indices satisfying the given criteria: , , , , , , , and . Thus, we print  as our answer.
