# Cutting the String

---

| Field | Value |
|---|---|
| **Slug** | `cutting-the-string` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 55 |
| **Contest** | 101hack50 |
| **URL** | https://www.hackerrank.com/challenges/cutting-the-string |

---

## Preview

Find the number of ways to split and merge the string without changing it.

## Problem Statement

In this challenge, you have to cut part of a string and reinsert it without changing the original string. You are given a string $s$ consisting of lowercase English letters. We define $s_{i,j}$ as the substring from the $i$'th to the $j$'th character and $|s|$ as the *length* of string $s$. Two substrings $s_{a,b}$ and $s_{c,d}$ are considered different if the pairs $(a, b)$ and $(c, d)$ are different.


You can cut a nonempty string $s_{i,j}$ out of $s$, where $1 \le i \le j \le |s|$. The remainder after cutting $s_{i,j}$ from $s$ is the *concatenation* of strings $s_{1,i-1}$ and $s_{j+1,|s|}$. Let $r$ denote this string, and let $t$ denote $s_{i,j}$. After cutting, you can insert $t$ back in $r$ at any position. In other words, you can split $r$ into two strings $r = uv$ (either $u$ or $v$ can be empty) and construct the string $utv$. If the resulting string is equal to $s$, you call the process of cutting and inserting *successful*.


The following example illustrates the whole process:
![image](https://s3.amazonaws.com/hr-assets/0/1497795637-8d6f2ad386-14.png "Unsuccessful cutting and insertion")

We start with $s = \texttt{"abracadabra"}$. The substring $s_{2,6} = \texttt{"braca"}$ is cut from the original string yielding the remainder $r = \texttt{"adabra"}$. Then $\texttt{"braca"}$ is reinserted between $\texttt{"ada"}$ and $\texttt{"bra"}$ yielding $\texttt{"adabracabra"}$. This is an example of an *unsuccessful* cutting and insertion since the final string $\texttt{"adabracabra"}$ is different from the original string $\texttt{"abracadabra"}$. 

Find the number of *successful* ways of cutting and inserting a substring, i.e., the number of ways you can cut a substring and insert it back without changing the string.

## Input Format

There is only one line of input containing the string $s$.

## Output Format

Output a single number, the answer to the problem.

## Constraints

* $1 \le |s| \le 6000$
* $s$ consists of lowercase English letters

## Sample Tests

### Test 1

```
aab
```

### Test 2

```
8
```
