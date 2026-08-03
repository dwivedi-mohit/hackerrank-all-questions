# Palindrome Index

---

| Field | Value |
|---|---|
| **Slug** | `palindrome-index` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 25 |
| **URL** | https://www.hackerrank.com/challenges/palindrome-index |

---

## Preview

Determine which character(s) must be removed to make a string a palindrome.

## Problem Statement

Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be removed to make the string a [palindrome](https://en.wikipedia.org/wiki/Palindrome).  There may be more than one solution, but any will do.  If the word is already a palindrome or there is no solution, return _-1_.  Otherwise, return the index of a character to remove.


**Example**

$s = \text{"bcbc"}$


Either remove *'b'* at index $0$ or *'c'* at index $3$.


**Function Description**


Complete the *palindromeIndex* function in the editor below.  


palindromeIndex has the following parameter(s):


- *string s:* a string to analyze


**Returns**


- *int:* the index of the character to remove or $-1$

## Input Format

The first line contains an integer $q$, the number of queries.		
Each of the next $q$ lines contains a query string $s$.

## Constraints

- $1 \le q \le 20$

- $1 \le \text{length of } s \le 10^5 + 5$

- All characters are in the range ascii[a-z].

## Sample Tests

### Test 1

```
STDIN Function
----- --------
3 q = 3
aaab s = 'aaab' (first query)
baa s = 'baa' (second query)
aaa s = 'aaa' (third query)
```

### Test 2

```
3
0
-1
```
