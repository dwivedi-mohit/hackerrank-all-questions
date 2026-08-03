# Day 7: Regular Expressions II

---

| Field | Value |
|---|---|
| **Slug** | `js10-regexp-2` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/js10-regexp-2 |

---

## Preview

Write a JavaScript RegExp to match a name satisfying certain criteria.

## Problem Statement

**Task**

Complete the function in the editor below by returning a *RegExp* object, $re$, that matches any string $s$ satisfying both of the following conditions:

- String $s$ *starts with* the prefix `Mr.`, `Mrs.`, `Ms.`, `Dr.`, or `Er.`
- The remainder of string $s$ (i.e., the rest of the string after the prefix) consists of one or more upper and/or lowercase English alphabetic letters (i.e., `[a-z]` and `[A-Z]`).

## Output Format

The function must return a *RegExp* object that matches any string $s$ satisfying both of the given conditions.

## Constraints

- The length of string $s$ is $\ge$ $3$.

## Sample Tests

### Test 1

```
Mr.X
```

### Test 2

```
true
```

### Test 3

```
Mrs.Y
```

### Test 4

```
true
```

### Test 5

```
Dr#Joseph
```

### Test 6

```
false
```

### Test 7

```
Er .Abc
```

### Test 8

```
false
```
