# Single-Player UNO

---

| Field | Value |
|---|---|
| **Slug** | `single-player-uno` |
| **Domain** | misc |
| **Difficulty** | Advanced |
| **Score** | 120 |
| **Contest** | 101hack31 |
| **URL** | https://www.hackerrank.com/challenges/single-player-uno |

---

## Problem Statement

UNO is a famous card game where the cards have numbers and colors. The fundamental rule is that each card played should be either the same color or the same number as the previously played card.

Single player UNO is similar. Our player, Alice, starts the game with a hand of $N$ cards. Alice must order her $N$ cards according to the following rules:

1. Any card can be the first card.
2. Each subsequent card must be either the same color or the same number as the previous card. 
3. When you play a card (except for the first card), according to the previous card, you will say "color" or "number" depending on what is the same. If this card is the exact same as the previous card, you can choose to say either "color" or "number". No two consecutive sayings may be the same.

Single player UNO has $76$ $(= 4 * 9 * 2 + 4)$ **different** cards. There are four colors: red, green, blue, and yellow. For each color, there is only **one** card numbered $0$ and **two** cards for each number from $1$ through $9$.

Alice wants to know how many different initial hands of cards will have a great order? 

**Note:** Two sets of initial hands are different only if there is at least one card that only belongs to one of them. All cards are considered to be unique elements of the deck, meaning any two cards with matching number and color values are still considered to be different.

The answer might be very large. You just need to output the remainder by dividing with $M$.

## Input Format

One line of input containing two space-separated integers, $N$ (the number of cards in Alice's hand) and $M$.

**Constraints**

In $100\%$ test cases, $1$ &le; $N$ &le; $76$, $1$ &le; $M$ &le; $10^9+7$

## Output Format

A single integer.

## Sample Tests

### Test 1

```
1 1000
```

### Test 2

```
76
```
