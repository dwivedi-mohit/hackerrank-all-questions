# Square Subsequences

- **Domain:** sql
- **Difficulty:** Hard
- **Max Score:** 90
- **Success Ratio:** 0.6770721205597416
- **Total Submissions:** 3716
- **Solved Count:** 2516
- **URL:** https://www.hackerrank.com/challenges/square-subsequences

## Problem Statement

**Square Subsequences**

A string is called a square string if it can be obtained by concatenating two copies of the same string. For example, "abab", "aa" are square strings, while "aaa", "abba" are not. Given a string, how many (non-empty) subsequences of the string are square strings? A subsequence of a string can be obtained by deleting zero or more characters from it, and maintaining the relative order of the remaining characters.

## Input Format

The first line contains the number of test cases, $T$.  
$T$ test cases follow. Each case contains a string, $S$.

## Output Format

Output $T$ lines, one for each test case, containing the required answer modulo 1000000007.

**Constraints:**  
$1 \le T \le 20$  
$S$ will have at most $200$ lowercase characters ('a' - 'z').

## Constraints

will have at most  lowercase characters ('a' - 'z').

## Sample Input

aaa

abab

baaba

## Sample Output

3

6

## Explanation

For the first case, there are 3 subsequences of length 2, all of which are square strings.

For the second case, the subsequences "abab", "aa", "bb" are square strings.

Similarly, for the third case, "bb", "baba" (twice), and "aa" (3 of them) are the square subsequences.
