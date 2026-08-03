# Divisor Exploration

---

| Field | Value |
|---|---|
| **Slug** | `divisor-exploration` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/divisor-exploration |

---

## Preview

Find and print the number of divisors for each dataset.

## Problem Statement

You are given $D$ datasets where each dataset is in the form of two integers, $m$ and $a$, such that:
$$n = \prod\limits_{i = 1}^{m} p_i^{a+i} \text{, where } p_i \text{ is the } i^{th} \text{ prime.}$$

For each dataset, find and print the following on a new line: 

$$\sum\limits_{d|n} \sigma_{0}(d)$$


where $\sigma_{0}(x)$ is the count of divisors of $x$. As the answer can be quite large, print the result of this value modulo $(10^9 + 7)$.

## Input Format

The first line contains an integer, $D$, denoting the number of datasets. 		
Each line $i$ of the $D$ subsequent lines contains two space-separated integers describing the respective values of $m_i$ and $a_i$ for dataset $i$.

## Output Format

For each dataset, print a single integer denoting the result of the summation above modulo $(10^9 + 7)$ on a new line.

## Constraints

+ $1 \le D \le 10^5$

+ $1 \le m \le 10^5$

+ $0 \le a \le 10^5$

## Sample Tests

### Test 1

```
3
2 0
3 0
2 4
```

### Test 2

```
18
180
588
```
