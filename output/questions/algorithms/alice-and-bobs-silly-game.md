# Alice and Bob's Silly Game

---

| Field | Value |
|---|---|
| **Slug** | `alice-and-bobs-silly-game` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/alice-and-bobs-silly-game |

---

## Preview

Alice and Bob are playing a game with prime numbers. Can you determine the winner?

## Problem Statement

Alice and Bob invented the following silly game:

- The game starts with an integer, $n$, that's used to build a $set$ of $n$ distinct integers in the inclusive range from $1$ to $n$ (i.e., $set = \{1, 2, 3, \ldots, n-1, n\}$).
- Alice always plays first, and the two players move in alternating turns.
- During each move, the current player chooses a [prime number](https://en.wikipedia.org/wiki/Prime_number), $p$, from $set$. The player then removes $p$ and all of its multiples from $set$.
* The first player to be unable to make a move loses the game.

Alice and Bob play $g$ games. Given the value of $n$ for each game, print the name of the game's winner on a new line. If Alice wins, print `Alice`; otherwise, print `Bob`.

**Note:** Each player always plays optimally, meaning they will not make a move that causes them to lose the game if some better, winning move exists.

## Input Format

The first line contains an integer, $g$, denoting the number of games Alice and Bob play. 	
Each line $i$ of the $g$ subsequent lines contains a single integer, $n$, describing a game.

## Output Format

For each game, print the name of the winner on a new line. If Alice wins, print `Alice`; otherwise, print `Bob`.

## Constraints

* $1 \le g \le 1000$

* $1 \le n \le 10^{5}$

**Subtasks**

* $1 \le n \le 1000$ for $50\%$ of the maximum score

## Sample Tests

### Test 1

```
3
1
2
5
```

### Test 2

```
Bob
Alice
Alice
```
