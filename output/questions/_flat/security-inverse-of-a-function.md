# Security Function Inverses

---

| Field | Value |
|---|---|
| **Slug** | `security-inverse-of-a-function` |
| **Domain** | security |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/security-inverse-of-a-function |

---

## Preview

Find the inverse of a given function f.

## Problem Statement

Consider a *bijective* function $f: X\rightarrow Y$.

Define another function $g: Y\rightarrow X$ so that for $x \in X$ and $y \in Y$ if $f(x) = y$ then $g(y) = x$.  <br>

Now, the function $g$ is said to be the inverse function of $f$ and is denoted as $g = f^{-1}$.

In this task, you'll be given an integer $n$ and a bijective function $f: X\rightarrow X$ where $X = \{1, 2, 3, ..., n\}$. <br>

Output the inverse of $f$.

## Input Format

There are $2$ lines in the input. <br>
The first line contains a single positive integer $n$. <br>
The second line contains $n$ space separated integers, the values of $f(1),\ f(2),\ f(3),\ ...,\ f(n)\ $, respectively.

## Output Format

Output $n$ lines. The $i^{th}$ line should contain the value of $f^{-1}(i)$.


**Sample Input#00**


	3
    1 2 3
  

**Sample Output#00**


    1
    2
    3
  

**Sample Input#01**


    3
    2 3 1
  

**Sample Output#01**


    3
    1
    2

## Constraints

$1 \le n \le 20$

## Sample Tests

### Test 1

```
3
1 2 3
```

### Test 2

```
1
2
3
```

### Test 3

```
3
2 3 1
```

### Test 4

```
3
1
2
```
