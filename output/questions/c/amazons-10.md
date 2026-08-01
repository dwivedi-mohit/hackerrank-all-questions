# Amazons

- **Domain:** c
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.15261044176706828
- **Total Submissions:** 249
- **Solved Count:** 38
- **URL:** https://www.hackerrank.com/challenges/amazons-10

## Problem Statement

[Amazons](https://en.wikipedia.org/wiki/Game_of_the_Amazons) is a 2 player abstract strategy games that takes place on a chess board of size 10x10. Each player has 4 amazons (represented as Queens of Chess) as shown in the board below. 

![amazons-board](https://s3.amazonaws.com/hr-assets/0/1526565059-54f8c55bd9-amazons-game.png)

A player is either white or black with white moving first. Each move consists of 2 parts:  one of the current player's amazon is moved from its current position to a new empty square in a straight line (orthogonally or diagonally) not crossing any non-empty square (similar to a Queen's movement in Chess). The second part consists of the amazon shooting an arrow from its new square to an empty square in a straight line (orthogonally or diagonally) not crossing any non-empty square. The amazon can also shoot an arrow in the direction it traveled. The last player to make a move wins.

**Input Format**

The board is indexed 'a' (ascii value 97) to 'j' (ascii value 106) from left to right and '0' ( ascii value 48 ) to '9' (ascii value 57) from bottom to top as shown in the figure above. White amazons are represented by the character 'W' (ascii value 87) and the Black amazons are represented by the character 'B' ( ascii value 66). Empty squares are represented by '-' (ascii value 45) and the squares where arrows land are represented by '.' (ascii value 46).

The first line of the input is either 'W' or 'B' representing the 1<sup>st</sup> or the 2<sup>nd</sup> player. 
The 2<sup>nd</sup> line has 10 10 which is the row/column size of the board.
10 lines follow each line having 10 characters representing a row in the board. 

**Output Format**

Output the position of the amazon you wish to move followed by the new position of the amazon and finally print the position of the square where the arrow should land. The output is written as 

    <char><num> <char><num> <char><num>

**Sample Input**

    W
    10 10
    B----.B---
    ....-....-
    ..W.---B..
    W..-----.-
    ..--------
    -.------..
    --B----..W
    ---.--...-
    ------.W--
    -----...--

**Sample Output**

    h1 j1 i1

**Explanation**

The current player is white. He moves one of his amazons positioned at *h1* 
to *j1* and shoots an arrow that lands at *i1*. The new configuration of the board is 

    B----.B---
    ....-....-
    ..W.---B..
    W..-----.-
    ..--------
    -.------..
    --B----..W
    ---.--...-
    ------.-.W
    -----...--

**Task**

Complete the function *next_move* that takes a character *player* and a 2-D array of character *board* as input and prints the output.

## Input Format

The board is indexed 'a' (ascii value 97) to 'j' (ascii value 106) from left to right and '0' ( ascii value 48 ) to '9' (ascii value 57) from bottom to top as shown in the figure above. White amazons are represented by the character 'W' (ascii value 87) and the Black amazons are represented by the character 'B' ( ascii value 66). Empty squares are represented by '-' (ascii value 45) and the squares where arrows land are represented by '.' (ascii value 46).

The first line of the input is either 'W' or 'B' representing the 1st or the 2nd player.
The 2nd line has 10 10 which is the row/column size of the board.
10 lines follow each line having 10 characters representing a row in the board.

## Output Format

Output the position of the amazon you wish to move followed by the new position of the amazon and finally print the position of the square where the arrow should land. The output is written as

<char><num> <char><num> <char><num>

## Sample Input

W
10 10
B----.B---
....-....-
..W.---B..
W..-----.-
..--------
-.------..
--B----..W
---.--...-
------.W--
-----...--

## Sample Output

h1 j1 i1

## Explanation

The current player is white. He moves one of his amazons positioned at h1
to j1 and shoots an arrow that lands at i1. The new configuration of the board is

B----.B---
....-....-
..W.---B..
W..-----.-
..--------
-.------..
--B----..W
---.--...-
------.-.W
-----...--

Task

Complete the function next_move that takes a character player and a 2-D array of character board as input and prints the output.
