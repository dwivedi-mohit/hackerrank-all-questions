# Stone Division

---

| Field | Value |
|---|---|
| **Slug** | `stone-division` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/stone-division |

---

## Preview

Determine which player wins in a Game of Stones.

## Problem Statement

Consider the following game:

- There are two players, *First* and *Second*, sitting in front of a pile of $n$ stones. *First* always plays first.
- There is a set, $S$, of $m$ distinct integers defined as $S = \{s_0, s_1, \ldots, s_{m-1}\}$.
- The players move in alternating turns. During each turn, a player chooses some $s_i \in S$ and splits one of the piles into exactly $s_i$ smaller piles of equal size. If no $s_i$ exists that will split one of the available piles into exactly $s_i$ equal smaller piles, the player loses.
- Both players always play optimally.

Given $n$, $m$, and the contents of $S$, find and print the winner of the game. If *First* wins, print `First`; otherwise, print `Second`.

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the size of the initial pile) and $m$ (the size of the set).		
The second line contains $m$ distinct space-separated integers describing the respective values of $s_0, s_1, \ldots, s_{m - 1}$.

## Output Format

Print `First` if the *First* player wins the game; otherwise, print `Second`.

## Constraints

- $1 \le n \le 10^{18}$
- $1 \le m \le 10$
- $2 \le s_i \le 10^{18}$

## Sample Tests

### Test 1

```
15 3
5 2 3
```

### Test 2

```
Second
```
