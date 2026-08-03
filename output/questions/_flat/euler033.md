# Project Euler #33: Digit canceling fractions

---

| Field | Value |
|---|---|
| **Slug** | `euler033` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 100 |
| **Contest** | projecteuler |
| **URL** | https://www.hackerrank.com/challenges/euler033 |

---

## Preview

Reducing fractions in a sophisticated manner

## Problem Statement

<sub>This problem is a programming version of [Problem 33](https://projecteuler.net/problem=33) from [projecteuler.net](https://projecteuler.net/)</sub>


The fraction $\frac{49}{98}$ is a curious fraction. An inexperienced mathematician while attempting to simplify it may incorrectly believe that $\frac{49}{98} = \frac{4}{8}$ is obtained by cancelling the $9$s.

We shall consider fractions like, $\frac{30}{50} = \frac{3}{5}$, to be trivial examples.


Which means fractions where trailing 0's are cancelled are trivial. So we will ignore all the cases where we have to cancel 0's.  


You will be given 2 integers $N$ and $K$. $N$ represents the number of digits in Numerator and Denominator, and $K$ represents the exact number of digits to be "cancelled" from Numerator and Denominator. Find every non-trivial fraction, 
(1) where numerator is less than denominator, 
(2) and the value of the reduced fraction is equal to the original fraction.

Sum all the Numerators and the Denominators of the original fractions, and print them separated by a space.

## Input Format

Input contains two integers $N$ $K$

## Output Format

Display 2 space separated integers that denote the sum of the Numerators and the sum of the Denominators respectively of original fractions.

**Note** You do not have to reduce the Numerator and Denominator.

## Constraints

$2 \le N \le 4$

$1 \le K \le N-1$

## Sample Tests

### Test 1

```
2 1
```

### Test 2

```
110 322
```
