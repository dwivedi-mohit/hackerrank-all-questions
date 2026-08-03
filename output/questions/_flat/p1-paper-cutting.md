# Cutting Paper Squares

---

| Field | Value |
|---|---|
| **Slug** | `p1-paper-cutting` |
| **Domain** | mathematics |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/p1-paper-cutting |

---

## Preview

Determine the number of cuts needed to cut a paper into $1 \times 1$ squares.

## Problem Statement

Mary has an $n \times m$ piece of paper that she wants to cut into $1 \times 1$ pieces according to the following rules:

- She can only cut *one piece of paper at a time*, meaning she *cannot* fold the paper or layer already-cut pieces on top of one another. 
- Each cut is a straight line from one side of the paper to the other side of the paper. For example, the diagram below depicts the three possible ways to cut a $3 \times 2$ piece of paper:		
	![example-cutting-squares.png](https://s3.amazonaws.com/hr-challenge-images/26273/1476740077-bd1ab26d74-example-cutting-squares.png)

Given $n$ and $m$, find and print the minimum number of cuts Mary must make to cut the paper into $n \cdot m$ squares that are $1 \times 1$ unit in size.

## Input Format

A single line of two space-separated integers denoting the respective values of $n$ and $m$.

## Output Format

Print a long integer denoting the minimum number of cuts needed to cut the entire paper into $1 \times 1$ squares.

## Constraints

- $1 \le n, m \le 10^{9}$

## Sample Tests

### Test 1

```
3 1
```

### Test 2

```
2
```
