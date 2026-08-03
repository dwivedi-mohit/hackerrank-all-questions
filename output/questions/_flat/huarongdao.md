# Huarongdao

---

| Field | Value |
|---|---|
| **Slug** | `huarongdao` |
| **Domain** | algorithms |
| **Difficulty** | Expert |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/huarongdao |

---

## Preview

Can you move the block to its exit in the minimum possible time?

## Problem Statement

Huarongdao is a well-known game in China. The purpose of this game is to move the Cao Cao block out of the board. 

Acme is interested in this game, and he invents a similar game. There is a N\*M board. Some blocks in this board are movable, while some are fixed. There is only one empty position. In one step, you can move a block to the empty position, and it will take you one second. The purpose of this game is to move the Cao Cao block to a given position. Acme wants to finish the game as fast as possible. 

But he finds it hard, so he cheats sometimes. When he cheats, he spends K seconds to pick a block and put it in an empty position. However, he is not allowed to pick the Cao Cao block out of the board .

**Note** 

1. Immovable blocks cannot be moved while cheating. 
2. A block can be moved only in the directions UP, DOWN, LEFT or RIGHT.

## Input Format

The first line contains four integers N, M, K, Q separated by a single space.  N lines follow.

Each line contains M integers 0 or 1 separated by a single space. If the j<sub>th</sub> integer is 1, then the block in i<sub>th</sub> row and j<sub>th</sub> column is movable. If the j<sub>th</sub> integer is 0 then the block in i<sub>th</sub> row and j<sub>th</sub> column is fixed.
Then Q lines follows, each line contains six integers EX<sub>i</sub>, EY<sub>i</sub>, SX<sub>i</sub>, SY<sub>i</sub>, TX<sub>i</sub>, TY<sub>i</sub> separated by a single space. The i<sub>th</sub> query is the Cao Cao block is in row SX<sub>i</sub> column SY<sub>i</sub>, the exit is in TX<sub>i</sub>, TY<sub>i</sub>, and the empty position is in row EX<sub>i</sub> column EY<sub>i</sub>. It is guaranteed that the blocks in these positions are movable. Find the minimum seconds Acme needs to finish the game. If it is impossible to finish the game, you should answer -1.

## Output Format

You should output Q lines, i-th line contains an integer which is the answer to i-th query.

## Constraints

N,M &le; 200

1 &le; Q &le; 250

10 &le; K&le; 15

1 &le; EX<sub>i</sub>,  SX<sub>i</sub>,  TX<sub>i</sub>&le; N

1 &le; EY<sub>i</sub>, SY<sub>i</sub>,TY<sub>i</sub> &le; M

## Sample Tests

### Test 1

```
5 5 12 1
1 1 1 1 1
1 1 1 1 1
0 1 1 1 1
1 1 1 1 1
0 1 0 1 1
1 5 4 3 4 1
```

### Test 2

```
20
```
