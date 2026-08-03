# Carpet Game

---

| Field | Value |
|---|---|
| **Slug** | `carpet-game` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 40 |
| **Contest** | 101hack53 |
| **URL** | https://www.hackerrank.com/challenges/carpet-game |

---

## Preview

Find the number of ways of placing some players in a 2D grid.

## Problem Statement

After having played a fun game for a few consecutive days, Jen decides to invite some of her friends to play too. The game is played on a carpet, with  $1 \times 1$ cells. To play the game, players sit on cells such that every two players can see each other. 

**Note:** During the game players are allowed to see only in $8$ directions: $\{E, N, W, S, NE, NW, SW, SE\}$. The blue region in the image below denotes the line of sight of a person sitting in the yellow cell. Two players can see each other if they are placed either horizontally, vertically or diagonally concerning each other and no other player is between them.

![image](https://s3.amazonaws.com/hr-assets/0/1518550738-9d0fe57583-direc.png)

On the $i^\text{th}$ day, Jen invites $k_i$ friends to play the game.
For each day, find the number of ways Jen along with her friends can sit on the carpet such that every player can see every other player. (No two players are allowed to sit in the same cell.)

Two ways of players' seating, is different if at least one player is at different cells in the two ways. Since the answer can be very large, print the answer modulo $10^9 + 7$.

Complete the function `howManyWays` which takes three integers $n_i$, $m_i$ and $k_i$ and returns an integer denoting the answer for the $i^\text{th}$ day, modulo $10^9 + 7$.

## Input Format

The first line contains a single integer $d$, the number of days for which the game is played. 

Each of the next $d$ lines contains three space-separated integers $n_i$, $m_i$ and $k_i$, the length of carpet, the width of carpet and the number of friends on the $i^\text{th}$ day, respectively.

## Output Format

Print $d$ lines. The $i^\text{th}$ line must contain an integer corresponding to the answer for the $i^\text{th}$ day, modulo $10^9 + 7$.

## Constraints

- $1 \le d \le 80$
- $n_i \times m_i \ge 2$
- $1 \le n_i, m_i \le 10^5$
- $1 \le k_i < n_i \times m_i$


**Subtasks**

- $1 \le n_i, m_i \le 50$ for $40\%$ of the maximum score.
- $1 \le n_i, m_i \le 10^3$ for $70\%$ of the maximum score.

## Sample Tests

### Test 1

```
3
2 2 1
2 2 2
2 2 3
```

### Test 2

```
12
24
24
```
