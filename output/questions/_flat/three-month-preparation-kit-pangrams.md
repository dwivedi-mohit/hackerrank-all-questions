# Pangrams

---

| Field | Value |
|---|---|
| **Slug** | `three-month-preparation-kit-pangrams` |
| **Domain** |  |
| **Difficulty** | Easy |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/three-month-preparation-kit-pangrams |

---

## Preview

Check whether a given string is a panagram or not.

## Problem Statement

A *pangram* is a string that contains every letter of the alphabet.  Given a sentence determine whether it is a pangram in the English alphabet.  Ignore case.  Return either `pangram` or `not pangram` as appropriate.

**Example**

$s = \text{'The quick brown fox jumps over the lazy dog'}$


The string contains all letters in the English alphabet, so return `pangram`.

**Function Description**

Complete the function *pangrams* in the editor below.  It should return the string `pangram` if the input string is a pangram.  Otherwise, it should return `not pangram`.


pangrams has the following parameter(s):

- *string s:* a string to test


**Returns**


- *string:* either `pangram` or `not pangram`

## Input Format

A single line with string $s$.

## Constraints

$0 \lt \text{ length of } s  \le 10^3$

Each character of $s$, $s[i] \in \{a-z, A-Z, \textit{space}\}$
