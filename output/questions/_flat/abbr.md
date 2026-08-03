# Abbreviation

---

| Field | Value |
|---|---|
| **Slug** | `abbr` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/abbr |

---

## Preview

Make two strings equal

## Problem Statement

You can perform the following operations on the string, $a$:


1. Capitalize zero or more of $a$'s lowercase letters.
2. Delete all of the remaining lowercase letters in $a$.

Given two strings, $a$ and $b$, determine if it's possible to make $a$ equal to $b$ as described. If so, print `YES` on a new line.  Otherwise, print `NO`.


For example, given $a=\text{AbcDE}$ and $b=\text{ABDE}$, in $a$ we can convert $\text{b}$ and delete $\text{c}$ to match $b$.  If $a=\text{AbcDE}$ and $b=\text{AFDE}$, matching is not possible because letters may only be capitalized or discarded, not changed.

**Function Description**

Complete the function $abbreviation$ in the editor below.  It must return either $YES$ or $NO$.

abbreviation has the following parameter(s):

- *a*: the string to modify

- *b*: the string to match

## Input Format

The first line contains a single integer $q$, the number of queries. 

Each of the next $q$ pairs of lines is as follows:

- The first line of each query contains a single string, $a$.

- The second line of each query contains a single string, $b$.

## Output Format

For each query, print `YES` on a new line if it's possible to make string $a$ equal to string $b$.  Otherwise, print `NO`.

## Constraints

+ $1 \leq q \leq 10$

+ $1 \leq |a|, |b| \leq 1000$
+ String $a$ consists only of uppercase and lowercase English letters, ascii[A-Za-z].
+ String $b$ consists only of uppercase English letters, ascii[A-Z].

## Sample Tests

### Test 1

```
1
daBcd
ABC
```

### Test 2

```
YES
```
