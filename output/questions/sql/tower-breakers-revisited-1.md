# Tower Breakers, Revisited!

- **Domain:** sql
- **Difficulty:** Medium
- **Max Score:** 25
- **Success Ratio:** 0.6246031746031746
- **Total Submissions:** 5040
- **Solved Count:** 3148
- **URL:** https://www.hackerrank.com/challenges/tower-breakers-revisited-1

## Problem Statement

Two players (numbered $1$ and $2$) are playing a game of Tower Breakers! The rules of the game are as follows:

- Player $1$ always moves first, and both players always move optimally.
- Initially there are $N$ towers of various heights.
- The players move in alternating turns. In each turn, a player can choose a tower of height $X$ and reduce its height to $Y$, where $1 \le Y \lt X$ and $Y$ evenly divides $X$.
- If the current player is unable to make any move, they lose the game.

Given the value of $N$ and the respective height values for all towers, can you determine who will win? If the first player wins, print $1$; otherwise, print $2$.

## Input Format

The first line contains an integer, $T$, denoting the number of test cases.		
Each of the $2T$ subsequent lines defines a test case. Each test case is described over the following two lines:

1. An integer, $N$, denoting the number of towers.
2. $N$ space-separated integers, $h_{0}, h_{1}, \ldots, h_{N-1}$, where each $h_i$ describes the height of tower $i$.

## Output Format

For each test case, print a single integer denoting the winner (i.e., either $1$ or $2$) on a new line.

## Constraints

* $1 \leq T \leq 100 $
* $1 \leq N \leq 100 $
* $1 \leq h_i \leq 10^6 $

## Sample Input

2
1 2
3
1 2 3

## Sample Output

2

## Explanation

Test Case 0:

Player  reduces the second tower to height  and subsequently wins.

Test Case 1:

There are two possible moves:

- Reduce the second tower to

- Reduce the third tower to .

Whichever move player  makes, player  will make the other move. Thus, player  wins.
