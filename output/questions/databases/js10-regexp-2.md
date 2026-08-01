# Day 7: Regular Expressions II

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9768850852812381
- **Total Submissions:** 50011
- **Solved Count:** 48855
- **URL:** https://www.hackerrank.com/challenges/js10-regexp-2

## Problem Statement

**Task**

Complete the function in the editor below by returning a *RegExp* object, $re$, that matches any string $s$ satisfying both of the following conditions:

- String $s$ *starts with* the prefix `Mr.`, `Mrs.`, `Ms.`, `Dr.`, or `Er.`
- The remainder of string $s$ (i.e., the rest of the string after the prefix) consists of one or more upper and/or lowercase English alphabetic letters (i.e., `[a-z]` and `[A-Z]`).

## Output Format

The function must return a *RegExp* object that matches any string $s$ satisfying both of the given conditions.

## Constraints

- The length of string $s$ is $\ge$ $3$.

## Sample Input

Mr.X

## Sample Output

true

## Explanation

This string starts with Mr., followed by an English alphabetic letter (X).
