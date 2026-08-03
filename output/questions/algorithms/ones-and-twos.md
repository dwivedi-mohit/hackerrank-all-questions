# Ones and Twos

---

| Field | Value |
|---|---|
| **Slug** | `ones-and-twos` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/ones-and-twos |

---

## Preview

Using A 1's and B 2's how many different evaluations are possible only by performing addition and multiplication

## Problem Statement

You are using at most **A** number of 1s and at most **B** number of 2s. How many different evaluation results are possible when they are formed in an expression containing only addition `+` sign and multiplication `*` sign are allowed?

Note that, multiplication takes precedence over addition.

For example, if **A=2** and **B=2**, then we have the following expressions:

*  `1`, `1*1` = 1
*  `2`, `1*2`, `1*1*2`, `1+1` = 2
*  `1+2`, `1+1*2` = 3
*  `2+2`, `2*2`, `1+1+2`, `1*2*2`, `1*1*2*2`, `1*2+1*2`, `1*1*2+2`, `1*2+2` = 4
*  `1+2+2`, `1+1*2+2` = 5
*  `1+1+2+2`,  `1+1+2*2` = 6

So there are 6 unique results that can be formed if A = 2 and B = 2.

## Input Format

The first line contains the number of test cases T, T testcases follow each in a newline.

Each testcase contains 2 integers A and B separated by a single space.

## Output Format

Print the number of different evaluations modulo (%) (10<sup>9</sup>+7.)

## Constraints

1 <= T <= 10<sup>5</sup>

0<=A<=1000000000

0<=B<=1000

## Sample Tests

### Test 1

```
4
0 0
2 2
0 2
2 0
```

### Test 2

```
0
6
2
2
```
