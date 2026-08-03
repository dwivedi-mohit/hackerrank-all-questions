# Inherited Code

---

| Field | Value |
|---|---|
| **Slug** | `inherited-code` |
| **Domain** | cpp |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/inherited-code |

---

## Preview

Handle errors that can occur in the existing code.

## Problem Statement

You inherited a piece of code that performs username validation for your company's website. The existing function works reasonably well, but it throws an exception when the username is too short. Upon review, you realize that nobody ever defined the exception. 

The inherited code is provided for you in the locked section of your editor. Complete the code so that, when an exception is thrown, it prints `Too short: n` (where $n$ is the length of the given username).

## Input Format

The first line contains an integer, $t$, the number of test cases.

Each of the $t$ subsequent lines describes a test case as a single username string, $u$.

## Output Format

You are not responsible for directly printing anything to stdout. If your code is correct, the locked stub code in your editor will print either `Valid` (if the username is valid), `Invalid` (if the username is invalid), or `Too short: n` (where $n$ is the length of the too-short username) on a new line for each test case.

## Constraints

- $1 \le t \le 1000$

- $1 \le |u| \le 100$

- The username consists only of uppercase and lowercase letters.

## Sample Tests

### Test 1

```
3
Peter
Me
Arxwwz
```

### Test 2

```
Valid
Too short: 2
Invalid
```
