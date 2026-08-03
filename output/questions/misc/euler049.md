# Project Euler #49: Prime permutations

---

| Field | Value |
|---|---|
| **Slug** | `euler049` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 100 |
| **Contest** | projecteuler |
| **URL** | https://www.hackerrank.com/challenges/euler049 |

---

## Preview

Prime permutations

## Problem Statement

<sub>This problem is a programming version of [Problem 49](https://projecteuler.net/problem=49) from [projecteuler.net](https://projecteuler.net/)</sub>


The arithmetic sequence, $1487, 4817, 8147$ in which each of the terms increases by $3330$ is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.


There are no arithmetic sequences made up of three $1-$, $2-$, or $3-digit$ primes, exhibiting this property.

You are given $N$ and $K$, find all $K$ size sequences where first element is less than $N$ and $K$ elements are permutations of each other, are prime and are in AP(Arithmetic Progression).


Print the answer as concatenated integer formed by joining $K$ terms.

## Input Format

Input contains two integers $N$ and $K$

## Output Format

Print the answer corresponding to the test case. each in new line in numerically sorted order of smallest value.

## Constraints

$2000 \le N \le 1000000$

$3 \le K \le 4$

## Sample Tests

### Test 1

```
2000 3
```

### Test 2

```
148748178147
```
