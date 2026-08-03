# Sherlock and Anagrams

---

| Field | Value |
|---|---|
| **Slug** | `sherlock-and-anagrams` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/sherlock-and-anagrams |

---

## Preview

Find the number of unordered anagramic pairs of substrings of a string.

## Problem Statement

Two strings are [*anagrams*][123] of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.


**Example**

$s = mom$


The list of all anagrammatic pairs is $[m, m], [mo, om]$ at positions $[[0], [2]], [[0, 1], [1, 2]]$ respectively.

[123]: http://en.wikipedia.org/wiki/Anagram


**Function Description**

Complete the function *sherlockAndAnagrams* in the editor below.


sherlockAndAnagrams has the following parameter(s):

-  *string s:* a string


**Returns**


- *int:* the number of unordered anagrammatic pairs of substrings in $s$

## Input Format

The first line contains an integer $q$, the number of queries. 

Each of the next $q$ lines contains a string $s$ to analyze.

## Constraints

$1 \le q \le 10$ 

$2 \le \text{ length of }s \le 100$

$s$ contains only lowercase letters in the range ascii[a-z].

## Sample Tests

### Test 1

```
2
abba
abcd
```

### Test 2

```
4
0
```

### Test 3

```
2
ifailuhkqq
kkkk
```

### Test 4

```
3
10
```

### Test 5

```
1
cdcd
```

### Test 6

```
5
```
