# Candles Counting

---

| Field | Value |
|---|---|
| **Slug** | `candles-2` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 85 |
| **URL** | https://www.hackerrank.com/challenges/candles-2 |

---

## Preview

Out of N elements how many strictly increasing subsequences are there so that these have at least K different color values at least once in the subsequence

## Problem Statement

Tim is visiting his grandma for two days and is bored due to the lack of the electricity over there. That's why he starts to play with grandma's colorful candle collection.

He aligned the $N$ candles from left to right. The $i$th candle from the left has the height $H_i$ and the color $C_i$, an integer ranged from 1 to a given $K$, the number of colors. 

Now he stares at the sequence of candles and wonders, how many strictly increasing ( in height ) colorful subsequences are there? A subsequence is considered as colorful if every of the $K$ colors appears at least one times in the subsequence. 

As the number of subsequences fulfilling the requirement can be large, print the result modulo $10^9 + 7$.

## Input Format

On the first line you will be given $N$ and $K$, then $N$ lines will follow. On the $i$th line you will be given two integers $H_i$ and $C_i$.

## Output Format

Print the number of strictly increasing colorful subsequences modulo $10^9 + 7$.

## Constraints

* $1 \leq N \leq 5 \cdot 10^4$
* $1 \leq C_i \leq K \leq 7$
* $1 \leq H_i \leq 5 \cdot 10^4$

## Sample Tests

### Test 1

```
4 3
1 1
3 2
2 2
4 3
```

### Test 2

```
2
```
