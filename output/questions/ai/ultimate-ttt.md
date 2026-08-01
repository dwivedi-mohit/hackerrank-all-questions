# Ultimate Tic Tac Toe

- **Domain:** ai
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.3878504672897196
- **Total Submissions:** 214
- **Solved Count:** 83
- **URL:** https://www.hackerrank.com/challenges/ultimate-ttt

## Problem Statement

We all know [Tic-Tac-Toe](https://www.hackerrank.com/challenges/tic-tac-toe) ends in a predictable draw when both players choose optimal moves. To make the game interesting, a group of mathematicians decided to fill in each square of the board with a smaller Tic-Tac-Toe board to produce what is now called **Ultimate Tic-Tac-Toe**.

![tic-tac-toe](https://s3.amazonaws.com/hr-assets/0/1526565329-5f681d4019-uttt.png)

**Challenge**

Your goal is to play a valid game against a bot. You need to win the game by continually printing the best next move, based on the game rules below. You will lose the test case if you write to an invalid board and/or write to a square that already has an X or O.

For the purposes of these instructions:

- **board** = one of the 9 tic-tac-toe game boards
- **square** = one of the 81 individual squares

**Game Rules**

Like the original Tic-Tac-Toe, Player 1 is represented by 'X' (ascii value: 88) and Player 2 is represented by 'O' (ascii value: 79). To start the game, Player 1 places an X on any one of the 81 empty squares, and then players alternate turns.

However, after the initial move, players must play the board that mirrors the square from the previous player.

![alt](https://s3.amazonaws.com/hr-assets/0/1526565391-9ccf63e616-ozxCl8.png)

For example: If Player 1 places an X in the upper-right *square* of a board, then Player 2 must play the upper-right *board*.


![alt2](https://s3.amazonaws.com/hr-assets/0/1526565478-18f99febf4-cY1BEf.png)

Continuing the example: If Player 2 places an O on the lower-middle square, then Player 1 must next play the lower-middle board.

Here are the necessary exceptions:

If the next move is to a board that is full or has already been won, then that player may choose an **open** square on **any** board, for that turn.

If a player marks 3 consecutive squares (horizontally, vertically or diagonally) on any given board, he wins that board. The first player to win 3 consecutive *boards* (horizontally, vertically or diagonally) wins
the game.

**Input Format**

Line 1 indicates the player with the next move and is represented by character 'X' or 'O' for Player 1 or Player 2, respectively.

Line 2 indicates the board to be played (as determined by the previous move), and is represented by 2 spaced integers as follows:

![uttt-indexed](https://s3.amazonaws.com/hr-assets/0/1526565563-5225fde877-uttt-indexed.png)

If the player is allowed to play *any* of the 9 boards, the integers will be printed as "-1 -1".

Lines 3 through 11 reflect the contents of all 81 squares in the same order as displayed in the figure. Each square is referenced first by the board in which it is present (0 ≤ x,y ≤ 2) and its position inside it (0 ≤ x,y ≤ 2). i.e., a square (1,1) inside board (0,2) is referred as `0 2 1 1`.  Each line contains 9 characters, using "X", "O", or "-" to represent the state of a square. Character "-" (ascii value: 45) indicates an open (unmarked) square. The characters are listed in the same order as the boards, in other words: top row (left to right), then middle row (left to right), then bottom row (left to right).

**Output**

You will indicate a valid next move by a single line containing 4 spaced integers, as follows:

-   The first two integers indicate the board, using the input convention above.

-   The second two integers indicate the square within that board.

For example: An output of `"1 1 1 1"` would mark the center square of the entire Ultimate game board.

![alt5](https://s3.amazonaws.com/hr-assets/0/1526565627-e9208524af-OyYVs6.png)

**Sample Input**

    O
    2 2
    ---------
    ---------
    --X------
    ---------
    ---------
    ---------
    ---------
    ---------
    ---------

**Sample Output**

    2 2 0 0

**Explanation**

In the previous move, 'X' makes the first move, placing an X on board number "0 0", square "2 2". Now, 'O' is forced to make a move only inside board "2 2". He chooses to mark the square "0 0". The resulting board is shown below.

    X
    0 0
    ---------
    ---------
    --X------
    ---------
    ---------
    ---------
    ------O--
    ---------
    ---------

Now, X is forced to mark a cell only inside `0 0`
More details of the game are given [here](http://bejofo.net/ttt)

## Input Format

Line 1 indicates the player with the next move and is represented by character 'X' or 'O' for Player 1 or Player 2, respectively.

Line 2 indicates the board to be played (as determined by the previous move), and is represented by 2 spaced integers as follows:

If the player is allowed to play any of the 9 boards, the integers will be printed as "-1 -1".

Lines 3 through 11 reflect the contents of all 81 squares in the same order as displayed in the figure. Each square is referenced first by the board in which it is present (0 ≤ x,y ≤ 2) and its position inside it (0 ≤ x,y ≤ 2). i.e., a square (1,1) inside board (0,2) is referred as 0 2 1 1.  Each line contains 9 characters, using "X", "O", or "-" to represent the state of a square. Character "-" (ascii value: 45) indicates an open (unmarked) square. The characters are listed in the same order as the boards, in other words: top row (left to right), then middle row (left to right), then bottom row (left to right).

Output

You will indicate a valid next move by a single line containing 4 spaced integers, as follows:

- The first two integers indicate the board, using the input convention above.

- The second two integers indicate the square within that board.

For example: An output of "1 1 1 1" would mark the center square of the entire Ultimate game board.

## Sample Input

O
2 2
---------
---------
--X------
---------
---------
---------
---------
---------
---------

## Sample Output

2 2 0 0

## Explanation

In the previous move, 'X' makes the first move, placing an X on board number "0 0", square "2 2". Now, 'O' is forced to make a move only inside board "2 2". He chooses to mark the square "0 0". The resulting board is shown below.

X
0 0
---------
---------
--X------
---------
---------
---------
------O--
---------
---------

Now, X is forced to mark a cell only inside 0 0
More details of the game are given here
