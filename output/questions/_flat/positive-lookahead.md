# Positive Lookahead

---

| Field | Value |
|---|---|
| **Slug** | `positive-lookahead` |
| **Domain** | regex |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/positive-lookahead |

---

## Preview

A positive lookahead asserts the regex to match if the regexp ahead is matching.

## Problem Statement

__$\textsf{regex_1(?=regex_2)}$__

The positive lookahead (__?=__) asserts `regex_1` to be immediately followed by `regex_2`. The lookahead is excluded from the match. It does not return matches of `regex_2`. The lookahead only asserts whether a match is possible or not. 

<img src="https://s3.amazonaws.com/hr-challenge-images/14901/1449648674-e67416e4d0-ach22.png" title="ach22.png" />
<sub>$$In \ the \ above \ image, \ the \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

__Task__ 

You have a test string $S$.

Write a regex that can match all occurrences of __`o`__ followed immediately by __`oo`__ in $S$.

__Note__


This is a regex only challenge. You are not required to write code. 

You have to fill the regex pattern in the blank (`_________`).

## Sample Tests

### Test 1

```
regex_1
```

### Test 2

```
regex_2
```

### Test 3

```
regex_2
```

### Test 4

```
o
```

### Test 5

```
oo
```

### Test 6

```
_________
```
