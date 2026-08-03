# Modular Game of Numbers

---

| Field | Value |
|---|---|
| **Slug** | `modular-game-of-numbers` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 30 |
| **Contest** | 101hack47 |
| **URL** | https://www.hackerrank.com/challenges/modular-game-of-numbers |

---

## Preview

Help Sophie win the Game of Numbers.

## Problem Statement

Sophie is playing "The Game of Numbers" with her friends and needs help winning! Each person in the game is assigned a number from $0$ to $n - 1$ where $n$ is the number of people playing. Sophie and her two closest friends, Bob and Alice, will always be playing the game so you can assume $n \ge 3$. In each game, Sophie, Bob, and Alice will shout an integer aloud at the same time. The player that is assigned to the number that is equal to the sum of those integers $\bmod n$ loses the game!

Sophie has been assigned the number $0$. Sophie knows Bob and Alice well so she can predict the list of $p$ integers that Alice will choose from and the list of $q$ integers that Bob will choose from. Help Sophie by telling her the smallest *positive* integer to shout that is the least likely to lose her the game!

## Input Format

The first line contains three space-separated integers $n$ (the total number of players in the game), $p$ (the number of integers Alice will choose from), and $q$ (the number of integers Bob will choose from).


The second line contains $p$ space-separated integers $a_0, a_1, \ldots, a_{p-1}$ (Alice's numbers, all equally likely to be chosen).

The third line contains $q$ space-separated integers $b_0, b_1, \ldots, b_{q-1}$ (Bob's numbers, all equally likely to be chosen as well).

## Output Format

Print an integer that Sophie should shout such that her probablity of losing is minimised. If there are multiple such integers, print the minimum one.

Remember that Sophie can choose *any positive integer*!

## Constraints

- $3 \le n \le 4000$ 

- $1 \le p, q \le n$ 

- $1 \le a_i, b_i \le n$ 

- All elements in list $a$ are distinct.

- All elements in list $b$ are distinct.


**Subtasks** 


- For $\text{60%}$ of the maximum score, $n \le 200$.

## Sample Tests

### Test 1

```
3 1 1
1
2
```

### Test 2

```
1
```

### Test 3

```
3 2 1
1 2
3
```

### Test 4

```
3
```
