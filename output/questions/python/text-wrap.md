# Text Wrap

---

| Field | Value |
|---|---|
| **Slug** | `text-wrap` |
| **Domain** | python |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/text-wrap |

---

## Preview

Wrap the given text in a fixed width.

## Problem Statement

<sub>Check [Tutorial](https://www.hackerrank.com/challenges/text-wrap/tutorial) tab to know how to to solve.</sub>


You are given a string $S$ and width $w$.

Your task is to wrap the string into a paragraph of width $w$.


**Function Description** 


Complete the *wrap* function in the editor below.


*wrap* has the following parameters: 


- *string string:* a long string 

- *int max_width:* the width to wrap to 


**Returns** 


- *string:* a single string with newline characters ('\n') where the breaks should be

## Input Format

The first line contains a string, $string$.

The second line contains the width, $max_width$.

## Constraints

+ $0 < len(string) < 1000$

+ $0 < max_width < len(string)$

## Sample Tests

### Test 1

```
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
```

### Test 2

```
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
```
