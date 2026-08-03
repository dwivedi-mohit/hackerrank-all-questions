# Extra Long Factorials

---

| Field | Value |
|---|---|
| **Slug** | `extra-long-factorials` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/extra-long-factorials |

---

## Preview

Calculate a very large factorial that doesn't fit in the conventional numeric data types.

## Problem Statement

The *factorial* of the integer $n$, written $n!$, is defined as: 


$$n! = n \times (n-1) \times (n-2) \times \cdots \times 3 \times 2 \times 1$$

Calculate and print the factorial of a given integer.


For example, if $n = 30$, we calculate $30 \times 29 \times 28 \times \cdots \times 2 \times 1$ and get $265252859812191058636308480000000$.

**Function Description**

Complete the *extraLongFactorials* function in the editor below.  It should print the result and return.


extraLongFactorials has the following parameter(s):


- *n*: an integer

**Note:** Factorials of $n > 20$ can't be stored even in a $64-bit$ long long variable. Big integers must be used for such calculations. Languages like Java, Python, Ruby etc. can handle big integers, but we need to write additional code in C/C++ to handle huge values.


We recommend solving this challenge using BigIntegers.

## Input Format

Input consists of a single integer $n$

## Output Format

Print the factorial of $n$.

## Constraints

$1 \le n \le 100$
