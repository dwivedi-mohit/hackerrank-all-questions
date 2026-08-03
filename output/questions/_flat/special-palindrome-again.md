# Special String Again

---

| Field | Value |
|---|---|
| **Slug** | `special-palindrome-again` |
| **Domain** |  |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/special-palindrome-again |

---

## Preview

Find Special sub-strings in a string.

## Problem Statement

A string is said to be a *special string* if either of two conditions is met:


- All of the characters are the same, e.g. `aaa`.
- All characters except the middle one are the same, e.g. `aadaa`.

A *special substring* is any substring of a string which meets one of those criteria.  Given a string, determine how many special substrings can be formed from it.


**Example** 

$s = \texttt{mnonopoo}$ 


$s$ contains the following $12$ special substrings:  $\texttt{\{m, n, o, n, o, p, o, o, non, ono, opo, oo\}}$. 


**Function Description**

Complete the *substrCount* function in the editor below. 


substrCount has the following parameter(s):

- *int n*: the length of string *s*
- *string s*: a string

**Returns** 

- *int:* the number of special substrings

## Input Format

The first line contains an integer, $n$, the length of $s$.

The second line contains the string $s$.

## Constraints

$1 \le n \le 10^6$

Each character of the string is a lowercase English letter, $\texttt{ascii[a-z]}$.

## Sample Tests

### Test 1

```
5
asasd
```

### Test 2

```
7
```

### Test 3

```
7
abcbaba
```

### Test 4

```
10
```

### Test 5

```
4
aaaa
```

### Test 6

```
10
```
