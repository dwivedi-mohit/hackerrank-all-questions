# Primitive Problem

---

| Field | Value |
|---|---|
| **Slug** | `primitive-problem` |
| **Domain** | mathematics |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/primitive-problem |

---

## Preview

Find the primitive roots of a prime number.

## Problem Statement

We define a *primitive root* of prime number $p$ to be some integer $g \in [1, p-1]$ satisfying the property that all values of $g^x \bmod p$ where $x \in [0, p - 2]$ are different. 

For example: if $p = 7$, we want to look at all values of $g$ in the inclusive range from $1$ to $p - 1 = 6$. For $g = 3$, the powers of $g^x \bmod p$ (where $x$ is in the inclusive range from $0$ to $p - 2 = 5$) are as follows:

- $3^0=1 \pmod 7$

- $3^1=3 \pmod 7$

- $3^2=2 \pmod 7$

- $3^3=6 \pmod 7$

- $3^4=4 \pmod 7$

- $3^5=5 \pmod 7$

Note that each of these evaluates to one of the six distinct integers in the range $[1, p-1]$.

Given prime $p$, find and print the following values as two space-separated integers on a new line:

1. The smallest primitive root of prime $p$.
2. The total number of primitive roots of prime $p$.


**Need Help?** Check out a breakdown of this process at [Math Stack Exchange](http://math.stackexchange.com/questions/124408/finding-a-primitive-root-of-a-prime-number).

## Input Format

A single prime integer denoting $p$.

## Output Format

Print two space-separated integers on a new line, where the first value is the smallest primitive root of $p$ and the second value is the total number of primitive roots of $p$.

## Constraints

+ $2 < p < 10^9$

## Sample Tests

### Test 1

```
7
```

### Test 2

```
3 2
```
