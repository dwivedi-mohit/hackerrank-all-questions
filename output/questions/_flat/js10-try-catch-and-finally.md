# Day 3: Try, Catch, and Finally

---

| Field | Value |
|---|---|
| **Slug** | `js10-try-catch-and-finally` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/js10-try-catch-and-finally |

---

## Preview

Learn to use `try`, `catch`, and 'finally' in JavaScript.

## Problem Statement

**Objective**

In this challenge, we learn about *strings* and *exceptions*. Check out the attached tutorials for more details.

**Task**

Complete the *reverseString* function; it has one parameter, $s$. You must perform the following actions:

1. *Try* to reverse string $s$ using the *split*, *reverse*, and *join* methods.	
2. If an exception is thrown, *catch* it and print the contents of the exception's $message$ on a new line. 
3. Print $s$ on a new line. If no exception was thrown, then this should be the reversed string; if an exception was thrown, this should be the original string.

## Input Format

Locked stub code in the editor reads variable $s$ from stdin and passes it to the function.

## Output Format

You must write two print statements using `console.log()`:

1. Print the contents of a caught exception's $message$ on a new line. If no exception was thrown, this line should not be printed.
2. Print $s$ on a new line. If no exception was thrown, then this should be the reversed string; if an exception was thrown, this should be the original string.

## Sample Tests

### Test 1

```
"1234"
```

### Test 2

```
4321
```

### Test 3

```
Number(1234)
```

### Test 4

```
s.split is not a function
1234
```
