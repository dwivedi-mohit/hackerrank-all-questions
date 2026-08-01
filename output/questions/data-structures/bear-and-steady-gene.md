# Bear and Steady Gene

- **Domain:** data-structures
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.723996516951771
- **Total Submissions:** 35601
- **Solved Count:** 25775
- **URL:** https://www.hackerrank.com/challenges/bear-and-steady-gene

## Problem Statement

A gene is represented as a string of length $n$ (where $n$ is divisible by $4$), composed of the letters $\text{A}$, $\text{C}$, $\text{T}$, and $\text{G}$.
It is considered to be *steady* if each of the four letters occurs exactly $\frac{n}{4}$ times.  For example, $\text{GACT}$ and $\text{AAGTGCCT}$ are both steady genes.

Bear Limak is a famous biotechnology scientist who specializes in modifying bear DNA to make it steady.  Right now, he is examining a gene represented as a string $gene$.  It is not necessarily steady.  Fortunately, Limak can choose one (maybe empty) substring of $gene$ and replace it with any string of the same length.

Modifying a large substring of bear genes can be dangerous.
Given a string $gene$, can you help Limak find the length of the smallest possible substring that he can replace to make $gene$ a steady gene?

*Note*: A substring of a string $s$ is a subsequence made up of zero or more *contiguous* characters of $s$.

As an example, consider $gene = ACTGAAAG$.  The substring $AA$ just before or after $G$ can be replaced with $CT$ or $TC$.  One selection would create $ACTGACTG$.

**Function Description**

Complete the $steadyGene$ function in the editor below.  It should return an integer that represents the length of the smallest substring to replace.  

steadyGene has the following parameter:  

- *gene*: a string

## Input Format

The first line contains an interger $n$ divisible by $4$, that denotes the length of a string $gene$.  
The second line contains a string $gene$ of length $n$.


## Output Format

Print the length of the minimum length substring that can be replaced to make $gene$ stable.

## Constraints

- $4 \le n \le 500\,000$  
- $n$ is divisible by $4$  
- $gene[i] \in [CGAT]$  

**Subtask**  

- $4 \le n \le 2000$ in tests worth $30\%$ points.

## Sample Input

GAAATAAA

## Explanation

One optimal solution is to replace  with  resulting in .

The replaced substring has length .
