# Determine the Winner

---

| Field | Value |
|---|---|
| **Slug** | `playing-cards-1-1` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 20 |
| **Contest** | hack-the-interview-global |
| **URL** | https://www.hackerrank.com/challenges/playing-cards-1-1 |

---

## Preview

Determine the winner in a new version of the classic game of cards.

## Problem Statement

A deck of cards contains 52 cards, where each card has a suit and a number written on it. There are 4 suits, namely $A, B, C$ and $D$, and numbers on cards are from range $1$ to $13$.

Before the game starts, one of the suits is decided to be called the winning suit. Then, the play begins and two players play exactly $n$ rounds as follows: 

- first, each player draws a single card from the deck
- if one of the players drew a card of the winning suit and the other did not, then the player who drew a card of the winning suit wins the round
- otherwise, the numbers written on the cards decide: if one player drew a card with a greater number on it than the other player, the player with the greater number wins, otherwise, if both players drew cards with the same numbers, the round ends in a draw
- after the round is ended, the players return the cards they drew into the deck

Given the cards the players drew in each round, determine the result of each round of the game.

## Input Format

In the first line, there is a single character $\text{winning_suit}$ denoting the winning suit.

In the second line, there is a single integer $n$ denoting the number of rounds to be played.

Each of the next $n$ lines denotes the cards that were drawn in a single round of the game and contains four space-separated values: $\text{suit1, number1, suit2}$, and $\text{number2}$ denoting the suit of player's 1 card, the number on player's 1 card, the suit of player's 2 card, and the number of player's 2 card respectively.

## Output Format

The output must contain exactly $n$ lines. The $i^{th}$ of those lines must denote the result of the $i^{th}$ round of the game and contain either `Player 1 wins` if Player 1 wins or `Player 2 wins` if Player 2 wins, or `Draw` if the round ends in a draw.

## Constraints

- $\text{winning_suit} \in \{A, B, C, D\}$
- $1\le n\le 10^3$
- $\text{suit1, suit2} \in \{A, B, C, D\}$
- $1\le \text{number1, number2} \le 13$

## Sample Tests

### Test 1

```
B
5
A 2 B 1
A 7 D 2
B 5 D 13
B 3 B 1
A 12 C 12
```

### Test 2

```
Player 2 wins
Player 1 wins
Player 1 wins
Player 1 wins
Draw
```
