# Bitter Chocolate

---

| Field | Value |
|---|---|
| **Slug** | `bitter-chocolate` |
| **Domain** | fp |
| **Difficulty** | Advanced |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/bitter-chocolate |

---

## Preview

Who eats the best chocolate.

## Problem Statement

Shashank and Arpith are both fond of chocolate, where a chocolate bar can be represented as a _3xN_ block of bars. On a particular day the leftmost-lowest block has been mixed with a very bitter ingredient by a not-so-good Prashant. He then gave that chocolate to them and told about this.

Prashant asked them to play a game with it, where a move of game consists of eating a block of bar along with all the blocks of bar which lies on the right and above it. Player alternate moves, and the person who eats the leftmost-lowest (bitter) block of bar is declared loser.

*Example:*

    Let the size of chocolate be 3x8. Block (1, 1) had been bittered. Player 1 starts the game, then they alternate moves.

_Player 1:_ Choses a block at (2, 6) to eat.

        _ _ _ _ _ _ _ _
    3  |_|_|_|_|_|_|_|_|
    2  |_|_|_|_|_|x|_|_|
    1  |$|_|_|_|_|_|_|_|
        1 2 3 4 5 6 7 8

_Player 2:_ Choses a block at (3, 3) to eat.

        _ _ _ _ _
    3  |_|_|x|_|_|
    2  |_|_|_|_|_|_ _ _
    1  |$|_|_|_|_|_|_|_|
        1 2 3 4 5 6 7 8

_Player 1:_ Choses a block at (1, 2) to eat.

        _ _
    3  |_|_|_ _ _
    2  |_|_|_|_|_|_ _ _
    1  |$|x|_|_|_|_|_|_|
        1 2 3 4 5 6 7 8

_Player 2:_ Choses a block at (2, 1) to eat.

        _
    3  |_|
    2  |x|
    1  |$|
        1

_Player 1:_ Doesn't have any option. So had to eat the bitter part of chocolate and be the loser.

        _
    1  |$|
        1

Of course this is not an optimal game.

As player 1 realised that he is noob after playing some steps, he asked you to help him to find whether now there exists any chance for him to win. Player 2 is expert at this game.

Given number of bar blocks in row<sub>1</sub>, row<sub>2</sub> and row<sub>3</sub> (row<sub>1</sub> ≥ row<sub>2</sub> ≥ row<sub>3</sub>) and its player 1 turn, find that if from now on he plays optimally whether he can win the game or not.

**Input Format**

First line of input containts number of test cases T. Then follows T lines, each line containing three positive integers row<sub>1</sub>, row<sub>2</sub> and row<sub>3</sub>, number of blocks of bar in row 1, row 2 and row 3 respectively.

**Output Format**

For each input, tell whether player 1 can win if he play optimally or not. Print `WIN` if player 1 can win, otherwise print `LOSE`.

**Constraints**


* 1 &le; row1 &le; 25
* 25 &ge; _row<sub>1</sub>_ &ge; _row<sub>2</sub>_ &ge; _row<sub>3</sub>_ &ge; 0

* Currently it's player 1' turn.

*  0 < _T_ ≤ 100

* Both players play optimally.


**Sample Input**

    2
    1 1 1
    2 2 1

**Sample Output**

    WIN
    LOSE

**Explanation**
*Test Case #00:*  Player 1 can easily win this game.

_Player 1:_ Eats block (2, 1).

        _
    3  |_|
    2  |x|
    1  |$|
        1

_Player 2:_ Does'nt have any option other than to eat block (1, 1) and lose, thus Player 1 `WIN`.

        _
    1  |$|
        1

*Test Case #01:* Player 1 is doomed to lose this game for any of his move. Let us explain what happen if he eats block (1, 2).

_Player 1:_ Eats block (1, 2)

        _
    3  |_|_
    2  |_|_|
    1  |$|x|
        1 2

_Player 2:_ Eats block (2, 1).

        _
    3  |_|
    2  |x|
    1  |$|
        1

_Player 1:_ Doesn't have any option other than to eat block (1, 1) and `LOSE`.

        _
    1  |$|
        1

## Sample Tests

### Test 1

```
_ _ _ _ _ _ _ _
3 |_|_|_|_|_|_|_|_|
2 |_|_|_|_|_|x|_|_|
1 |$|_|_|_|_|_|_|_|
 1 2 3 4 5 6 7 8
```

### Test 2

```
_ _ _ _ _
3 |_|_|x|_|_|
2 |_|_|_|_|_|_ _ _
1 |$|_|_|_|_|_|_|_|
 1 2 3 4 5 6 7 8
```

### Test 3

```
_ _
3 |_|_|_ _ _
2 |_|_|_|_|_|_ _ _
1 |$|x|_|_|_|_|_|_|
 1 2 3 4 5 6 7 8
```

### Test 4

```
_
3 |_|
2 |x|
1 |$|
 1
```

### Test 5

```
_
1 |$|
 1
```

### Test 6

```
2
1 1 1
2 2 1
```

### Test 7

```
WIN
LOSE
```

### Test 8

```
_
3 |_|
2 |x|
1 |$|
 1
```

### Test 9

```
_
1 |$|
 1
```

### Test 10

```
_
3 |_|_
2 |_|_|
1 |$|x|
 1 2
```

### Test 11

```
_
3 |_|
2 |x|
1 |$|
 1
```

### Test 12

```
_
1 |$|
 1
```
