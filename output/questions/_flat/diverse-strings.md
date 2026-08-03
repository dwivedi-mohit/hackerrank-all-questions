# Diverse Strings

---

| Field | Value |
|---|---|
| **Slug** | `diverse-strings` |
| **Contest** | hourrank-30 |
| **Difficulty** | Hard |
| **Score** | 75 |
| **URL** | https://www.hackerrank.com/challenges/diverse-strings |

---

## Problem Statement

In this challenge, we introduce the concept of *assorted* and *diversed* strings. 

- A string $s$ is called *assorted* if no two distinct letters in $s$ appear the same number of times. For example, `aacbcc` is assorted, but `aabaccab` is not assorted, since `b` and `c` each appears exactly $2$ times.
- A string $s$ is called *diverse* if it is assorted and all its prefixes and suffixes are assorted. For example, `aabaa` is diverse, but `aaba` is not diverse, since the suffix `ba` is not assorted.  

Given $n$ and $k$, find the lexicographically smallest *diverse* string of length $n$ with exactly $k$ distinct letters. Your output string can only contain lowercase English letters. If no such string exists, output `NONE`.

## Input Format

The first line of input contains $q$, the number of queries.  

Each query consists of a single line containing two space-separated integers $n$ and $k$.

## Output Format

For each case, output a single line containing the required diverse string, or the string `NONE` if no such string exists.

## Constraints

- $1 \le q \le 60$  
- $1 \le n \le 10^5$  
- $1 \le k \le 26$  
- $n \ge k$
