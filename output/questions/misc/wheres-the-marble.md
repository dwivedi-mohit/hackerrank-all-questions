# Where's the Marble?

---

| Field | Value |
|---|---|
| **Slug** | `wheres-the-marble` |
| **Contest** | hourrank-18 |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/wheres-the-marble |

---

## Problem Statement

Jill and Bob are playing the following game:

- There are $10$ cups on saucers arranged in a straight line. Each saucer is numbered sequentially from $1$ to $10$. 
- The game starts when Jill watches Bob place a marble inside the cup on saucer number $m$. 
- Bob then takes $n$ turns. In each turn, he swaps the cups on a pair of saucers numbered $a$ and $b$, where $a \ne b$. The diagram below shows an example:

![image](https://s3.amazonaws.com/hr-assets/0/1488269146-f990fe43cf-cups6.png)

- After Bob completes all his turns, Jill chooses an integer from $1$ to $10$ denoting the saucer where she think the cup with the marble is located.

Given $m$ and Bob's sequence of moves, print the saucer number denoting the marble's location at the end of the game.

## Input Format

The first line contains two space-separated integers describing the respective values of $m$ (the marble's initial location) and $n$ (Bob's number of turns).		
Each line $i$ of the $n$ subsequent lines contains two space-separated integers, $a_i$ and $b_i$, describing the saucer numbers for the cups Bob swaps in his $i^{th}$ move.

## Output Format

Print an integer denoting the saucer number of the cup containing the marble at the end of the game.

## Constraints

- $ 1 \le m, a_i, b_i \le 10$ 
- $ 1 \le n \le 50$
