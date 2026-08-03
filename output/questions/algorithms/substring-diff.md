# Substring Diff

---

| Field | Value |
|---|---|
| **Slug** | `substring-diff` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/substring-diff |

---

## Preview

Given two strings P, Q. Find out maximal length L such that there exist a pair (i, j) for that mismatching of P,Q <= S

## Problem Statement

In this problem, we'll use the term "longest common substring" loosely.  It refers to substrings differing at some number or fewer characters when compared index by index.  For example, 'abc' and 'adc' differ in one position, 'aab' and 'aba' differ in two.


Given two strings and an integer $k$, determine the length of the longest common substrings of the two strings that differ in no more than $k$ positions.


For example, $k = 1$.  Strings $s1=abcd$ and $s2=bbca$.  Check to see if the whole string (the longest substrings) matches.  Given that neither the first nor last characters match and $2 > k$, we need to try shorter substrings.  The next longest substrings are $s1' = [abc,bcd]$ and $s2' = [bbc, bca]$.  Two pairs of these substrings only differ in $1$ position: $[abc,bbc]$ and $[bcd,bca]$.  They are of length $3$.


**Function Description**

Complete the *substringDiff* function in the editor below.  It should return an integer that represents the length of the longest common substring as defined.


substringDiff has the following parameter(s):


- *k*: an integer that represents the maximum number of differing characters in a matching pair

- *s1*: the first string

- *s2*: the second string

## Input Format

The first line of input contains a single integer, $t$, the number of test cases follow.

Each of the next $t$ lines contains three space-separated values:  an integer $k$ and two strings, $s1$ and $s2$.

## Output Format

For each test case, output a single integer which is the length of the maximum length common substrings differing at $k$ or fewer positions.

## Constraints

+ $1 \le t \le 10$

+ $0 \le k \le |s1|$ 

+ $|s1| = |s2|$

+ $1 \le |s1|,|s2| \le 1500$
+ All characters in $s1$ and $s2 \in ascii[a-z]$.

## Sample Tests

### Test 1

```
3
2 tabriz torino
0 abacba abcaba
3 helloworld yellomarin
```

### Test 2

```
4
3
8
```
