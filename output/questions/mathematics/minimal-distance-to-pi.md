# Minimal Distance to Pi

---

| Field | Value |
|---|---|
| **Slug** | `minimal-distance-to-pi` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 75 |
| **URL** | https://www.hackerrank.com/challenges/minimal-distance-to-pi |

---

## Preview

Given a range of denominators, find the common fraction that best approximates Pi.

## Problem Statement

Given two long integers, $min$ and $max$, find and print a [common fraction](https://en.wikipedia.org/wiki/Fraction_(mathematics)#Simple.2C_common.2C_or_vulgar_fractions), $\frac{n}{d}$, such that $min \le d \le max$ and $\lvert \frac{n}{d} - \pi \rvert$ is minimal (recall that $\pi \approx 3.1415926535\,8979323846\,2643383279\,5028841971\,693993751$). If there are several fractions having minimal distance to $\pi$, choose the one with the smallest denominator.

## Input Format

Two space-separated long integers describing the respective values of $min$ and $max$.

## Output Format

Print your answer in the form `n/d`, where $n$ is the numerator of the fraction closest to $\pi$ and $d$ is the denominator of that fraction.

## Constraints

* $1 \le min \le max \le 10^{15}$

## Sample Tests

### Test 1

```
1 10
```

### Test 2

```
22/7
```
