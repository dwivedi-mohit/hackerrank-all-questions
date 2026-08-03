# Maximum Streaks

---

| Field | Value |
|---|---|
| **Slug** | `heads-or-tails` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 10 |
| **Contest** | hack-the-interview-global |
| **URL** | https://www.hackerrank.com/challenges/heads-or-tails |

---

## Preview

Calculate the longest streaks of Heads and Tails in a series of coin tosses.

## Problem Statement

A coin was tossed numerous times. You need to find the longest streak of tosses resulting $\text{Heads}$ and the longest streak of tosses resulting in $\text{Tails}$.

Formally, given the results of $n$ tosses of a coin, find the maximum number of consecutive $\text{Heads}$ and the maximum number of consecutive $\text{Tails}$.

Consider the following example: a coin was tossed $n = 7$ times and the results were $\text{Heads, Heads, Tails, Tails, Heads, Heads, Heads}$. Therefore, the longest $\text{Heads}$ streak was $3$ and the longest $\text{Tails}$ streak was $2$.

Complete the function *getMaxStreaks* which takes an array of strings *toss* and returns an array of two integers denoting the maximum streaks of $\text{Heads}$ and $\text{Tails}$ respectively.

## Input Format

In the first line, there is a single integer $n$ denoting the number of tosses.

Then, $n$ lines follow. The $i^{th}$ of them contains a string $toss_i$ denoting the result of the $i^{th}$ toss of the coin.

## Output Format

In a single line, print two space-separated integers denoting the maximum streak of $\text{Heads}$ and the maximum streak of $\text{Tails}$ respectively.

## Constraints

- $1 \le n \le 50$
- $toss_{i} \in \{\text{Heads, Tails}\}$

## Sample Tests

### Test 1

```
7
Heads
Tails
Tails
Tails
Heads
Heads
Tails
```

### Test 2

```
2 3
```

### Test 3

```
3
Tails
Tails
Tails
```

### Test 4

```
0 3
```

### Test 5

```
4
Heads
Heads
Heads
Heads
```

### Test 6

```
4 0
```
