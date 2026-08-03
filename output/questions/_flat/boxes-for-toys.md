# Boxes for Toys

---

| Field | Value |
|---|---|
| **Slug** | `boxes-for-toys` |
| **Domain** | misc |
| **Difficulty** | Expert |
| **Score** | 85 |
| **Contest** | 101hack50 |
| **URL** | https://www.hackerrank.com/challenges/boxes-for-toys |

---

## Preview

Compute the expected value of the smallest box's volume among all subsegments.

## Problem Statement

Peter is an employee of a local toy factory in Quahog, where he's in charge of boxing toys that are *ordered* by *shops*.


There are $n$ toy types at the factory. The $i$'th toy type has a 3-dimensional [cuboid](https://en.wikipedia.org/wiki/Cuboid) shape with dimensions $a_i \times b_i \times c_i$. We denote this as $(a_i,b_i,c_i)$. A toy of dimensions $(a_i,b_i,c_i)$ can be rotated to get *any permutation* of the dimensions, for example, $(b_i,a_i,c_i)$, $(c_i,a_i,b_i)$, $(c_i,b_i,a_i)$, etc.

The toys are arranged in a row such that similar toys are next to each other, so when a shop *orders* some toys, they always form a *contiguous* subsequence of the sequence of all toy types. When a shop orders some interval of toys, let's say from the $l$'th to $r$'th, Peter has to pack them. He chooses a single box shape: a cuboid with dimensions $(a, b, c)$. He then produces $r-l+1$ boxes of this shape and packs each toy in a separate box. If Peter chooses some box shape, then each ordered toy must fit in this box. It means that, *possibly after some rotation*, each of its dimensions must be no greater than the corresponding dimension of the box.


![image](https://s3.amazonaws.com/hr-assets/0/1497796087-5a91fe3b2f-4.png)

Peter always succeeds in choosing the best box, that is, he always chooses the box shape whose volume $a \cdot b \cdot c$ is the minimum possible.

You are the factory's boss, and you're wondering whether Peter's strategy gives good results on average. Assuming that all intervals $[l,r]$ will be ordered with equal probability, print the [expected volume](https://en.wikipedia.org/wiki/Expected_value) of the box Peter will use. The factory has an unlimited amount of toys of each type, so when a shop orders some toys, those types won't disappear from the shop.

The answer can always be expressed as ${p \over q}$ where $p$ and $q$ are relatively prime integers; you should output $pq^{-1} \bmod (10^9 + 7)$. $q^{-1}$ denotes the [modular multiplicative inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse) of $q$ modulo $10^9 + 7$.

## Input Format

The first line contains one integer $n$ denoting the number of toy types.

Each of the next $n$ lines describes one toy. The $i$'th of them contains three space-separated integers 

$a_i$, $b_i$, $c_i$, the dimensions of the $i$'th toy.

## Output Format

Print a single integer, the sought value of $pq^{-1} \bmod (10^9 + 7)$.

## Constraints

- $2 \leq n \leq 3 \cdot 10^5$
- $1 \leq a_i, b_i, c_i \leq 10^9$

**Subtasks**


- $n \leq 5000$ for $20\%$ of the total score

## Sample Tests

### Test 1

```
2
5 2 3
1 10 1
```

### Test 2

```
333333369
```

### Test 3

```
3
1 2 3
2 1 3
3 2 1
```

### Test 4

```
6
```
