# What Are the Odds?

---

| Field | Value |
|---|---|
| **Slug** | `what-are-the-odds` |
| **Contest** | hourrank-19 |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/what-are-the-odds |

---

## Problem Statement

[Nim](https://en.wikipedia.org/wiki/Nim) is a famous two-player algorithm game with the following basic rules:

* The game starts with $n$ piles of stones indexed from $0$ to $n-1$. Each pile $i$ (where $0 \le i \lt n$) has $s_i$ stones. The diagram below shows an example:


![image](https://s3.amazonaws.com/hr-assets/0/1490949233-32163ca443-odds4.png)


* The players move in alternating turns. During each move, the current player must remove one or more stones from a single pile. 
* The first player who is unable to remove a stone (e.g., a stone can't be removed if all piles are already empty) loses the game.

Alice and Bob decided to add the following *special move* before starting a game of Nim:

* Alice selects two indices, $b$ and $e$, such that $0 \le b \le e \le n-1$.
* Remove all the piles in the between index $b$ and index $e$. Note that the number of removed piles can be anywhere from $1$ to $n$.

For example, If Alice selects $b=1$ and $e=3$, the set of piles of the diagram above would look like this:


![image](https://s3.amazonaws.com/hr-assets/0/1490949456-2d52a6a65b-odds6.png)

After Alice makes the special move, Bob starts a game of Nim as its first player. They both play optimally, meaning they will not make a move that causes them to lose the game if some better, winning move exists. 

Given the number of stones in each pile, find the number of ways Alice can select $b$ and $e$ to ensure she wins the game.

## Input Format

There are two lines of input:

1. An integer, $n$, denoting the number of piles.
2. $n$ space-separated integers describing the respective values of $s_{0}, s_{1}, \ldots, s_{n-1}$.

## Output Format

Print the number of ways Alice can select $b$ and $e$ to ensure she wins the game.

## Constraints

- $1 \le n \le 5 \cdot 10^5$
- $1 \le s_i \le 10^5$

**Subtasks**

- $1 \le n \le 5000$  for $20\%$ of the maximum score.
