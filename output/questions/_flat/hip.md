# Hip

---

| Field | Value |
|---|---|
| **Slug** | `hip` |
| **Domain** |  |
| **Difficulty** | Advanced |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/hip |

---

## Preview

Hip is a classic game played on a square board. Each player takes turns placing tokens on an unoccupied position. The objective is to avoid completing a square on the board by marking all four of your tokens. The first player who completes a square loses.

## Problem Statement

Hip is a classic board game invented by [Martin Gardner](https://en.wikipedia.org/wiki/Martin_Gardner). It's a 2 player game played on a 9x9 board. Players take turns placing a token on an unoccupied cell. The player who completes any square such that 4 corners are marked by his token <b>loses</b>. The square may be of any size and can be tilted at any angle.

Here are a couple of game states that shows the players lose by completing a square. <br/><br/>

![image alt](https://ferrari.interviewstreet.com/hackerrank/hip.png)<br/><br/>

The function <b> nextMove</b> takes in a character <i> player</i>

and an 9x9 char <i>board</i> as an input and provides 2 integer

positions row and column space separated as output. The board is 0-indexed.



**Example Input**



    b

    r--------

    ---------

    --r------

    ---b--b--

    --r------

    ---------

    ---------

    ---------

    ---------



**Example Output**



    0 1



The board results in the following state



    rb-------

    ---------

    --r------

    ---b--b--

    --r------

    ---------

    ---------

    ---------

    ---------



First player is identified by token **r**, the second player by **b** and an unoccupied cell is identified by **-** (ascii value:45)

## Sample Tests

### Test 1

```
b
r--------
---------
--r------
---b--b--
--r------
---------
---------
---------
---------
```

### Test 2

```
0 1
```

### Test 3

```
rb-------
---------
--r------
---b--b--
--r------
---------
---------
---------
---------
```
