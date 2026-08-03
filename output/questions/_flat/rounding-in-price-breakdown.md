# Rounding in Price Breakdown

---

| Field | Value |
|---|---|
| **Slug** | `rounding-in-price-breakdown` |
| **Domain** |  |
| **Difficulty** | Medium |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/rounding-in-price-breakdown |

---

## Preview

Round the total reservation costs.

## Problem Statement

At Airbnb, you could imagine total reservation costs are computed from a base price and some fees and taxes. The base price may be an integer, but taxes and fees are percentage based, so the total amount could add up to be non-whole number. For example, base price = 100, fee = 2.3 and taxes = 1.4 would lead to a net reservation cost of 103.7. However, we want net reservation cost, to be shown on our website, to be an integer. Given base price, fee and taxes, we would like to round them such that they add up to a desired total while minimizing the rounding error. More formally, we’re going to solve the general case:

Given numbers prices = [x1, x2, ..., xn] and target price target. We want to find a way to round each element in prices such that after rounding, we get rounded numbers roundedPrices = [y1, y2, ...., yn] such that y1+y2+...+yn = target where  yi = Floor(xi) or Ceil(xi), floor or ceiling of xi. We also want to minimize the rounding error given by the sum, Σ |xi-yi| for 1 <= i and i <= n. Return the rounded numbers roundedPrices.

Time Complexity Restrictions

You should implement an algorithm that does not use brute force to solve the problem.

## Input Format

Input Restrictions
The test cases will guarantee that there is a valid unique output of roundedPrices.

## Sample Tests

### Test 1

```
3
0.7
2.8
4.9
8
```

### Test 2

```
0 3 5
```
