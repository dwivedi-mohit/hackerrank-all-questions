# Hyper Strings

---

| Field | Value |
|---|---|
| **Slug** | `hyper-strings` |
| **Domain** | algorithms |
| **Difficulty** | Advanced |
| **Score** | 90 |
| **URL** | https://www.hackerrank.com/challenges/hyper-strings |

---

## Preview

Given a string A, [a-j]{1+}, such that A[i]<A[j] for i>j. Given a set of A, how many strings of length M are possible by concatinating strings from set any no. of times.

## Problem Statement

String $A$ is called a _Super String_ if and only if:

- $A$ contains only letters $a, b, c, d, e, f, g, h, i, j$;
- For any $i$ and $j$, $A[i]$ has lower ascii code than $A[j]$, where $0 \lt i \lt j \lt length(A)$

Given a set of Super Strings $H$, a _Hyper String_ is a string that can be constructed by concatenation of some Super Strings of the set $H$. We can use each Super String as many times as we want.

Given set $H$, you have to compute the number of Hyper Strings with length no greater than $M$.

## Input Format

The first line of input contains two integers, $N$ (the number of Super Strings in $H$) and $M$. The next $N$ lines describe the Super Strings in set $H$.

## Output Format

Output an integer which is the number of possible Hyper Strings that can be derived. Since it may not fit in $32$ bit integer, print the output module $1000000007$. (i.e. answer = answer % $1000000007$)

## Constraints

$N$ and $M$ are not greater than $100$.

## Sample Tests

### Test 1

```
2 3 
a 
ab
```

### Test 2

```
7
```
