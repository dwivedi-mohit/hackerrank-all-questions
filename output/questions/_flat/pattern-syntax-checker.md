# Pattern Syntax Checker

---

| Field | Value |
|---|---|
| **Slug** | `pattern-syntax-checker` |
| **Domain** | java |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/pattern-syntax-checker |

---

## Preview

Given a regex, determine if the pattern is valid or not using Pattern.compile method.

## Problem Statement

Using __Regex__, we can easily match or search for patterns in a text. Before searching for a pattern, we have to specify one using some well-defined syntax.

In this problem, you are given a pattern. You have to check whether the syntax of the given pattern is valid.

**Note**: In this problem, a regex is only valid if you can compile it using the  [Pattern.compile](http://docs.oracle.com/javase/6/docs/api/java/util/regex/Pattern.html#compile%28java.lang.String%29) method.

## Input Format

The first line of input contains an integer $N$, denoting the number of test cases. The next $N$ lines contain a string of any printable characters representing the pattern of a regex.

## Output Format

For each test case, print ``Valid`` if the syntax of the given pattern is correct. Otherwise, print ``Invalid``. Do not print the quotes.

## Sample Tests

### Test 1

```
3
([A-Z])(.+)
[AZ[a-z](a-z)
batcatpat(nat
```

### Test 2

```
Valid
Invalid
Invalid
```
