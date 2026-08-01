# Maximum Palindromes

- **Domain:** data-structures
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.5568333439227396
- **Total Submissions:** 15739
- **Solved Count:** 8764
- **URL:** https://www.hackerrank.com/challenges/maximum-palindromes

## Problem Statement

Madam Hannah Otto, the CEO of *Reviver* Corp., is fond of palindromes, or words that read the same forwards or backwards. She thinks palindromic brand names are appealing to millennials.  

As part of the marketing campaign for the company's new juicer called the *Rotator*&#8482;, Hannah decided to push the marketing team's palindrome-searching skills to a new *level* with a new challenge.  

In this challenge, Hannah provides a string $s$ consisting of lowercase English letters. Every day, for $q$ days, she would select two integers $l$ and $r$, take the substring $s_{l \ldots r}$ (the substring of $s$ from index $l$ to index $r$), and ask the following question:

Consider all the palindromes that can be constructed from some of the letters from $s_{l \ldots r}$. You can reorder the letters as you need. Some of these palindromes have the maximum length among all these palindromes. How many maximum-length palindromes are there?  

For example, if $s = \texttt{madamimadam}$, $l = 4$ and $r = 7$, then we have,

![image](https://s3.amazonaws.com/hr-assets/0/1514365300-ce2afe4687-palindrome1.png)

Your job as the head of the marketing team is to answer all the queries. Since the answers can be very large, you are only required to find the answer [modulo](https://en.wikipedia.org/wiki/Modulo_operation) $10^9 + 7$.  

Complete the functions `initialize` and `answerQuery` and return the number of maximum-length palindromes modulo $10^9 + 7$. 


## Input Format

The first line contains the string $s$.

The second line contains a single integer $q$.

The $i^\text{th}$ of the next $q$ lines contains two space-separated integers $l_i$, $r_i$ denoting the $l$ and $r$ values Anna selected on the $i^\text{th}$ day.  

## Output Format

For each query, print a single line containing a single integer denoting the answer.

## Constraints

Here, $|s|$ denotes the length of $s$.  

- $1 \leq |s| \leq 10 ^ 5$
- $1 \leq q \leq 10 ^ 5$
- $1 \leq l_i \leq r_i \leq |s|$

**Subtasks**

For 30% of the total score:

- $1 \leq |s| \leq 100$
- $1 \leq q \leq 1000$
- $r_i - l_i \leq 3$

For 60% of the total score:

- $1 \leq |s| \leq 100$
- $1 \leq q \leq 1000$

## Sample Input

week
2
1 4
2 3

## Sample Output

2
1

## Explanation

On the first day,  and . The maximum-length palindromes are "ewe" and "eke".

On the second day,  and . The maximum-length palindrome is "ee".
