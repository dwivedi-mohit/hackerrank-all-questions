# LCM and GCD

---

| Field | Value |
|---|---|
| **Slug** | `lcm-and-gcd` |
| **Domain** | misc |
| **Difficulty** | Advanced |
| **Score** | 150 |
| **Contest** | 101hack22 |
| **URL** | https://www.hackerrank.com/challenges/lcm-and-gcd |

---

## Problem Statement

Churu is interested in finding the $LG(S) $ of a given set $S$, but he finds the problem very hard. Help him solve the problem.

$$ LG(S) = \sum_{s \in \text{subset of S} }  LCM(s)* GCD(s)$$

$$ LCM(a_{1},a_{2},...,a_{n}) = LCM(a_{1},LCM(a_{2},...LCM(a_{n-1},a_{n}))) $$
$$ GCD(a_{1},a_{2},...,a_{n}) = GCD(a_{1},GCD(a_{2},...GCD(a_{n-1},a_{n}))) $$

As the value of $LG(S)$ can be very large, print it modulo $10^7$. [LCM](http://en.wikipedia.org/wiki/Least_common_multiple) and [GCD](http://en.wikipedia.org/wiki/Greatest_common_divisor) are the standard notations. For the singleton set, $GCD$ and $LCM$ will be the number only. For example, $GCD$ of $S = ${$x$}, will be $x$ only. Consider the $LCM$ and $GCD$ of a null set as $0$.<br>

## Input Format

The first line contains $T$, the number of test cases. $T$ test cases follow.

The first line of each test case contains $N$, the number of elements; the next line contains $N$ distinct space-separated positive integers.

**Constraints**

$1 \le T \le 50$

$2 \le N \le 100$

Numbers in the array are in the range $[1, 250]$

$2 \le$ _Sum of $N$ over all test cases_ $\le 100$

## Output Format

For every test case, output the sum in a newline.

## Sample Tests

### Test 1

```
2 
2 
2 3 
3 
2 4 10
```

### Test 2

```
19 
228
```
