# Jerry's Expression

---

| Field | Value |
|---|---|
| **Slug** | `jerrys-expression` |
| **Contest** | hourrank-30 |
| **Difficulty** | Medium |
| **Score** | 45 |
| **URL** | https://www.hackerrank.com/challenges/jerrys-expression |

---

## Problem Statement

This problem revolves around the [Polish notation](http://https://en.wikipedia.org/wiki/Polish_notation). 

- *Polish notation is the way to write parenthesis-free expressions. Its distinguishing feature is that it places operators to the left of their operands.*
- *expression* ::= *number* | (*operator expression expression*)
- *operator* ::= $+$ | $-$ | $\times$ | $\div$ | …
- *For example:  "$(A+B)\times(C-D)$" is "$\times+ AB-CD$"*.

You are given a Polish notation expression. Operators can be only $+$ and $-$.  Each number in expression is replaced with $?$. You have to replace each $?$ with positive integer number, so that value of expression was $0$. Also, you have to make the biggest number in expression as small as possible.

## Input Format

The only line contains string with expression (string will contain only '?', '+' and '-').

## Output Format

Return an integer array, $k^{th}$ number should be the number for $k^{th}$ '?' in the string. If there are many solutions print any.

## Constraints

- $3 \le$ *string length* $ \le 10^6$.
