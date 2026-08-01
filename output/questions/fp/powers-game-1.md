# Powers Game

- **Domain:** fp
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.7674418604651163
- **Total Submissions:** 3526
- **Solved Count:** 2706
- **URL:** https://www.hackerrank.com/challenges/powers-game-1

## Problem Statement

After their success in coming up with *Fun Game*, Kyle and Mike invented another game having the following rules:

* The game starts with an $n$-element sequence, $*2^1 * 2^2 * 2^3 * \ldots *2^n$, and is played by two players, $P_1$ and $P_2$. 
* The players move in alternating turns, with $P_1$ always moving first. During each move, the current player chooses one of the asterisks ($*$) in the above sequence and changes it to either a `+` (plus) or a `-` (minus) sign.  
* The game ends when there are no more asterisks ($*$) in the expression. If the evaluated value of the sequence is divisible by $17$, then $P_2$ wins; otherwise, $P_1$ wins.

Given the value of $n$, can you determine the outcome of the game? Print $\texttt{First}$ if $P_1$ will win, or $\texttt{Second}$ if $P_2$ will win. Assume both players always move optimally.

## Input Format

The first line of input contains a single integer $T$, denoting the number of test cases.
Each line $i$ of the $T$ subsequent lines contains an integer, $n$, denoting the maximum exponent in the game's initial sequence.

## Output Format

For each test case, print either of the following predicted outcomes of the game on a new line:

- Print $\texttt{First}$ if $P_1$ will win.
- Print $\texttt{Second}$ if $P_2$ will win.

## Constraints

* $1 \leq T \leq 10^6$
* $1 \leq n \leq 10^6$

## Sample Input

2

## Sample Output

First

## Explanation

In this case, it doesn't matter in which order the asterisks are chosen and altered. There are  different courses of action and, in each one, the final value is not divisible by  (so  always loses and we print  on a new line).

Possible options:

-

-

-

-
