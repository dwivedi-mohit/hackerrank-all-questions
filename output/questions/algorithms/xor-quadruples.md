# Beautiful Quadruples

---

| Field | Value |
|---|---|
| **Slug** | `xor-quadruples` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/xor-quadruples |

---

## Preview

Count the number of beautiful quadruples.

## Problem Statement

We call an quadruple of positive integers, $(W, X, Y, Z)$, *beautiful* if the following condition is true:

$$W \oplus X \oplus Y \oplus Z \neq 0$$

**Note:** $\oplus$ is the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operator.

Given $A$, $B$, $C$, and $D$, count the number of *beautiful* quadruples of the form $(W, X, Y, Z)$ where the following constraints hold:

- $1 \leq W \leq A$
- $1 \leq X \leq B$
- $1 \leq Y \leq C$
- $1 \leq Z \leq D$


When you count the number of *beautiful* quadruples, you should consider two quadruples as same if the following are true:

* They contain same integers.
* Number of times each integers occur in the quadruple is same.

For example $(1,1,1,2)$ and $(1,1,2,1)$ should be considered as same.

## Input Format

A single line with four space-separated integers describing the respective values of $A$, $B$, $C$, and $D$.

## Output Format

Print the number of *beautiful* quadruples.

## Constraints

* $1 \leq A, B, C, D \leq 3000$
* For $50\%$ of the maximum score, $1 \leq A, B, C, D \leq 50$

## Sample Tests

### Test 1

```
1 2 3 4
```

### Test 2

```
11
```
