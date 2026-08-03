# Binomial Coefficients

---

| Field | Value |
|---|---|
| **Slug** | `binomial-coefficients` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/binomial-coefficients |

---

## Preview

Calculate how many binomial coefficients of n become 0 after modulo by P.

## Problem Statement

In mathematics, **binomial coefficients** are a family of positive integers that occur as coefficients in the binomial theorem.  
$$n\choose k$$
denotes the number of ways of choosing k objects from n different objects.

However when n and k are too large, we often save them after modulo operation by a prime number P. Please calculate how many binomial coefficients of n become to 0 after modulo by P.

**Input Format**

The first of input is an integer $T$, the number of test cases.

Each of the following $T$ lines contains 2 integers, $n$ and prime $P$.


**Constraints**

$T < 100$

$n < 10^{500}$

$P < 10^9$

**Output Format**

For each test case, output a line contains the number of   $n \choose k$s (0<=k<=n)  each of which after modulo operation by P is 0.

**Sample Input**

    3
    2 2
    3 2
    4 3

**Sample Output**

    1
    0
    1

## Sample Tests

### Test 1

```
3
2 2
3 2
4 3
```

### Test 2

```
1
0
1
```
