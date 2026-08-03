# Project Euler #47: Distinct primes factors

---

| Field | Value |
|---|---|
| **Slug** | `euler047` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 100 |
| **Contest** | projecteuler |
| **URL** | https://www.hackerrank.com/challenges/euler047 |

---

## Preview

Distinct prime factors

## Problem Statement

<sub>This problem is a programming version of [Problem 47](https://projecteuler.net/problem=47) from [projecteuler.net](https://projecteuler.net/)</sub>


The first two consecutive numbers to have two distinct prime factors are:

$$14 = 2 × 7 \\\
 15 = 3 × 5$$
 
The first three consecutive numbers to have three distinct prime factors are:
 $$644 = 2^2 × 7 × 23 \\\
 645 = 3 × 5 × 43 \\\
 646 = 2 × 17 × 19$$

Given $N$ find all the $K$ consecutive integers, where first integer is $\le N$ to have exactly $K$ distinct prime factors. Print the first of these numbers in ascending order.


**Input Format**

Input contains two integers $N$ and $K$.


**Output Format**

Print the answer corresponding to the test case. Print each integer in a new line.


**Constraints**

$20 \le N \le 2 \times 10^6$

$2 \le K \le 4$


**Sample Input#00**

    20 2

**Sample Output#00**

    14
    20
  

**Sample Input#01**


    644 3

**Sample Output**


    644

## Sample Tests

### Test 1

```
20 2
```

### Test 2

```
14
20
```

### Test 3

```
644 3
```

### Test 4

```
644
```
