# Kitty and Katty

- **Domain:** sql
- **Difficulty:** Medium
- **Max Score:** 80
- **Success Ratio:** 0.7977425259304454
- **Total Submissions:** 3278
- **Solved Count:** 2615
- **URL:** https://www.hackerrank.com/challenges/kitty-and-katty

## Problem Statement

Kitty and Katty have $N$ plastic blocks. They label the blocks with sequential numbers from $1$ to $N$ and begin playing a game in turns, with Kitty always taking the first turn. The game's rules are as follows:

* For each turn, the player removes $2$ blocks, $A$ and $B$, from the set. They calculate $A-B$, write the result on a new block, and insert the new block into the set. 
* The game ends when only $1$ block is left. The winner is determined by the value written on the final block, $X$:
	- If $X \% 3 = 1$, then Kitty wins.
	- If $X \% 3 = 2$, then Katty wins.
	- If $X \% 3 = 0$, then the player who moved last wins.

Recall that $\%$ is the [Modulo Operation](https://en.wikipedia.org/wiki/Modulo_operation).
	
Given the value of $N$, can you find and print the name of the winner? Assume that both play optimally.

**Note:** The selection order for $A$ and $B$ matters, as sometimes $A-B \neq B-A$. The diagram below shows an initial set of blocks where $N=5$. If $A=2$ and $B=3$, then the newly inserted block is labeled $-1$; alternatively, if $A=3$ and $B=2$, the newly inserted block is labeled $1$.

<img src="https://s3.amazonaws.com/hr-challenge-images/18182/1456840823-a57b686e56-all.png" title="all.png" />


## Input Format

The first line contains a single positive integer, $T$ (the number of test cases or games). 	
The $T$ subsequent lines each contain an integer, $N$ (the number of blocks for that test case).

**Constraints**	

- $1 \leq T \leq 100$<br>
- $1 \leq N \leq 10^5$

## Output Format

For each test case, print the name of the winner (i.e.: either **Kitty** or **Katty**) on a new line.

## Constraints

-

-

## Sample Input

2
3

## Sample Output

Kitty
Katty

## Explanation

Test Case 0:

 so there are two blocks labeled  and . Kitty chooses  and , then inserts a new block with  the label  (the result of ). The game ends, as there is now only  block in the set. The label on the last block, , is , so we calculate . Because  , Kitty wins and we print Kitty on a new line.

Test Case 1:

, so there are three blocks labeled , , and . No matter how Kitty makes the first move, Katty will win. If Kitty chooses  and  on the first move and inserts a block labeled  (the result of ), the set of blocks becomes . Katty then must choose  and  and insert a new block labeled  (the result of ). The game ends, as there is now only  block in the set. The label on the last block, , is , so we calculate . Because  and Katty made the last move, Katty wins and we print Katty on a new line.
