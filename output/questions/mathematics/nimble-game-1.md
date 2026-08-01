# Nimble Game

- **Domain:** mathematics
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.7658921076875832
- **Total Submissions:** 9769
- **Solved Count:** 7482
- **URL:** https://www.hackerrank.com/challenges/nimble-game-1

## Problem Statement

Two people are playing Nimble! The rules of the game are:

- The game is played on a line of $n$ squares, indexed from $0$ to $n-1$. Each square $i$ (where $0 \le i \lt n$) contains $c_{i}$ coins. For example:	
	![nimble.png](https://s3.amazonaws.com/hr-challenge-images/18624/1457422376-06a45e063f-nimple.png)
- The players move in alternating turns. During each move, the current player must  remove exactly $1$ coin from square $i$ and move it to square $j$ if and only if $0 \le j \lt i$.
- The game ends when all coins are in square $0$ and nobody can make a move. The first player to have no available move loses the game.

Given the value of $n$ and the number of coins in each square, determine whether the person who wins the game is the *first* or *second* person to move. Assume both players move optimally.

## Input Format

The first line contains an integer, $T$, denoting the number of test cases.		
Each of the $2T$ subsequent lines defines a test case. Each test case is described over the following two lines:

1. An integer, $n$, denoting the number of squares.
2. $n$ space-separated integers, $c_{0}, c_{1}, \ldots, c_{n-1}$, where each $c_i$ describes the number of coins at square $i$.

## Output Format

For each test case, print the name of the winner on a new line (i.e., either $\texttt{First}$ or $\texttt{Second}$).

## Constraints

- $1 \le T \le 10^4$
- $1 \le n \le 100$
- $0 \le c_i \le 10^9$

## Sample Input

5
0 2 3 0 6
4
0 0 0 0

## Sample Output

First
Second

## Explanation

Explanation for  testcase:

The first player will shift one coin from  to . Hence, the second player is left with the squares . Now whatever be his/her move is, the first player can always nullify the change by shifting a coin to the same square where he/she shifted it. Hence the last move is always played by the first player, so he wins.

Exlanation for  testcase:

There are no coins in any of the squares so the first player cannot make any move, hence second player wins.
