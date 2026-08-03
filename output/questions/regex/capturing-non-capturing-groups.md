# Capturing & Non-Capturing Groups

---

| Field | Value |
|---|---|
| **Slug** | `capturing-non-capturing-groups` |
| **Domain** | regex |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/capturing-non-capturing-groups |

---

## Preview

Creating capturing and non-capturing group.

## Problem Statement

__$\textsf{( )}$__ 

Parenthesis __( )__ around a regular expression can group that part of regex together. This allows us to apply different [quantifiers](https://msdn.microsoft.com/en-us/library/3206d374(v=vs.110).aspx) to that group.

These parenthesis also create a numbered capturing. It stores the part of string matched by the part of regex inside parentheses.

These numbered capturing can be used for backreferences. ( We shall learn about it later )

<img src="https://s3.amazonaws.com/hr-challenge-images/14621/1449645417-9339477c31-ach16.png" title="ach16.png" />
<sub>$$In \ above \ image \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

__$\textsf{(?: )}$__

__(?: )__ can be used to create a non-capturing group. It is useful if we do not need the group to capture its match.

___
__Task__ 

You have a test String $S$. 

Your task is to write a regex which will match $S$ with the following condition:

- $S$ should have $3$ or more consecutive repetitions of __`ok`__.

__Note__


This is a regex only challenge. You are not required to write a code. 

You have to fill the regex pattern in the blank (`_________`).

## Sample Tests

### Test 1

```
ok
```

### Test 2

```
_________
```
