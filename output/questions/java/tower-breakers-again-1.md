# Tower Breakers, Again!

- **Domain:** java
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.6175202156334232
- **Total Submissions:** 3710
- **Solved Count:** 2291
- **URL:** https://www.hackerrank.com/challenges/tower-breakers-again-1

## Problem Statement

Two players (numbered $1$ and $2$) are playing a game of Tower Breakers! The rules of the game are as follows:

- Player $1$ always moves first.
- Initially there are $N$ towers of various heights.
- The players move in alternating turns. In each turn, a player must choose a tower of height $X$ and break it down into $Y$ towers, each of height $Z$. The numbers $Y$ and $Z$ must satisfy $Y \times Z = X$ and $Y \gt 1$.  
- If the current player is unable to make any move, they lose the game.

Given the value of $N$ and the respective height values for all towers, can you determine who will win, assuming both players always move *optimally*? If the first player wins, print $1$; otherwise, print $2$.

## Input Format

The first line contains an integer, $T$, denoting the number of test cases.		
The $2T$ subsequent lines define the test cases. Each test case is described by two lines:

1. An integer, $N$, denoting the number of towers.
2. $N$ space-separated integers, $h_{0}, h_{1}, \ldots, h_{N-1}$, where each $h_i$ describes the height of tower $i$.

## Output Format

For each test case, print a single integer denoting the winner (i.e., either $1$ or $2$) on a new line.

## Constraints

- $1 \leq T \leq 200 $
- $1 \leq N \leq 100 $
- $1 \leq h_i \leq 10^5 $

## Sample Input

2
1 2
3
1 2 3

## Sample Output

2

## Explanation

In the first test case, the first player simply breaks down the second tower of height  into two towers of height  and wins.

In the second test case, there are only two possible moves:

- Break the second tower into  towers of height .

- Break the third tower into  towers of height .

Whichever move player  makes, player  can make the other move and win the game.
