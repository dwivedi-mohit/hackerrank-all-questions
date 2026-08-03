# Subsequence Again

---

| Field | Value |
|---|---|
| **Slug** | `subsequence-3` |
| **Contest** | codeagon-2017 |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/subsequence-3 |

---

## Problem Statement

You are provided with a string $s$ and an integer $k$. You have to find another string $t$ which satisfies the following conditions:

* $t$ must be a subsequence of $s$.
* Every character in $t$ must occur *at least* $k$ times. 
* The length of $t$ must be as large as possible.
* If there are multiple strings for $t$ with largest possible length, pick the lexicographically smallest one.

For example, let's say the string is $s=$ ``hackerrank`` and $k=2$. 

![image](https://s3.amazonaws.com/hr-assets/0/1497940453-503c98b605-subsequence.png)

The solution for this is $t=$ ``akrrak``. Here $t$ is a subsequence of $k$, it contains the characters $a$, $k$ and $r$ repeated at least $k=2$ times. And, it is the only longest possible subsequence that satisfies the conditions.

## Input Format

The first line contains a string $s$ denoting the original string.		
 The second line contains an integer $k$.

## Output Format

Print the string $t$ on a single line.

## Constraints

* $ 1 \le |s| \le 10^5 $
* $ 1 \le k \le 10^5 $
* String $s$ will only contain lowercase English characters.
* Every input will have a valid solution.
