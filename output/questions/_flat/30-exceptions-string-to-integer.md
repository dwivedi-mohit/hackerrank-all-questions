# Day 16: Exceptions - String to Integer

---

| Field | Value |
|---|---|
| **Slug** | `30-exceptions-string-to-integer` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/30-exceptions-string-to-integer |

---

## Preview

Can you determine if a string can be converted to an integer?

## Problem Statement

**Objective**		
Today, we're getting started with *Exceptions* by learning how to parse an integer from a string and print a custom error message. Check out the [Tutorial](/challenges/30-exceptions-string-to-integer/tutorial) tab for learning materials and an instructional video!

**Task**	
Read a string, $S$, and print its integer value; if $S$ cannot be converted to an integer, print `Bad String`.

**Note:** You *must* use the String-to-Integer and exception handling constructs built into your submission language. If you attempt to use loops/conditional statements, you will get a $0$ score.

## Input Format

A single string, $S$.

## Output Format

Print the parsed integer value of $S$, or `Bad String` if $S$ cannot be converted to an integer.

**Sample Input 0**

	3

**Sample Output 0**

	3

**Sample Input 1**

	za

**Sample Output 1**

	Bad String

## Constraints

- $1 \le \left|S\right| \le 6$, where $\left|S\right|$ is the length of string $S$.
- $S$ is composed of *either* lowercase letters ($a-z$) *or* decimal digits ($0-9$).

## Sample Tests

### Test 1

```
3
```

### Test 2

```
3
```

### Test 3

```
za
```

### Test 4

```
Bad String
```
