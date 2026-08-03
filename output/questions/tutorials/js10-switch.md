# Day 2: Conditional Statements: Switch

---

| Field | Value |
|---|---|
| **Slug** | `js10-switch` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/js10-switch |

---

## Preview

Practice using Switch statements.

## Problem Statement

**Objective**

In this challenge, we learn about *switch statements*. Check out the attached tutorial for more details.

**Task**

Complete the `getLetter(s)` function in the editor. It has one parameter: a string, $s$, consisting of lowercase English alphabetic letters (i.e., `a` through `z`). It must return `A`, `B`, `C`, or `D` depending on the following criteria:

- If the first character in string $s$ is in the set $\{a, e, i, o, u\}$, then return `A`.
- If the first character in string $s$ is in the set $\{b, c, d, f, g\}$, then return `B`.
- If the first character in string $s$ is in the set $\{h, j, k, l, m\}$, then return `C`.
- If the first character in string $s$ is in the set $\{n, p, q, r, s, t, v, w, x, y, z\}$, then return `D`.

**Hint:** You can get the letter at some index $i$ in $s$ using the syntax `s[i]` or `s.charAt(i)`. 


**Function Description** 


Complete the *getLetter* function in the editor below. 


*getLetter* has the following parameters: 


- *string s:*  a string


**Returns** 


- *string:* a single letter determined as described above

## Input Format

Stub code in the editor reads a single string denoting $s$ from stdin.

## Constraints

- $1 \le |s| \le 100$, where $|s|$ is the length of $s$.
- String $s$ contains lowercase English alphabetic letters (i.e., `a` through `z`) only.

## Sample Tests

### Test 1

```
adfgt
```

### Test 2

```
A
```
