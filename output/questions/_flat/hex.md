# Hex

---

| Field | Value |
|---|---|
| **Slug** | `hex` |
| **Domain** |  |
| **Difficulty** | Hard |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/hex |

---

## Preview

hex game

## Problem Statement

[HEX](http://en.wikipedia.org/wiki/Hex_(board_game)) is a 2-player strategy board game played on a [hexagonal grid](http://en.wikipedia.org/wiki/Hex_map), theoretically of any size and several possible shapes, but traditionally as a 11×11 rhombus. 


Players take turns placing a stone of their color (blue or red) on a single cell within the overall playing board. The goal is to form a connected path of your stones linking the opposing sides of the board marked by your colors, before your opponent connects his or her sides in a similar fashion. The first player to complete his or her connection wins the game. The four corner hexagons each belong to both adjacent sides. (src: wikipedia)

For the first player, the path runs from LEFT to RIGHT and for the second player, the path runs from top to bottom. 

A 11×11 hex game board showing a winning configuration for blue is as shown below :<br><br>

![winning-HEX-board](http://upload.wikimedia.org/wikipedia/commons/3/38/Hex-board-11x11-%282%29.jpg)
<br><br>

**Input format**

The first line of the input is either 'B' (ascii value: 66) or 'R' (ascii value: 82) representing the 1<sup>st</sup> and the 2<sup>nd</sup> player respectively. Twelve lines follow with the first line containing the integer 11<sup>*</sup> and then each line having eleven characters representing a row in the board. An unoccupied hex is represented by '-' (ascii value: 45)

The board is indexed on the top left as "a1" and the bottom right as "k11" - the columns are alphabets and rows are integers.

**Output format**

Players take turns placing their respective pieces on an unoccupied hex. Print the cell as given format i.e. a character and an integer without any space. For example "c4" is a valid move. 

**Sample input**  


	R
    11
	R----------
    ---R-------
    B----------
    -----B-----
    R----------
    --------R--
    --R--------
    --------B--
    ---B-------
    ---B-------
    ---B------- 
 
**Sample output**

    b3

**Explanation**  

b3 is 1 step right and 2 steps down from top left. After the move, the configuration of board will be

    R----------
    ---R-------
    BR---------
    -----B-----
    R----------
    --------R--
    --R--------
    --------B--
    ---B-------
    ---B-------
    ---B-------

**Task**   

Given a board state, output the next move. We have designed the codechecker such that it alternates the control to make a move between the two players. Every submission will have two games - one with you as the first player and the other as second player.

**Notes & caveat**

As this is a first player win game, we follow a slight variation to the [pie rule](http://en.wikipedia.org/wiki/Pie_rule) to make the game fair. The first move of the board alone is decided by the 2<sup>nd</sup> player. 

When the game starts, the board looks like this. The control of making this move is with the 2<sup>nd</sup> player.

	R	
    11
    -----------
    -----------
    -----------
    -----------
    -----------
    -----------
    -----------
    -----------
    -----------
    -----------
    -----------

Let's say the output is b4, the board state becomes

    -----------
    -----------
    -----------
    -B---------
    -----------
    -----------
    -----------
    -----------
    -----------
    -----------
    -----------

The next board state will look like the one below with the control again with the 2<sup>nd</sup> player.

	R
    11
    -----------
    -----------
    -----------
    -B---------
    -----------
    -----------
    -----------
    -----------
    -----------
    -----------
    -----------

Let's say the output is b5, the board states becomes

	R
    11
    -----------
    -----------
    -----------
    -B---------
    -R---------
    -----------
    -----------
    -----------
    -----------
    -----------
    -----------

The next board state will be the one below with the control to the 1<sup>st</sup> player 

	B
    11
    -----------
    -----------
    -----------
    -B---------
    -R---------
    -----------
    -----------
    -----------
    -----------
    -----------
    -----------

It keeps alternating from hereon. 

<i>Why do we need the integer 11 in the input?</i> <br />
We plan to design extended versions of this game with other rhombus board sizes and we wouldn't want you to resubmit your code everytime.

## Sample Tests

### Test 1

```
R
11
R----------
---R-------
B----------
-----B-----
R----------
--------R--
--R--------
--------B--
---B-------
---B-------
---B-------
```

### Test 2

```
R----------
---R-------
BR---------
-----B-----
R----------
--------R--
--R--------
--------B--
---B-------
---B-------
---B-------
```

### Test 3

```
R 
11
-----------
-----------
-----------
-----------
-----------
-----------
-----------
-----------
-----------
-----------
-----------
```

### Test 4

```
-----------
-----------
-----------
-B---------
-----------
-----------
-----------
-----------
-----------
-----------
-----------
```

### Test 5

```
R
11
-----------
-----------
-----------
-B---------
-----------
-----------
-----------
-----------
-----------
-----------
-----------
```

### Test 6

```
R
11
-----------
-----------
-----------
-B---------
-R---------
-----------
-----------
-----------
-----------
-----------
-----------
```

### Test 7

```
B
11
-----------
-----------
-----------
-B---------
-R---------
-----------
-----------
-----------
-----------
-----------
-----------
```
