# Positive Lookbehind

---

| Field | Value |
|---|---|
| **Slug** | `positive-lookbehind` |
| **Domain** | regex |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/positive-lookbehind |

---

## Preview

It asserts the regex to match if regexp behind is matching.

## Problem Statement

__$\textsf{(?<=regex_2)regex_1}$__

The positive lookbehind (__?<=__) asserts `regex_1` to be immediately preceded by `regex_2`. Lookbehind is excluded from the match (do not consume matches of `regex_2`), but only assert whether a match is possible or not. 

<img src="https://s3.amazonaws.com/hr-challenge-images/14903/1449648924-81d5f2a6d0-ach24.png" title="ach24.png" />
<sub>$$In \ above \ image \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

__Task__ 

You have a test String $S$.

Write a regex which can match all the occurences of digit which are immediately preceded by odd digit.

__Note__


This is a regex only challenge. You are not required to write a code. 

You have to fill the regex pattern in the blank (`_________`).

<sub>__`JavaScript do not support lookbehind.`__</sub>

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
_________
```

### Test 5

```
JavaScript do not support lookbehind.
```
