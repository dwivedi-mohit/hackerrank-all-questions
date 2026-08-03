# ginortS

---

| Field | Value |
|---|---|
| **Slug** | `ginorts` |
| **Domain** | python |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/ginorts |

---

## Preview

An uneasy sort.

## Problem Statement

You are given a string $S$. 

$S$ contains alphanumeric characters only.

![](http://i.imgur.com/u7WkSk7.gif)
Your task is to sort the string $S$ in the following manner:

- All sorted *lowercase letters* are ahead of *uppercase letters*. 
- All sorted *uppercase letters* are ahead of digits.
- All sorted *odd digits* are ahead of sorted *even digits*.

## Input Format

A single line of input contains the string $S$.

## Output Format

Output the sorted string $S$.

## Constraints

+ $0 < len(S) < 1000$

## Sample Tests

### Test 1

```
Sorting1234
```

### Test 2

```
ginortS1324
```
