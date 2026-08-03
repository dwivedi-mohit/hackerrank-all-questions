# How Many Solvable Puzzles?

---

| Field | Value |
|---|---|
| **Slug** | `solving-the-puzzle-1` |
| **Domain** | misc |
| **Difficulty** | Advanced |
| **Score** | 100 |
| **Contest** | 101hack30 |
| **URL** | https://www.hackerrank.com/challenges/solving-the-puzzle-1 |

---

## Preview

Count the number of ways to create a solvable puzzle.

## Problem Statement

Consider the following game: $The$ $game$ $of$ $15$. 

In this game, you have $16$ tiles with all the integer numbers from $0$ to $15$ arranged in a game field of $4$ rows and $4$ columns. During a move, you can exchange two side-by-side adjacent tiles (i.e. horizontally or vertically adjacent) only if one of them has the value $0$. Using a sequence of moves, the goal of the game is to reach the following final state:

	1   2   3    4
	5   6   7    8
	9   10  11  12
	13  14  15   0 
  

We have a game field consisting of $4$ rows and $4$ columns. For each particular cell of this field, we know what pieces are allowed to be placed in it. 

Challenge: Count the number of ways to place the pieces under this constraint to reach the final state pictured above.

## Input Format

Let's enumerate the cells of the field in the following way:

    1   2   3   4
    5   6   7   8
    9   10  11  12
    13  14  15  16
  

There are $16$ lines given in the input. 

The $i$<sup>th</sup> line of the input starts with a single integer $C_i$, denoting the number of tiles that can be placed on the corresponding cell. Then, $C_i$ integers describing the tiles that can be placed in the corresponding cell, follow.

## Output Format

Output a single line: The number of ways to place the tiles under the given conditions.

## Sample Tests

### Test 1

```
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 0
```

### Test 2

```
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
```

### Test 3

```
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
1 11
1 12
1 13
1 14
1 15
1 0
```

### Test 4

```
1
```

### Test 5

```
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 0
```
