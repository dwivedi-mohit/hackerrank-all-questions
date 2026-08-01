# Camelot

- **Domain:** python
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.760932944606414
- **Total Submissions:** 343
- **Solved Count:** 261
- **URL:** https://www.hackerrank.com/challenges/camelot

## Problem Statement

Camelot is  a strategic board game played by 2 players. 

The game is played on a board of 160 squares, which is roughly rectangular (12×14), with three squares removed from each of the four corners, and four extra squares extending outside the main rectangle, two each at the top and bottom of the board. These two-square areas are called the castles. Each player starts the game with fourteen pieces: four knights and ten men, set up as shown (see diagram).

![camelot board](https://s3.amazonaws.com/hr-assets/0/1526566206-aedd9160b2-camelot_board.png)

Both knights and men can move either horizontally, vertically, or diagonally in three ways, as follows:

+ One space in any direction (like a king in chess). This is called a plain move.
+ A leaping move (called cantering) over an adjacent friendly piece to a 
vacant space immediately beyond. Multiple leaps over a player's own pieces are permitted. Cantering is always optional (never obligatory).
+ A jumping move over an adjacent enemy piece to a vacant space immediately beyond. The enemy piece is captured and removed from the board. As in checkers, multiple jumps are allowed, and capturing is obligatory whenever it is possible.

Men may make any of the three moves, but only one type of move per turn. Knights have a fourth option: a combination move consisting of a canter immediately followed by a jump (capture). This is called the knight's charge. The knight may, in this single move, perform multiple canters (or just one), followed by multiple jumps (or just one); but the canter(s) must precede the jump(s). A knight may not combine a plain move with a canter or a jump.

**Objective** 

The game is won if a player moves any two of his pieces (Knights and/or Men) into his opponent's castle. Or, the game is won if a player captures all of his opponent's pieces, and has two or more of his own pieces left. Or, the game is won if a player has two or more pieces, and his opponent is unable to make a legal move.

**Input Format**

The first line of the input contains a digit, 1 or 2 indicating if the player to perform the move is 1<sup>st</sup> player or 2<sup>nd</sup> player.  
16 lines follow, each line contains 12 characters. They can be one of the following 

+ `x` indicating an invalid position on the board.  
+ `-` indicating the empty position on the board.  
+ `S` indicating one of the men of the 1<sup>st</sup> player.  
+ `s` indicating one of the men of the 2<sup>nd</sup> player.  
+ `H` indicating one of the knight of the 1<sup>st</sup> player.  
+ `h` indicating one of the knight of the 2<sup>nd</sup> player.  

**Output Format**

Each row is indicated by a number [1-16] and each column is indicated by an upper case english character [A-L]. So, the two castles of the 1<sup>st</sup> player is represented by the location `F1` and `G1` and the 2<sup>nd</sup> player is represented by the location `F16` and `G16`.  

As only 1 pawn can be moved across the board in 1 move, the output format to move a particular pawn would be space separated positions of it's initial position, intermediate position and ending with it's final position.  

**Sample Input**

    2
    xxxxx--xxxxx
    xx--------xx
    x----------x
    ------------
    ------------
    ------ss----
    ---ss-------
    ------------
    --h---------
    ------------
    --s--SSS----
    -h--SSSS----
    -h----S-----
    x----------x
    xx-H------xx
    xxxxx--xxxxx

**Sample Output**

    B4 B6 D6 F4 H4

**Resulting Board**  

    xxxxx--xxxxx
    xx--------xx
    x----------x
    ------------
    ------------
    ------ss----
    ---ss-------
    ------------
    --h---------
    ------------
    --s--SSS----
    -h---SSS----
    -------h----
    x----------x
    xx-H------xx
    xxxxx--xxxxx

**Explanation**  

In this move, the 2<sup>nd</sup> player's Knight makes a Knight's charge by first performing a cantering move from `B4` to `B6`, `B6` to `D6` and follows it up with a jumping move from `D6` to `F4` and another jumping move from `F4` to `H4`.  

Full rules of the game can be seen on the game's [wikipedia](https://en.wikipedia.org/wiki/Camelot_(board_game)

## Input Format

The first line of the input contains a digit, 1 or 2 indicating if the player to perform the move is 1st player or 2nd player.

16 lines follow, each line contains 12 characters. They can be one of the following

- x indicating an invalid position on the board.

- - indicating the empty position on the board.

- S indicating one of the men of the 1st player.

- s indicating one of the men of the 2nd player.

- H indicating one of the knight of the 1st player.

- h indicating one of the knight of the 2nd player.

## Output Format

Each row is indicated by a number [1-16] and each column is indicated by an upper case english character [A-L]. So, the two castles of the 1st player is represented by the location F1 and G1 and the 2nd player is represented by the location F16 and G16.

As only 1 pawn can be moved across the board in 1 move, the output format to move a particular pawn would be space separated positions of it's initial position, intermediate position and ending with it's final position.

## Sample Input

xxxxx--xxxxx
xx--------xx
x----------x
------------
------------
------ss----
---ss-------
------------
--h---------
------------
--s--SSS----
-h--SSSS----
-h----S-----
x----------x
xx-H------xx
xxxxx--xxxxx

## Sample Output

B4 B6 D6 F4 H4

Resulting Board

xxxxx--xxxxx
xx--------xx
x----------x
------------
------------
------ss----
---ss-------
------------
--h---------
------------
--s--SSS----
-h---SSS----
-------h----
x----------x
xx-H------xx
xxxxx--xxxxx

## Explanation

In this move, the 2nd player's Knight makes a Knight's charge by first performing a cantering move from B4 to B6, B6 to D6 and follows it up with a jumping move from D6 to F4 and another jumping move from F4 to H4.

Full rules of the game can be seen on the game's [wikipedia](https://en.wikipedia.org/wiki/Camelot_(board_game)
