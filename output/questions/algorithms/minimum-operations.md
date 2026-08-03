# Minimum Operations

---

| Field | Value |
|---|---|
| **Slug** | `minimum-operations` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 45 |
| **URL** | https://www.hackerrank.com/challenges/minimum-operations |

---

## Problem Statement

In this challenge, the task is to debug the existing code to successfully execute all provided test files.
________________________________________________________________________________________

There are $n$ boxes in front of you. For each $i$, box $i$ contains $r[i]$ red balls, $g[i]$ green balls, and $b[i]$ blue balls. 
 
You want to separate the balls by their color. In each operation, you can pick a single ball from some box and put it into another box. The balls are separated if no box contains balls of more than one color.

Debug the given function `min_operations` and compute the minimal number of operations required to separate the balls.

Note: In this problem you can modify at most *six* lines of code and you cannot add any new lines.

*To restore the original code, click on the icon to the right of the language selector.*

## Input Format

The first line contains a single integer $n$.
The next $n$ lines $i$ contain three space-separated integers, $r[i]$, $g[i]$, and $b[i]$, respectively.

## Output Format

Print the minimal number of operations required to separate the balls. If this is impossible, return $-1$.

## Constraints

$1 \le n \le 100$

$0 \le r[i],\ g[i],\ b[i] \le 105$

## Sample Tests

### Test 1

```
3
1 1 1
1 1 1
1 1 1
```

### Test 2

```
6
```
