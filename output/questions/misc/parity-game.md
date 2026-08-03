# Parity Game

---

| Field | Value |
|---|---|
| **Slug** | `parity-game` |
| **Contest** | hourrank-22 |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/parity-game |

---

## Problem Statement

Mancunian is playing the famous Parity Game. In this game, the player is given an array $A$ comprising of $n$ positive integers. The goal is to remove some (possibly empty) subsequence of these integers so that the sum of the resulting array is even. The player is **NOT** allowed to remove all the numbers (i.e. the resulting array should be nonempty).  

There can be multiple possible subsequences that can be removed to achieve this. Print the size of the smallest such subsequence. If there is no such subsequence, print $-1$.

## Input Format

The first line of input contains the size of the array, $n$.  
The second line contains $n$ space-separated integers, the $i^\text{th}$ of which contains $A_i$.

## Output Format

Print a single integer which is the answer to the given problem.

## Constraints

- $1 \le n \le 10^{3}$  
- $1 \le A_i \le 10^{3}$
