# Polynomial Division

---

| Field | Value |
|---|---|
| **Slug** | `polynomial-division` |
| **Domain** | data-structures |
| **Difficulty** | Hard |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/polynomial-division |

---

## Preview

Determine if polynomial division between varying degree polynomials is possible without a remainder.

## Problem Statement

Consider a sequence, $c_0, c_1, \dots c_{n-1}$, and a polynomial of degree $1$ defined as $Q(x) = a \cdot x + b$. You must perform $q$ queries on the sequence, where each query is one of the following two types:

- `1 i x`: Replace $c_i$ with $x$.
- `2 l r`: Consider the polynomial $P(x) = c_{l} \cdot x^0 + c_{l+1} \cdot x^1 + \dots + c_{r} \cdot x^{r-l}$ and determine whether $P(x)$ is divisible by $Q(x) = a \cdot x + b$ over the field $Z_p$, where $p = 10^9 + 7$. In other words, check if there exists a polynomial $R(x)$ with integer coefficients such that each coefficient of $P(x) - R(x) \cdot Q(x)$ is divisible by $p$. If a valid $R(x)$ exists, print `Yes` on a new line; otherwise, print `No`.

Given the values of $n$, $a$, $b$, and $q$ queries, perform each query in order.

## Input Format

The first line contains four space-separated integers describing the respective values of $n$ (the length of the sequence), $a$ (a coefficient in $Q(x)$), $b$ (a coefficient in $Q(x)$), and $q$ (the number of queries).		
The second line contains $n$ space-separated integers describing $c_0, c_1, \dots c_{n-1}$.			
Each of the $q$ subsequent lines contains three space-separated integers describing a query of either type `1` or type `2`.

## Output Format

For each query of type `2`, print `Yes` on a new line if $Q(x)$ is a divisor of $P(x)$; otherwise, print `No` instead.

## Constraints

- $1 \le n, q \le 10^5$
- For query type `1`: $0 \le i \le n - 1$ and $0 \le x < 10^9 + 7$.
- For query type `2`: $0 \le l \le r \le n - 1$.
- $0 \le a, b, c_i < 10^9 + 7$
- $a \ne 0$

## Sample Tests

### Test 1

```
3 2 2 3
1 2 3
2 0 2
1 2 1
2 0 2
```

### Test 2

```
No
Yes
```
