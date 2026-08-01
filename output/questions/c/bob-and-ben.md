# Bob and Ben

- **Domain:** c
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.8320571720265442
- **Total Submissions:** 1959
- **Solved Count:** 1630
- **URL:** https://www.hackerrank.com/challenges/bob-and-ben

## Problem Statement

Bob and Ben are playing a game with forests! The game's rules are as follows:

* The game starts with a [forest](http://mathworld.wolfram.com/Forest.html) of $n$ trees.
* Bob always moves first and they take alternating turns. The first player with no available move loses the game.
- During each move, the player removes one node. If the node is *not a leaf*, then the whole tree vanishes; otherwise, the rest of the tree remains in the forest. We define a leaf to be a node with exactly $1$ connected edge.
- Both players play optimally, meaning they will not make a move that causes them to lose the game if some better, winning move exists.

We define each tree $i$ in the $n$-tree forest as follows:

- Tree $i$ is defined by two integers, $m_{i}$ (the number of nodes in the tree) and $k_{i}$ (a constant). 
- Its nodes are numbered sequentially from $1$ to $m_{i}$.
- Its edges are numbered sequentially from $1$ to $m_{i} - 1$, and each edge $j$ connects node $j+1$ to node $\lfloor max (1, \frac{j}{k_i} )\rfloor$.

Given the values of $m_i$ and $k_i$ for each tree in the forest, can you determine who will win the game?


## Input Format

The first line contains an integer, $g$, denoting the number of games. The subsequent lines describe each game in the following format:

1. The first line contains an integer, $n$, denoting the number of trees in the forest.		
2. Each of the $n$ subsequent lines contains two space-separated integers describing the respective values of $m_i$ and $k_i$ for tree $i$. 


## Output Format

For each game, print the name of the winner on a new line (i.e., ``BOB`` or ``BEN``).

## Constraints

* $ 1 \le g \le 100$
* $ 1 \le n \le 10^6$
* $ 1 \le m_i \le 10^9$
* $ 2 \le k_i \le 100$
* The sum of $n$ over all games is at most $10^6$.

**Subtasks**

For $\text{50%}$ of the maximum score:

* The sum of $n$ over all games is at most $10^3$.
* $ 1 \le m_i \le 10^3$

For $\text{25%}$ of the maximum score:

* $ 1 \le  n, m_i, g \le 10$


## Sample Input

2
1 2
1 3
1
3 2

## Sample Output

BEN
BOB

## Explanation

Bob and Ben play the following two games:

- The forest consists of  trees containing one node each, and each tree has no edges as  and  are both  (so both trees have  edges). The sequence of moves is as follows:

We then print the name of the winner, BEN, on a new line.

- The forest consists of  tree containing three nodes. We find the  edges like so:

- Edge  connects node  to node .

- Edge  connects node  to node .

The game then plays out as follows:

We then print the name of the winner, BOB, on a new line.
