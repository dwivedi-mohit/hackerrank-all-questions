# Matching Whitespace & Non-Whitespace Character

---

| Field | Value |
|---|---|
| **Slug** | `matching-whitespace-non-whitespace-character` |
| **Domain** | regex |
| **Difficulty** | Easy |
| **Score** | 5 |
| **URL** | https://www.hackerrank.com/challenges/matching-whitespace-non-whitespace-character |

---

## Preview

Use \s to match whitespace and \S to match non whitespace characters in this challenge.

## Problem Statement

__$\textsf{\s}$__

__\s__ matches any whitespace character __`[ \r\n\t\f ]`__.

<img src="https://s3.amazonaws.com/hr-challenge-images/14233/1449636160-8b65ab3bd0-ach05_01.png" title="ach05_01.png" />
<sub>$$In \ the \ above \ image, \ the \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>
___
__$\textsf{\S}$__

__\S__ matches any non-white space character.

<img src="https://s3.amazonaws.com/hr-challenge-images/14233/1449636254-93a53af3f6-ach05_02.png" title="ach05_02.png" />
<sub>$$In \ above \ image \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

__Task__ 

You have a test string $S$. Your task is to match the pattern $XXxXXxXX$ 

Here, $x$ denotes whitespace characters, and $X$ denotes non-white space characters.

__Note__


This is a regex only challenge. You are not required to write code. 

You have to fill the regex pattern in the blank (`_________`).

## Sample Tests

### Test 1

```
[ \r\n\t\f ]
```

### Test 2

```
_________
```
