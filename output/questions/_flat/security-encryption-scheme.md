# Security Encryption Scheme

---

| Field | Value |
|---|---|
| **Slug** | `security-encryption-scheme` |
| **Domain** | security |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/security-encryption-scheme |

---

## Preview

Count the number of bijections and the number of keys that produce different encryption functions.

## Problem Statement

An *encryption scheme* consists of a set $\{E_e : e \in K\}$ and a corresponding set $\{D_d : d \in K\}$ of encrypting and decrypting functions, respectively. <br> 
For each $e \in K$, there is a unique key $d \in K$ where $D_d = E_e^{-1}$. <br>
An encryption scheme is also called a *cipher*.

It should be clear that every $e$ is actually a representative of some bijection from $M$ to $C$. In this task, you have to count the number of such bijections and, hence, the number of keys that produce different encryption functions.

Assume that $|M| = |C| = n$ which is given as the input.

**Constraints**

$1\le n\le10$

## Input Format

The input consists of a single positive integer $n$.

## Output Format

Output a single positive integer, the number of bijections.

## Sample Tests

### Test 1

```
3
```

### Test 2

```
6
```
