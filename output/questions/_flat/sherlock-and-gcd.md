# Sherlock and GCD

---

| Field | Value |
|---|---|
| **Slug** | `sherlock-and-gcd` |
| **Domain** | mathematics |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/sherlock-and-gcd |

---

## Preview

Help Sherlock in finding the subset.

## Problem Statement

Sherlock is stuck while solving a problem: Given an array $A = \{a_1, a_2, \cdots, a_N \}$, he wants to know if there exists a subset $B$ of this array which follows these statements:

* $B$ is a non-empty subset.
* There exists no integer $x (x > 1)$ which divides all elements of $B$.
* There are no elements of $B$ which are equal to another.

## Input Format

The first line of input contains an integer, $T$, representing the number of test cases. Then $T$ test cases follow.

Each test case consists of two lines. The first line contains an integer, $N$, representing the size of array $A$. In the second line there are $N$ space-separated integers, $a_1, a_2, \ldots, a_n$, representing the elements of array $A$.

**Constraints**

$1 \le T \le 10$  

$1 \le N \le 100$  

$1 \le a_i \le 10^5 \text{  } \forall 1\le i \le N$

## Output Format

Print `YES` if such a subset exists; otherwise, print `NO`.

## Sample Tests

### Test 1

```
3
3
1 2 3
2
2 4
3
5 5 5
```

### Test 2

```
YES
NO
NO
```
