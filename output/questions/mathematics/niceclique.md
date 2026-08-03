# Nice Clique

---

| Field | Value |
|---|---|
| **Slug** | `niceclique` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/niceclique |

---

## Preview

Some numbers are better paired up with others; figure out which cliques are nice and which are not.

## Problem Statement

Given a sequence of $n$ numbers, $D = (d_1, d_2, \dots, d_n)$, what's the maximum size of a subsequence of $D$ in which every pair is a *nice pair*?

The pair $(a, b)$ is a nice pair iff at least one of the following condition holds.


1. The [parity](http://en.wikipedia.org/wiki/Parity_(mathematics)) of the number of distinct prime divisors of $a$ is equal to that of $b$. For example, $18$ has two distinct prime divisors: $2$ and $3$.

2. The parity of the sum of all positive divisors of $a$ is equal to that of $b$.

## Input Format

The first line contains a single integer $n$. The second line contains $n$ space-separated integers $d_1, d_2, \dots, d_n$.

## Output Format

Print the maximum size of any subsequence of $D$ in which every pair is a nice pair.

## Constraints

- $1 \le n \le 200$
- $1 \le d_i \le 10^{15}$

## Sample Tests

### Test 1

```
4
2 3 6 8
```

### Test 2

```
3
```
