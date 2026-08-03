# Day 14: All about Scope!

---

| Field | Value |
|---|---|
| **Slug** | `day-14-scope-and-imports` |
| **Contest** | 30-days-of-code |
| **Difficulty** | Easy |
| **Score** | 75 |
| **URL** | https://www.hackerrank.com/challenges/day-14-scope-and-imports |

---

## Problem Statement

Welcome to Day 14, and congratulations on getting halfway through the series! Review *scope* and *importing* [here](https://youtu.be/ylx2U0N2jG4), or just jump right into the problem.

The *absolute difference* between two integers, $a$ and $b$, is $|a - b|$. The *maximum absolute difference* of two integers in a set of positive integers, $elements$, is the largest *absolute difference* of any two integers in $elements$.

The class *Difference* is started for you in the editor. It has a private instance array (`elements`) for storing $N$ non-negative integers, and a public integer (`maxDifference`) for storing the *maximum absolute difference*.

Code for handling Input/Output is provided for you in the editor. Your task is to write the *class constructor* for `Difference` and the `computeDifference` method so that it finds the *maximum absolute difference* between any two numbers in $N$ and stores it in `maxDifference`. 

Good Luck!

## Input Format

The first line contains a positive integer, $N$, denoting the size of array $elements$.	
The second line contains $N$ space-separated positive integers describing $elements$.

**Constraints**  
$1 \le N \le 10$  
$1 \le elements[i]\le 100$, where $ 0\le i \le N - 1 $

## Output Format

Print the *maximum absolute difference* between any two integers in $elements$.
