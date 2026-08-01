# Fun Game

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.6366112775810406
- **Total Submissions:** 3671
- **Solved Count:** 2337
- **URL:** https://www.hackerrank.com/challenges/fun-game-1

## Problem Statement

Kyle and Mike are bored on a rainy day and decide to pass the time by creating a new game having the following rules:

* The game starts with two $n$-sized integer arrays, $A$ and $B$, and is played by two players, $P_1$ and $P_2$. 
* The players move in alternating turns, with $P_1$ always moving first. During each move, the current player must choose an integer, $i$, such that $0 \le i \le n-1$. If the current player is $P_1$, then $P_1$ receives $A_i$ points; if the current player is $P_2$, then $P_2$ receives $B_i$ points.
* Each value of $i$ can be chosen only once. That is, if a value of $i$ is already chosen by some player, none of the player can re-use it. So, game always ends after $n$ moves.
* The player with the maximum number of points wins.
* The arrays A and B are accessible to both the players P1 and P2. So the players make a optimal move at every turn. 

Given the values of $n$, $A$, and $B$, can you determine the outcome of the game? Print $\texttt{First}$ if $P_1$ will win, $\texttt{Second}$ if $P_2$ will win, or $\texttt{Tie}$ if they will tie. Assume both players always move optimally.

## Input Format

The first line of input contains a single integer, $T$, denoting the number of test cases. Each of the $3T$ subsequent lines describes a test case. A single test case is defined over the following three lines:

1. An integer, $n$, denoting the number of elements in arrays $A$ and $B$.
2. $n$ space-separated integers, $A_{0}, A_{1}, \ldots, A_{n-1}$, where each $A_i$ describes the element at index $i$ of array $A$.
3. $n$ space-separated integers, $B_{0}, B_{1}, \ldots, B_{n-1}$, where each $B_i$ describes the element at index $i$ of array $B$.

## Output Format

For each test case, print one of the following predicted outcomes of the game on a new line:

- Print $\texttt{First}$ if $P_1$ will win.
- Print $\texttt{Second}$ if $P_2$ will win.
- Print $\texttt{Tie}$ if the two players will tie.

## Constraints

* $1 \leq T \leq 10$ 
* $1 \leq n \leq 1000$ 
* $1 \leq A_i, B_i \leq 10^5$ 

## Sample Input

3
1 3 4
5 3 1
2
1 1
1 1
2
2 2
3 3

## Sample Output

First
Tie
Second

## Explanation

Test Case 0: ,
The players make the following  moves:

-  chooses  and receives  points.

-  chooses  and receives  points. Note that  will not choose , because this would cause  to win.

-  chooses  (which is the only remaining move) and receives  points.

As all  moves have been made, the game ends. 's score is  points and 's score is  points, so  is the winner and we print  on a new line.

Test Case 1: ,
Because both players will only make  move and all possible point values are , the players will end the game with equal scores. Thus, we print  on a new line.

Test Case 1: ,

Because both players will only make  move and all the possible point values for  are greater than all the possible point values for ,  will win the game. Thus, we print  on a new line.
