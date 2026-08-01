# A Chessboard Game

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.8919376195380315
- **Total Submissions:** 13594
- **Solved Count:** 12125
- **URL:** https://www.hackerrank.com/challenges/a-chessboard-game-1

## Problem Statement

Two players are playing a game on a $15 \times 15$ chessboard. The rules of the game are as follows:

* The game starts with a single coin located at some $x,y$ coordinates. The coordinates of the upper left cell are $(1,1)$, and of the lower right cell are $(15,15)$.

* In each move, a player must move the coin from cell $(x,y)$ to one of the following locations:
	1. $(x-2,y+1)$ 
    2. $(x-2,y-1)$ 
    3. $(x+1,y-2)$ 
    4. $(x-1,y-2)$

	**Note:** The coin must remain inside the confines of the board.

* Beginning with player 1, the players alternate turns. The first player who is unable to make a move loses the game.

The figure below shows all four possible moves using an $8 \times 8$ board for illustration:

![chess(1)](https://s3.amazonaws.com/hr-challenge-images/19825/1459017588-a9b7aa42b4-chess1.png)

Given the initial coordinates of the players' coins, assuming optimal play, determine which player will win the game. 

**Function Description**

Complete the *chessboardGame* function in the editor below.  It should return a string, either `First` or `Second`.

chessboardGame has the following parameter(s):  

- *x*: an integer that represents the starting column position   
- *y*: an integer that represents the starting row position  

## Input Format

The first line contains an integer $t$, the number of test cases. 	
Each of the next $t$ lines contains $2$ space-separated integers $x$ and $y$.

## Output Format

On a new line for each test case, print $\texttt{First}$ if the first player is the winner.  Otherwise, print $\texttt{Second}$.

## Constraints

* $1 \le t \le 225$
* $1 \le x[i],y[i] \le 15$

## Sample Input

5 2
5 3
8 8

## Sample Output

Second
First
First

## Explanation

In the first case, player1 starts at the red square and can move to any of the blue squares.  Regardless of which one is chosen, the player 2 can move to one of the green squares to win the game.

In the second case, player 1 starts at the red square and can move to any of the blue squares or the purple one.  Moving to the purple one limits player 2 to the yellow square.  From the yellow square, player 1 moves to the green square and wins.
