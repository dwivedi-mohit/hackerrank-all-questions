# Fibonacci LCM

---

| Field | Value |
|---|---|
| **Slug** | `fibonacci-lcm` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/fibonacci-lcm |

---

## Preview

Find the LCM of Fibonacci numbers

## Problem Statement

After Derek (of district 5) discovered how to compute the greatest common divisor (gcd) of Fibonacci numbers, he now tried to answer the next obvious question: how does one compute the *least common multiple* (lcm) of Fibonacci numbers? Unfortunately, Derek found out that this wasn't as easy as the original problem, so he asked you to answer it for him.

The Fibonacci numbers are defined as:

$$F_1 = F_2 = 1$$
$$F_n = F_{n-1} + F_{n-2}$$

Given $N$ integers $a_1, a_2, \ldots, a_N$, find $\text{lcm}(F_{a_1},F_{a_2},\ldots,F_{a_N})$, and give your answer modulo $10^9+7$.

**Input Format**

The first line of input contains $N$.

Each of the next $N$ lines contains a number: the $i^{\text{th}}$ line contains $a_i$.

**Constraints**

$1 \le N \le 100$

$1 \le a_i \le 10^9$


**Output Format**

Print a single integer, which is the least common multiple of the $F_{a_i}$, modulo $10^9+7$.

**Sample Input**


    5
    1
    3
    3
    6
    9

**Sample Output**


    136
  

**Explanation**

$\text{lcm}(F_1,F_3,F_3,F_6,F_9) = \text{lcm}(1,2,2,8,34) = 136$

## Sample Tests

### Test 1

```
5
1
3
3
6
9
```

### Test 2

```
136
```
