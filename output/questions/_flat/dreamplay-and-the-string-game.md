# Dreamplay and the String Game: Used

---

| Field | Value |
|---|---|
| **Slug** | `dreamplay-and-the-string-game` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 55 |
| **Contest** | 101hack48 |
| **URL** | https://www.hackerrank.com/challenges/dreamplay-and-the-string-game |

---

## Preview

Determine the winner of a game where each player removes a character from either end of a string.

## Problem Statement

Dreamplay made a game for his friends Steven and Amanda to play on two strings, $s$ and $p$. They move in alternating turns, with Steven moving first. During each move, the player can perform exactly one of the following operations:

-  Remove the first character in $s$.
-  Remove the last character in $s$.

The game ends once string $s$ is *not longer than* string $p$, that is, $\text{length}(s) \le \text{length}(p)$. If $s$ is exactly the same as string $p$ at the end of the game, then Amanda wins; otherwise, Steven wins. 

For example, if $s = \text{bababbabab}$ and $p = \text{bab}$, the diagram below depicts two possible gameplay scenarios:

![Two string games.](https://s3.amazonaws.com/hr-assets/0/1491899589-c6408ba4f3-32.png "Two string games.")

Complete the function so that it returns a string denoting the name of the winner (i.e., either `Amanda` or `Steven`) for a given $s$ and $p$, assuming both players play optimally.

## Input Format

The first line contains an integer, $q$, denoting the number of queries (i.e., calls to the function). The $2 \cdot q$ subsequent lines describe each query over two lines:

1. The first line contains a string denoting $s$.

2. The second line contains a string denoting $p$.

## Output Format

Return a string denoting the name of the winner (i.e., either `Amanda` or `Steven`).

## Constraints

<!-- Please be careful about changing constraints next time! -->

- $1 \leq q \leq {10}^{4}$ 
- $1 \le \text{ length of } p < {10}^{6}$
- $1 \le \text{ length of } s < {10}^{6}$
- The sum of the lengths of $p$ and $s$ in a single file is $< 10^6$

- $s$ and $p$ consist only of lowercase English letters.

## Sample Tests

### Test 1

```
1
aaaa
aa
```

### Test 2

```
Amanda
```

### Test 3

```
1
abb
b
```

### Test 4

```
Amanda
```
