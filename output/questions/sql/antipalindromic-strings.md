# Anti-Palindromic Strings

- **Domain:** sql
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.6354499771585199
- **Total Submissions:** 2189
- **Solved Count:** 1391
- **URL:** https://www.hackerrank.com/challenges/antipalindromic-strings

## Problem Statement

You are given two integers, $N$ and $M$. Count the number of strings of length $N$ (under the alphabet set of size $M$) that doesn't contain any palindromic string of the length greater than $1$ as a consecutive substring.

## Input Format

Several test cases will be given to you in a single file. The first line of the input will contain a single integer, $T$, the number of test cases.

Then there will be $T$ lines, each containing two space-separated integers, $N$ and $M$, denoting a single test case. The meanings of $N$ and $M$ are described in the Problem Statement above.

## Output Format

For each test case, output a single integer - the answer to the corresponding test case. This number can be huge, so output it modulo $10^9+7$.

**Constraints**  

$1 \leq T \leq 10^5$<br>
$1 \leq N, M \leq 10^9$

## Sample Input

2 2
2 3

## Sample Output

6

## Explanation

For the 1st testcase, we have an alphabet of size M = 2. For the sake of simplicity, let's consider the alphabet as [A, B]. We can construct four strings of size N = 2 using these letters.

AA
AB
BA
BB

Out of these, we have two strings, AB and BA, that satisfy the condition of not having a palindromic string of length greater than 1. Hence, the answer 2.

For the 2nd test case, we have an alphabet of size M = 3. For the sake of simplicity, let's consider the alphabet as [A, B, C]. We can construct nine strings of size N = 2 using these letters.

AA
AB
AC
BA
BB
BC
CA
CB
CC

Save AA, BB, and CC, all the strings satisfy the given condition; hence, the answer 6.
