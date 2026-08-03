# Balanced Strings

---

| Field | Value |
|---|---|
| **Slug** | `balanced-strings` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 40 |
| **Contest** | regular-expresso |
| **URL** | https://www.hackerrank.com/challenges/balanced-strings |

---

## Preview

Find out if a string is balanced using regular expression tools.

## Problem Statement

Consider a string, $s$, consisting only of the letters `a` and `b`. We say that string $s$ is balanced if both of the following conditions are satisfied:

1. $s$ has the same number of occurrences of `a` and `b`.
2. In each prefix of $s$, the number of occurrences of `a` and `b` differ by *at most* $1$.

Your task is to write a regular expression accepting only balanced strings.

## Input Format

Locked stub code in the editor reads a single string denoting $s$ from stdin and uses your RegEx to check it.

## Output Format

You are not responsible for printing anything to stdout. Locked stub code in the editor checks your RegEx against string $s$.

## Constraints

- String $s$ consists of the letters `a` and `b` only.

## Sample Tests

### Test 1

```
ab
```

### Test 2

```
true
```
