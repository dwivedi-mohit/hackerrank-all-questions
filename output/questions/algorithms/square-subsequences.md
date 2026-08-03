# Square Subsequences

---

| Field | Value |
|---|---|
| **Slug** | `square-subsequences` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 90 |
| **URL** | https://www.hackerrank.com/challenges/square-subsequences |

---

## Preview

How many substrings of a string are square strings, i.e., can be made by concatinating two copies of some other string

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
