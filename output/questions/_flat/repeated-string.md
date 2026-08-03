# Repeated String

---

| Field | Value |
|---|---|
| **Slug** | `repeated-string` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/repeated-string |

---

## Preview

Find and print the number of letter a's in the first n letters of an infinitely large periodic string.

## Problem Statement

There is a string, $s$, of lowercase English letters that is repeated infinitely many times.  Given an integer, $n$, find and print the number of letter `a`'s in the first $n$ letters of the infinite string.

**Example**

$s=\text{'abcac'}$

$n = 10$


The substring we consider is $abcacabcac$, the first $10$ characters of the infinite string.  There are $4$ occurrences of `a` in the substring.


**Function Description**


Complete the *repeatedString* function in the editor below.


repeatedString has the following parameter(s):


- *s:* a string to repeat

- *n:* the number of characters to consider


**Returns**


- *int:* the frequency of `a` in the substring

## Input Format

The first line contains a single string, $s$. 		
The second line contains an integer, $n$.

## Constraints

* $1 \le |s| \le 100$
* $1 \le n \le 10^{12}$
- For $\text{25%}$ of the test cases, $n \le 10^6$.

## Sample Tests

### Test 1

```
aba
10
```

### Test 2

```
7
```

### Test 3

```
a
1000000000000
```

### Test 4

```
1000000000000
```
