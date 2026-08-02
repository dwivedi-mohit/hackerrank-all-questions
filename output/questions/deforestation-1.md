# Deforestation

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.729251012145749
- **Total Submissions:** 1976
- **Solved Count:** 1441
- **URL:** https://www.hackerrank.com/challenges/deforestation-1

## Problem Statement

Alice and Bob are playing a game with a rooted tree. The tree has $N$ vertices and the first node, $1$, is always the root. Here are the basic rules:

1. They move in alternating turns, and both players always move optimally.
2. During each move, a player removes an edge from the tree, disconnecting one of its leaves or branches. The leaf or branch that was disconnected from the rooted tree is removed from the game. 
3. The first player to be unable to make a move loses the game.
4. Alice always makes the first move. 

For example, the diagram below shows a tree of size $n = 7$, where the root is node $1$:
![tree-initial.png](https://s3.amazonaws.com/hr-challenge-images/19585/1463178479-7f173f4eeb-tree-initial.png)

Now, if a player removes the edge between $1$ and $4$, then nodes $4$ and $7$ become disconnected from the root and are removed from the game:

![tree-removed.png](https://s3.amazonaws.com/hr-challenge-images/19585/1463178803-d8fdcb21e9-tree-removed.png)

Given the structure of the tree, determine and print the winner of the game. If Alice wins, print $\texttt{Alice}$; otherwise print $\texttt{Bob}$.

## Input Format

The first line contains a single integer, $T$, denoting the number of test cases.	
For each test case, the first line contains an integer, $N$, denoting the number of nodes in the tree. 		
Each of the $N-1$ subsequent lines contains $2$ space-separated integers, $u$ and $v$, defining an edge connecting nodes $u$ and $v$.

## Output Format

For each test case, print the name of the winner (i.e., $\texttt{Alice}$ or $\texttt{Bob}$) on a new line.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 500$
- $1 \leq u, v \leq N$

## Sample Input

5
1 2
3 1
3 4
4 5

## Sample Output

Alice

## Explanation

Test Case 0:

Alice removes the edge connecting node  to node , effectively trimming nodes  and  from the tree. Now the only remaining edges are  and . Because Bob can't remove both of them, Alice will make the last possible move. Because the last player to move wins, we print  on a new line.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
