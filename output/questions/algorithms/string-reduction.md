# String Reduction

---

| Field | Value |
|---|---|
| **Slug** | `string-reduction` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/string-reduction |

---

## Preview

Find the smallest string which can result by repeatedly replacing two characters.

## Problem Statement

Given a string consisting of the letters $\text a$, $\text b$ and $\text c$, we can perform the following operation: 

* Take any two adjacent distinct characters and replace them with the third character. 

Find the shortest string obtainable through applying this operation repeatedly.


For example, given the string $\text{aba}$ we can reduce it to a $1$ character string by replacing $\text{ab}$ with $\text{c}$ and $\text{ca}$ with $\text b$: $\text{aba}\rightarrow\text{ca}\rightarrow\text{b}$.


**Function Description**


Complete the *stringReduction* function in the editor below.  It must return an integer that denotes the length of the shortest string obtainable.


stringReduction has the following parameter:

- *s*: a string

## Input Format

The first line contains the number of test cases $t$.


Each of the next $t$ lines contains a string $s$ to process.

## Output Format

For each test case, print the length of the resultant minimal string on a new line.

## Constraints

* $1 \le t \le 100$
* $1 \lt |s| \le 100$

## Sample Tests

### Test 1

```
3 
cab 
bcab 
ccccc
```

### Test 2

```
2 
1 
5
```
