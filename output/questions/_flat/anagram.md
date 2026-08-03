# Anagram

---

| Field | Value |
|---|---|
| **Slug** | `anagram` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 25 |
| **URL** | https://www.hackerrank.com/challenges/anagram |

---

## Preview

Find the minimum number of characters of the first string that we need to change in order to make it an anagram of the second string.

## Problem Statement

Two words are [*anagrams*](https://en.wikipedia.org/wiki/Anagram) of one another if their letters can be rearranged to form the other word.


Given a string, split it into two contiguous substrings of equal length.  Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

**Example** 

$s = \text{abccde}$


Break $s$ into two parts: 'abc' and 'cde'.  Note that all letters have been used, the substrings are contiguous and their lengths are equal.  Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams.  Two changes were necessary.


**Function Description**

Complete the *anagram* function in the editor below.  


anagram has the following parameter(s):


- *string s:* a string


**Returns**


- *int:* the minimum number of characters to change or -1.

## Input Format

The first line will contain an integer, $q$, the number of test cases.

Each test case will contain a string $s$.

## Constraints

- $1 \le q \le 100$ <br>
- $1 \le |s| \le 10^4$

- $s$ consists only of characters in the range ascii[a-z].

## Sample Tests

### Test 1

```
6
aaabbb
ab
abc
mnop
xyyx
xaxbbbxx
```

### Test 2

```
3
1
-1
2
0
1
```
