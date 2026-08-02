# Misère Nim

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.8241346050798414
- **Total Submissions:** 9331
- **Solved Count:** 7690
- **URL:** https://www.hackerrank.com/challenges/misere-nim-1

## Problem Statement

Two people are playing game of [Misère](https://en.wikipedia.org/wiki/Misère) Nim. The basic rules for this game are as follows:

- The game starts with $n$ piles of stones indexed from $0$ to $n-1$. Each pile $i$ (where $0 \le i \lt n$) has $s_i$ stones.
- The players move in alternating turns. During each move, the current player must  remove one or more stones from a single pile. 
- The player who removes the last stone *loses* the game.

Given the value of $n$ and the number of stones in each pile, determine whether the person who wins the game is the *first* or *second* person to move. If the first player to move wins, print `First` on a new line; otherwise, print `Second`. Assume both players move optimally.  

**Example**   
$s = [1, 1, 1]$  

In this case, player 1 picks a pile, player 2 picks a pile and player 1 has to choose the last pile.  Player 2 wins so return `Second`.  

$s = [1, 2, 2]$  

There is no permutation of optimal moves where player 2 wins.  For example, player 1 chooses the first pile.  If player 2 chooses 1 from another pile, player 1 will choose the pile with 2 left.  If player 2 chooses a pile of 2, player 1 chooses 1 from the remaining pile leaving the last stone for player 2. Return `First`.  

**Function Description**  

Complete the *misereNim* function in the editor below.  

*misereNim* has the following parameters:  

- *int s[n]:* the number of stones in each pile   

**Returns**   

- *string:* either `First` or `Second`


## Input Format

The first line contains an integer, $T$, the number of test cases.		
Each test case is described over two lines:

1. An integer, $n$, the number of piles.
2. $n$ space-separated integers, $s[i]$, that describe the number of stones at pile $i$.

## Output Format

 


## Constraints

- $1 \le T \le 100$
- $1 \le n \le 100$
- $1 \le s[i] \le 10^9$

## Sample Input

STDIN   Function
-----   --------
2       T = 2
2       s[] size n = 2
1 1     s = [1, 1]
3       s[] size n = 3
2 1 3   s = [2, 1, 3]

## Sample Output

First
Second

## Explanation

In the first testcase, the first player removes 1 stone from the first pile and then the second player has no moves other than removing the only stone in the second pile. So first wins.

In the second testcase, the series of moves can be depicted as:

In every possible move of first player we see that the last stone is picked by him, so second player wins.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
