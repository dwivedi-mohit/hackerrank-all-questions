# Stone Game

---

| Field | Value |
|---|---|
| **Slug** | `stonegame` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/stonegame |

---

## Preview

Find the number of ways Bob can remove the stones to force Alice into losing a game of Nim.

## Problem Statement

Alice and Bob are playing the game of [Nim](http://en.wikipedia.org/wiki/Nim) with $n$ piles of stones with sizes $p_0, p_1, \ldots, p_{n-1}$. If Alice plays first, she loses if and only if the '[xor](http://en.wikipedia.org/wiki/Exclusive_or) sum' (or 'Nim sum') of the piles is zero, i.e., $p_{0} \oplus p_{1} \oplus \ldots \oplus p_{n-1} = 0$.

Since Bob already knows who will win (assuming optimal play), he decides to cheat by removing some stones in some piles before the game starts. However, to reduce the risk of suspicion, he must keep at least one pile unchanged. Your task is to count the number of ways Bob can remove the stones to force Alice into losing the game. Since the number can be very large, output the number of ways [modulo](https://en.wikipedia.org/wiki/Modulo_operation) $10^9 + 7$. Assume that both players will try to optimize their strategy and try to win the game.

## Input Format

The first line of the input contains an integer $n$ denoting the number of piles. The next line contains $n$ space-separated integers $p_0, p_1, \ldots, p_{n-1}$ indicating the sizes of the stone piles.

## Output Format

Print a single integer denoting the number of ways Bob can force Alice to lose the game, modulo $10^9 + 7$.

## Constraints

- $3 \le n \le 100$

- $0 < p[i] < 10^9$

## Sample Tests

### Test 1

```
3
1 2 3
```

### Test 2

```
4
```

### Test 3

```
10
10 10 1 1 1 1 1 10 10 10
```

### Test 4

```
321616
```
