# Tastes Like Winning

- **Domain:** c
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.6188436830835118
- **Total Submissions:** 2335
- **Solved Count:** 1445
- **URL:** https://www.hackerrank.com/challenges/taste-of-win

## Problem Statement

Stephanie just learned about a game called *Nim* in which there are two players and $n$ piles of stones. During each turn, a player must choose any non-empty pile and take as many stones as they want. The first player who cannot complete their turn (i.e., because all piles are empty) loses.  

Stephanie knows that, for each start position in this game, it's possible to know which player will win (i.e., the first or second player) if both players play optimally. Now she wants to know the number of different games that exist that satisfy all of the following conditions:

- The game starts with $n$ non-empty piles and each pile contains less than $2^m$ stones.
- All the piles contain pairwise different numbers of stones.
- The first player wins if that player moves optimally.

Help Stephanie by finding and printing the number of such games satisfying all the above criteria, modulo $10^9 + 7$.

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ and $m$.

## Output Format

Print the number of such games, modulo $10^9 + 7$.

## Constraints

* $1 \leq n, m \leq 10^7$  

## Sample Input

2 2

## Sample Output

6

## Explanation

We want to know the number of games with  piles where each pile contains  stones. There are six such possible games with the following distributions of stones: . Thus, we print the result of  as our answer.
