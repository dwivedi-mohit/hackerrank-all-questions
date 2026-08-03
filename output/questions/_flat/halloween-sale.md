# Halloween Sale

---

| Field | Value |
|---|---|
| **Slug** | `halloween-sale` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/halloween-sale |

---

## Preview

How many games can you buy during the Halloween Sale?

## Problem Statement

You wish to buy video games from the famous online video game store Mist.

Usually, all games are sold at the same price, $p$ dollars. However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price. Specifically, the first game will cost $p$ dollars, and every subsequent game will cost $d$ dollars less than the previous one. This continues until the cost becomes less than or equal to $m$ dollars, after which every game will cost $m$ dollars. How many games can you buy during the Halloween Sale?

**Example**

$p = 20$

$d = 3$

$m = 6$

$s = 70$. 

The following are the costs of the first $11$, in order:

$$20, 17, 14, 11, 8, 6, 6, 6, 6, 6, 6$$

Start at $p = 20$ units cost, reduce that by $d = 3$ units each iteration until reaching a minimum possible price, $m = 6$.  Starting with $s = 70$ units of currency in your Mist wallet, you can buy 5 games: $20 + 17 + 14 + 11 + 8 = 70$.

**Function Description**


Complete the _howManyGames_ function in the editor below.


_howManyGames_ has the following parameters:


- *int p:* the price of the first game

- *int d:* the discount from the previous game price
- *int m:* the minimum cost of a game

- *int s:* the starting budget

## Input Format

The first and only line of input contains four space-separated integers $p$, $d$, $m$ and $s$.

## Constraints

- $1 \le m \le p \le 100$

- $1 \le d \le 100$

- $1 \le s \le 10^4$

## Sample Tests

### Test 1

```
20 3 6 80
```

### Test 2

```
6
```

### Test 3

```
20 3 6 85
```

### Test 4

```
7
```
