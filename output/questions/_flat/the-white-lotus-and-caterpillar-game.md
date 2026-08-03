# The White Lotus and Caterpillar game

---

| Field | Value |
|---|---|
| **Slug** | `the-white-lotus-and-caterpillar-game` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/the-white-lotus-and-caterpillar-game |

---

## Preview

Gary and Flo are playing a game in Jim's restaurant. Can you calculate something for them, while they are eating?

## Problem Statement

As usual Gary and Flo are sitting at their favourite burger restaurant called *Jim's Burgers*. They want to treat themselves with delicious burger after an interesting day with lots of competitive programming. So they have ordered their burgers and are waiting for them. But with nothing to do, they get bored and decide to play a game.

The game is played on a sheet of paper with $n$ rows and $m$ columns and goes as follows: 

Flo places his white lotus tile somewhere at the top row and Gary places a caterpillar tile somewhere on the bottom row. Flo begins the game and their turns alternate. Flo can move his tile to any of the 8 adjacent cells, while Gary's caterpillar tile can only move  __left__ or __right__, or __stay__ at the same cell. Of course, they cannot step outside of the grid. Flo's goal is to catch Gary as fast as possible, that is, with the minimum number of moves, while Gary (with the caterpillar tile) has to survive for as long as possible.


Now they are wondering: If they place their tiles in the corresponding rows and some random columns, what is the expected number of moves Flo has to make to win the game (assuming they will play optimally)? 

Can you help them answer this question?

**Constraints**

$ 2 \leq n,m \leq 5000 $

**Input Format**

You will be given two space separated integers $n$ and $m$, denoting the number of rows and the number of columns on the board respectively. 

**Output Format**

Output the answer in one line. 

**Note**: The answer will be considered valid if it differs from the correct answer by at most $10^{-6}$.

**Sample input**

	2 3
**Sample output**

	1.2222222

Consider the pair $(x, y)$ as the starting column of the lotus and the starting column of the caterpillar respectively. 

For $n = 2$ and $m = 3$ we get the following scenario. 

$(1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3)$ will lead to 1 move. 
The remaining pairs $(1, 3)$ and $(3, 1)$ will lead to 2 moves. So the expected value  is $\frac{1+1+1+1+1+1+1+2+2}{9}=1.222..$

## Sample Tests

### Test 1

```
2 3
```

### Test 2

```
1.2222222
```
