# Digits Square Board

- **Domain:** python
- **Difficulty:** Medium
- **Max Score:** 35
- **Success Ratio:** 0.7198863636363636
- **Total Submissions:** 1760
- **Solved Count:** 1267
- **URL:** https://www.hackerrank.com/challenges/digits-square-board-1

## Problem Statement

Two HackerRank staffers found a secret room with a mysterious $N \times N$ square board and decided to play a game with it. The game has the following rules:

- At the beginning of the game, the players write a single digit (given as input) ranging from $1$ to $9$ in each $1 \times 1$ cell composing the $N \times N$ square board. 
- The players move in alternating turns. In each move, the current player performs the following actions:
	1. Chooses a board that has at least one *non-prime* number written on it and has more than one cell (i.e., dimensions $\gt 1 \times 1$). 
    2. Cuts the chosen board into $2$ smaller boards by breaking it along any horizontal or vertical line at the edge of a cell.

	**Note:** Although the game starts with one $N \times N$ board, that board is split in two during each move. At the beginning of the $k^{th}$ move, a player can choose any one of the $k$ pieces of the original board (as long as it can have a legal move performed on it).

- The game ends when there are no more cuttable boards (i.e., there are $N \cdot (1 \times 1)$ boards, or all boards have only prime numbers written on them). The first player who is unable to make a move loses.

Given the value of $n$ and the respective numbers written in each $(i,j)$ cell of the board, determine whether the person who wins the game is the first or second person to move. Assume both players move optimally.

**Time Limit**

* Python: 18 seconds
* Pypy2: 5 seconds

For other languages, the time limit is [standard](https://www.hackerrank.com/environment).

## Input Format

The first line contains an integer, $T$, denoting the number of test cases.		
Each test case is defined as follows over the subsequent lines:

1. An integer, $N$, denoting the length of each of the board's sides.
2. Each line $i$ of the $n$ subsequent lines contains $n$ space-separated integers describing $A_{(i,0)}, A_{(i,1)}, \ldots, A_{(i,n-1)}$, where each $A_{(i,j)}$ describes the number written in cell $(i,j)$ of the board.

## Output Format

For each test case, print the name of the player with the winning strategy on a new line (i.e., either $\texttt{First}$ or $\texttt{Second}$).

## Constraints

- $1 \leq T \leq 10 $
- $1 \leq N \leq 30 $
- $ 1\leq A_{(i,j)} \leq 9 $

## Sample Input

3
2 7 5
2 7 5
7 7 7
2
4 3
1 2

## Sample Output

Second
First

## Explanation

We'll refer to the two players as  and .

Test Case 0:

All cells contain prime numbers, so there are no valid moves available to . As  wins by default, we print  on a new line.

Test Case 1:

In this test case, the two players perform the following sequence of moves:

-  makes a horizontal cut, splitting the board into two  boards. This is demonstrated in the following diagram:

-  now chooses one of the two  rectangles and cuts it vertically, splitting it into two  squares.

-  chooses remaining  rectangle and cuts it vertically, splitting it into two  squares.

After the above  moves take place, the board is split into four  squares and no more moves are available for  to make. Thus,  wins and we print  on a new line.
