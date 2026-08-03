# Matching Anything But a Newline

---

| Field | Value |
|---|---|
| **Slug** | `matching-anything-but-new-line` |
| **Domain** | regex |
| **Difficulty** | Easy |
| **Score** | 5 |
| **URL** | https://www.hackerrank.com/challenges/matching-anything-but-new-line |

---

## Preview

Use [.] in the regex expression to match anything but a newline character.

## Problem Statement

[__dot__](http://www.regular-expressions.info/dot.html)


The dot (`.`) matches anything (except for a newline).

<img src="https://s3.amazonaws.com/hr-challenge-images/14095/1449635015-863dfc293f-ach02.png" title="ach02.png" />

<sub>$$In\ the \ above \ image, \ a \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

<sub>**Note**: If you want to match (`.`) in the test string, you need to escape the dot by using a slash `\.`.<br> In Java, use `\\.` instead of `\.`. </sub> 


__Task__


You have a test string $S$.

Your task is to write a regular expression that matches only and exactly strings of form: $abc.def.ghi.jkx$, where each variable $a,b,c,d,e,f,g,h,i,j,k,x$ can be any single character except the newline.

  

__Note__


This is a regex only challenge. You are not required to write any code. 

You only have to fill in the regex pattern in the blank (`_________`).

## Sample Tests

### Test 1

```
.
```

### Test 2

```
.
```

### Test 3

```
\.
```

### Test 4

```
\\.
```

### Test 5

```
\.
```

### Test 6

```
_________
```
