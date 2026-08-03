# Straight Flush

---

| Field | Value |
|---|---|
| **Slug** | `straight-flush` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 30 |
| **Contest** | 101hack32 |
| **URL** | https://www.hackerrank.com/challenges/straight-flush |

---

## Preview

Given a poker hand, determine if it's a straight flush.

## Problem Statement

We define the poker terms below as follows:

- The [**face cards**](https://en.wikipedia.org/wiki/Face_card) are J, Q, and K. They rank higher than cards $2 - 10$, and J $\lt$ Q $\lt$ K.
- A [**straight**](https://en.wikipedia.org/wiki/List_of_poker_hands#Straight) is a sequence of five consecutively numbered cards. <br>For example: 8♥ 9♥ 10♠ J♠ Q♣ 
- A [**flush**](https://en.wikipedia.org/wiki/Flush_(cards)) has five cards of the same suit. <br>For example: 4♣ 6♣ 7♣ 10♣ Q♣
- A [**straight flush**](https://en.wikipedia.org/wiki/List_of_poker_hands#Straight_flush) has five consecutively numbered cards of the same suit. <br>For example: 8♣ 9♣ 10♣ J♣ Q♣
- The [**Ace** (A)](https://en.wikipedia.org/wiki/Ace) is a special card with two possible behaviors in a [**straight**](https://en.wikipedia.org/wiki/List_of_poker_hands#Straight). It can be played as either a low card with a value of $1$, or as the highest card with a value $\gt$ K.

Given a poker hand of $5$ cards, print **YES** if you have a **straight flush** or **NO** otherwise.

## Input Format

There are five lines of input, and each line contains a two-character string.

The first character indicates the rank, and will be one of the following characters (ordered from lowest to highest rank): $2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A$. Note that $T$ stands for $10$, and recall that $A$ also can double as the lowest-ranking card with a value of $1$.

The second character denotes the suit and will be one of the following: $S$ (spades), $H$ (hearts), $D$ (diamonds), or $C$ (clubs).

## Output Format

Print **YES** if your hand is a **straight flush** or **NO** otherwise.

## Sample Tests

### Test 1

```
3C
4C
6C
7C
5C
```

### Test 2

```
3C
4H
6C
7C
5C
```

### Test 3

```
AC
2C
3C
4C
5C
```

### Test 4

```
YES
```

### Test 5

```
NO
```

### Test 6

```
YES
```
