# Java Anagrams

---

| Field | Value |
|---|---|
| **Slug** | `java-anagrams` |
| **Domain** | java |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/java-anagrams |

---

## Preview

Given two strings, determine of they are anagrams of each other.

## Problem Statement

Two strings, $a$ and $b$, are called anagrams if they contain all the same characters in the same frequencies.  For this challenge, the test is not case-sensitive. For example, the anagrams of `CAT` are `CAT`, `ACT`, `tac`, `TCA`, `aTC`, and `CtA`.

**Function Description**  


Complete the *isAnagram* function in the editor. 


*isAnagram* has the following parameters:


- *string a:* the first string 

- *string b:* the second string 


**Returns** 


- *boolean:* If $a$ and $b$ are case-insensitive anagrams, return true.  Otherwise, return false.

## Input Format

The first line contains a string $a$.		
The second line contains a string $b$.

## Constraints

- $1 \le length(a), length(b) \le 50$
- Strings $a$ and $b$ consist of English alphabetic characters.
- The comparison should NOT be case sensitive.

## Sample Tests

### Test 1

```
anagram
margana
```

### Test 2

```
Anagrams
```

### Test 3

```
anagramm
marganaa
```

### Test 4

```
Not Anagrams
```

### Test 5

```
Hello
hello
```

### Test 6

```
Anagrams
```
