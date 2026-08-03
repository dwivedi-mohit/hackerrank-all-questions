# Order of Prime in Factorial

---

| Field | Value |
|---|---|
| **Slug** | `order-of-prime-in-factorial` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/order-of-prime-in-factorial |

---

## Preview

How many factorials have order divisible by that prime?

## Problem Statement

For a given prime $p$, define $\operatorname{ord}_p(k)$ as the multiplicity of $p$ in $k$, i.e. the number of times $p$ appears in the prime factorization of $k$.

For a given $p$ (prime) and $L$, let $F(p,L)$ be the number of integers $n$ such that $1 \le n \le L$ and $\operatorname{ord}_p(n!)$ is divisible by $p$. Here $n!$ denotes the factorial of $n$.

Your job is to calculate $F(p,L)$ given $p$ and $L$.

**Input Format**

The first line contains the number of test cases $T$. 

Each of the next $T$ lines contains two integers $p$ and $L$ separated by a space.

**Output Format**

For each test case, output one line containing $F(p,L)$.


**Constraints**

$1 \le T \le 100000$

$2 \le p \le 10^{18}$

$1 \le L \le 10^{18}$

$p$ is prime

**Sample input**


    2
    2 6
    3 6
  


**Sample Output**


    2
    2

**Explanation** 

Here are the first 6 factorials: 1, 2, 6, 24, 120, 720.


The multiplicities of 2 in these numbers are: 0, 1, 1, 3, 3, 4.

Exactly two of these are divisible by 2 (0 and 4), so $F(2,6) = 2$.

The multiplicities of 3 in these numbers are: 0, 0, 1, 1, 1, 2.

Exactly two of these are divisible by 3 (0 and 0), so $F(3,6) = 2$.

## Sample Tests

### Test 1

```
2
2 6
3 6
```

### Test 2

```
2
2
```
