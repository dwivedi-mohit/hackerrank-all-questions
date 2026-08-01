# Stone Piles

- **Domain:** sql
- **Difficulty:** Hard
- **Max Score:** 85
- **Success Ratio:** 0.7159926470588235
- **Total Submissions:** 3264
- **Solved Count:** 2337
- **URL:** https://www.hackerrank.com/challenges/stone-piles

## Problem Statement

There are $N$ piles of stones where the ith pile has $x_i$ stones in it. Alice and Bob play the following game:

1. Alice starts, and they alternate turns.

2. In a turn, a player can choose any one of the piles of stones and divide the stones in it into any number of unequal piles such that no two of the newly created piles have the same number of stones. For example, if there 8 stones in a pile, it can be divided into one of these set of piles: $(1,2,5), (1,3,4), (1,7), (2,6)$ or $(3,5)$. 

3. The player who cannot make a move (because all the remaining piles are indivisible) loses the game.

Given the starting set of piles, who wins the game assuming both players play optimally (that means they will not make a move that causes them to lose the game if some better, winning move exists)?


## Input Format

The first line contains the number of test cases $T$. $T$ test cases follow. The first line for each test case contains $N$, the number of piles initially. The next line contains $N$ space delimited numbers, the number of stones in each of the piles.


## Output Format

Output $T$ lines, one corresponding to each test case containing ``ALICE`` if Alice wins the game and ``BOB`` otherwise.


## Constraints

* $1 <= T <= 50$
* $1 <= N <= 50$  
* $1 <= x_i <= 50$


## Sample Input

1
4
2
1 2
3
1 3 4
1
8

## Sample Output

BOB
BOB
ALICE
BOB

## Explanation

For the first case, the only possible move for Alice is (4) -> (1,3). Now Bob breaks up the pile with 3 stones into (1,2). At this point Alice cannot make any move and has lost.
