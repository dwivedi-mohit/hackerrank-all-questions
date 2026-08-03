# Cycle Representation

---

| Field | Value |
|---|---|
| **Slug** | `cycle-representation` |
| **Domain** | mathematics |
| **Difficulty** | Expert |
| **Score** | 120 |
| **URL** | https://www.hackerrank.com/challenges/cycle-representation |

---

## Preview

Count the cycles!

## Problem Statement

Let $n$ be a fixed integer. <br>

A **permutation** is a bijection from the set $\{1,2,\ldots,n\}$ to itself. <Br><br>
A **cycle of length $k$** ($k\ge 2$) is a permutation $f$ where different integers exist $i_1,\ldots,i_k$ such that $f(i_1)=i_2, f(i_2)=i_3, \ldots, f(i_k)=i_1$ and, for all $x$ not in $\{i_1,\ldots,i_k\}$, $f(x)=x$.

The **composition of $m$ permutations** $f_1,\ldots,f_m$, written $f_1\circ f_2\circ\ldots\circ f_m$, is their composition as functions.

Steve has some cycles $f_1,f_2,\ldots,f_m$. He knows the length of cycle $f_i$ is $l_i$, but he does not know exactly what the cycles are.
He finds that the composition $f_1\circ f_2\circ\ldots\circ f_m$ of the cycles is a cycle of length $n$. <br>
He wants to know how many possibilities of $f_1,\ldots,f_m$ exist.

## Input Format

The first line contains $T$, the number of test cases. <br>
Each test case contains the following information:<br>
The first line of each test case contains two space separated integers, $n$ and $m$.<br>
The second line of each test case contains $m$ integers, $l_1,\ldots,l_m$.

**Constraints**

$n \geqslant 2$

Sum of $n\leqslant 1000$

$2\leqslant l_i \leqslant n$

Sum of $m\le 10^6$

## Output Format

Output $T$ lines. Each line contains a single integer, the answer to the corresponding test case.

Since the answers may be very large, output them modulo $(10^9+7)$.

## Sample Tests

### Test 1

```
1
3 2
2 2
```

### Test 2

```
6
```
