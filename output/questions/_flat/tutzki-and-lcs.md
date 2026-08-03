# LCS Returns

---

| Field | Value |
|---|---|
| **Slug** | `tutzki-and-lcs` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/tutzki-and-lcs |

---

## Preview

Find the total number of ways to insert a character in a string such that the length of the longest common subsequence of two strings increases by one.

## Problem Statement

Given two strings, $a$ and $b$, find and print the total number of ways to insert a character at any position in string $a$ such that the length of the [Longest Common Subsequence](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem?oldformat=true) of characters in the two strings increases by one.

## Input Format

The first line contains a single string denoting $a$. 		
The second line contains a single string denoting $b$.

## Output Format

Print a single integer denoting the total number of ways to insert a character into string $a$ in such a way that the length of the longest common subsequence of $a$ and $b$ increases by one.

## Constraints

**Scoring**		

* $1 \le |a|, |b| \le 5000$
* Strings $a$ and $b$ are alphanumeric (i.e., consisting of arabic digits and/or upper and lower case English letters).
* The new character being inserted must also be alphanumeric (i.e., a digit or upper/lower case English letter).

**Subtask**		

* $1 \le |a|, |b| \le 1000$ for $\text{66.67%}$ of the maximum score.

## Sample Tests

### Test 1

```
aa
baaa
```

### Test 2

```
4
```
