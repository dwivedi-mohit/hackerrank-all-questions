# String Construction 

---

| Field | Value |
|---|---|
| **Slug** | `string-construction` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 25 |
| **URL** | https://www.hackerrank.com/challenges/string-construction |

---

## Preview

Find the minimum cost of copying string s.

## Problem Statement

Amanda has a string of lowercase letters that she wants to copy to a new string.  She can perform the following operations with the given costs. She can perform them any number of times to construct a new string $p$:

* Append a character to the end of string $p$ at a cost of $1$ dollar. 
* Choose any [substring](https://en.wikipedia.org/wiki/Substring) of $p$ and append it to the end of $p$ at no charge.

Given $n$ strings $s[i]$, find and print the *minimum* cost of copying each $s[i]$ to $p[i]$ on a new line.

For example, given a string $s = abcabc$, it can be copied for $3$ dollars.  Start by copying $a$, $b$ and $c$ individually at a cost of $1$ dollar per character.  String $p = abc$ at this time.  Copy $p[0:2]$ to the end of $p$ at no cost to complete the copy.


**Function Description**


Complete the *stringConstruction* function in the editor below.  It should return the minimum cost of copying a string.


stringConstruction has the following parameter(s):


- *s*: a string

## Input Format

The first line contains a single integer $n$, the number of strings. 	
Each of the next $n$ lines contains a single string, $s[i]$.

## Output Format

For each string $s[i]$ print the minimum cost of constructing a new string $p[i]$ on a new line.

## Constraints

- $1 \le n \le 5$

- $1 \le |s[i]| \le 10^5$


**Subtasks**

- $1 \le |s[i]| \le 10^3$ for $\text{45%}$ of the maximum score.

## Sample Tests

### Test 1

```
2
abcd
abab
```

### Test 2

```
4
2
```
