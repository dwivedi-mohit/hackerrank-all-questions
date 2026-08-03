# P-sequences

---

| Field | Value |
|---|---|
| **Slug** | `p-sequences` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/p-sequences |

---

## Preview

How many sequences of N elements are there if product of two adjacent elements is not greater than P

## Problem Statement

We call a sequence of `N` natural numbers (*a*<sub>1</sub>, *a*<sub>2</sub>, ..., *a*<sub>N</sub>) a *P-sequence*, if the product of any two adjacent numbers in it is not greater than *P*. In other words, if a sequence (*a*<sub>1</sub>, *a*<sub>2</sub>, ..., *a*<sub>N</sub>) is a *P-sequence*, then *a*<sub>i</sub> * *a*<sub>i+1</sub> &le; `P` &forall; 1 &le; i &lt; N

You are given `N` and `P`. Your task is to find the number of such *P-sequences* of `N` integers modulo 10<sup>9</sup>+7.

## Input Format

The first line of input consists of `N`

The second line of the input consists of `P`.

## Output Format

Output the number of *P-sequences* of `N` integers modulo 10<sup>9</sup>+7.

## Constraints

2 &le; N &le; 10<sup>3</sup>

1 &le; P &le; 10<sup>9</sup>

1 &le; a<sub>i</sub>

## Sample Tests

### Test 1

```
2
2
```

### Test 2

```
3
```
