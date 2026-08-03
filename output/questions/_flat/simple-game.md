# Simple Game

---

| Field | Value |
|---|---|
| **Slug** | `simple-game` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/simple-game |

---

## Preview

Find the number of winning configurations for Little Cat.

## Problem Statement

Big Cat and Little Cat love playing games. Today, they decide to play a Game of Stones, the *Kitties are Coming* edition. The game's rules are as follows: 

- The game starts with $N$ stones that are randomly divided into $M$ piles. 
- The cats move in alternating turns, and Little Cat always moves first.
- During a move, a cat picks a pile having a number of stones $\ge 2$ and splits it into any number of non-empty piles in the inclusive range from $2$ to $K$. 
- The first cat to be unable to make a move (e.g., because all piles contain exactly $1$ stone) loses the game. 

Little Cat is curious about the number of ways in which the stones can be initially arranged so that she is guaranteed to win. Two arrangements of stone piles are considered to be different if they contain different sequences of values. For example, arrangements $(2, 1, 2)$ and $(2, 2, 1)$ are different.

Given the values for $N$, $M$, and $K$, find the number of winning configurations for Little Cat and print it modulo $10^9+7$. 

**Note:** Each cat always moves *optimally*, meaning that they're both playing to win and neither cat will make a move that causes them to lose the game if some other (winning) sequence of moves can be made.

## Input Format

The first line of input contains three space-separated integers, $N$ (the number of stones), $M$ (the number of piles), and $K$ (the maximum number of piles into which a pile can be split during a single move), respectively.

## Output Format

Print the number of initial arrangements of piles that will result in Little Cat winning, modulo $10^9+7$.

## Constraints

* $1 \leq M \leq 10$
* $M \leq N \leq 600$
* $2 \leq K \leq 600$

## Sample Tests

### Test 1

```
4 3 3
```

### Test 2

```
3
```
