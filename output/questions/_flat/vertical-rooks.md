# Vertical Rooks

---

| Field | Value |
|---|---|
| **Slug** | `vertical-rooks` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 90 |
| **URL** | https://www.hackerrank.com/challenges/vertical-rooks |

---

## Preview

Decide who will win the game in HackerChess

## Problem Statement

HackerChess is a variant of chess played at HackerRank. It is a game played between two players who make moves in turns until one of them cannot make any move. The player who cannot make a move loses the game and the other player is declared the winner. The game is played on a board with $n$ rows and $n$ columns. The only pieces used in the game are rooks. A rook in HackerChess moves only vertically, which means that in never leaves a column to which it belongs. Moreover, in a single move, a rook moves through any number of unoccupied cells. Notice that there are no captures in HackerChess, two rooks cannot occupy the same cell, and a rook cannot jump over another rook. Each player has exactly one rook in each of the $n$ columns of the board.

Given the initial position of the rooks and knowing that the second player makes the first move, decide who will win the game if both players play optimally.

## Input Format

In the first line, there is a single integer $t$ denoting the number of games to be played. After that, descriptions of $t$ games follow:

In the first line, there is a single integer $n$ denoting the size of the board. Next, $n$ lines follow. In the $i$-th of them there is a single integer $r_{1,i}$ denoting the row of the rook belonging to the first player placed in the $i$-th column. After that, another $n$ lines follow. In the $i$-th of them there is a single integer $r_{2,i}$ denoting the row of the rook belonging to the second player placed in the $i$-th column.

## Output Format

Print exactly $t$ lines. In the $i$-th of them, print `player-1` if the first player will win the $i$-th game. Otherwise, print `player-2` in this line.

## Constraints

- $ 1 \leq t \leq 10$

- $ 2 \leq n \leq 2000$
- $ 1 \leq r_{1,i}, r_{2,i} \leq n$
- $ r_{1,i} \neq r_{2,i}$

## Sample Tests

### Test 1

```
1
3
1
2
2
3
1
1
```

### Test 2

```
player-2
```

### Test 3

```
1
4
3
3
3
3
4
4
4
4
```

### Test 4

```
player-1
```
