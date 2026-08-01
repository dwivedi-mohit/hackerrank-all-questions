# Chessboard Game, Again!

- **Domain:** regex
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.7558049535603715
- **Total Submissions:** 2584
- **Solved Count:** 1953
- **URL:** https://www.hackerrank.com/challenges/chessboard-game-again-1

## Problem Statement

Two players are playing a game on a $15 \times 15$ chessboard. The rules of the game are as follows:

* The game starts with $k$ coins located at one or more $(x,y)$ coordinates on the board (a single cell may contain more than one coin). The coordinate of the upper left cell is $(1,1)$, and the coordinate of the lower right cell is $(15,15)$.
* In each move, a player must move a single coin from some cell $(x,y)$ to one of the following locations:
	1. $(x-2,y+1)$ 
    2. $(x-2,y-1)$ 
    3. $(x+1,y-2)$ 
    4. $(x-1,y-2)$. 
    
    **Note:** The coin must remain inside the confines of the board.

* The players move in alternating turns. The first player who is unable to make a move loses the game.

The figure below shows all four possible moves:

![chess](https://s3.amazonaws.com/hr-challenge-images/19574/1458463909-1760b192c9-chess.png)

**Note:** While the figure shows a $8 \times 8$ board, this game is played on a $15 \times 15$ board.

Given the value of $k$ and the initial coordinate(s) of $k$ coins, determine which player will win the game. Assume both players always move optimally.

## Input Format

The first line contains an integer, $T$, denoting the number of test cases. 	
Each test case is defined as follows over the subsequent lines:

1. The first line contains an integer, $k$, denoting the number of coins on the board.
2. Each line $i$ (where $0 \le i \lt k$) of the $k$ subsequent lines contains $2$ space-separated integers describing the respective values of $x_i$ and $y_i$ of the coordinate where coin $k_i$ is located.

**Note:** Recall that a cell can have more than one coin (i.e., any cell can have $0$ to $k$ coins in it at any given time).

## Output Format

On a new line for each test case, print $\texttt{First}$ if the first player is the winner; otherwise, print $\texttt{Second}$.

## Constraints

* $1 \le T \le 1000$
* $1 \le k \le 1000$
* $1 \le x_i,y_i \le 15$, where $0 \le i \lt k$.

## Sample Input

3
5 4
5 8
8 2
6
7 1
7 2
7 3
7 4
7 4
7 4

## Sample Output

First
Second
