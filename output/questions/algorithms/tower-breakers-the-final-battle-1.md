# Tower Breakers - The Final Battle

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.7516985793699815
- **Total Submissions:** 1619
- **Solved Count:** 1217
- **URL:** https://www.hackerrank.com/challenges/tower-breakers-the-final-battle-1

## Problem Statement

Our unsung tower-breaking heroes (players $P_1$ and $P_2$) only have one tower left, and they've decided to break it for a special game commemorating the end of $5$ days of Game Theory! The rules are as follows:

- $P_1$ always moves first, and both players always move optimally.
- Initially there is $1$ tower of height $N$.
- The players move in alternating turns. The moves performed by each player are different:
	1. At each turn, $P_1$ divides the current tower into some number of smaller towers. If the turn starts with a tower of height $H$ and $P_1$ breaks it into $x \ge 2$ smaller towers, the following condition must apply: $H = h_1+h_2+...+h_x$, where $h_i$ denotes the height of the $i^{th}$ new tower.
	2. At each turn, $P_2$ chooses some tower $k$ of the $x$ new towers made by $P_1$ (where $1 \le k \le x$). Then $P_1$ must pay $k^2$ coins to $P_2$. After that, $P_1$ gets another turn with tower $h_k$ and the game continues.
- The game is over when no valid move can be made by $P_1$, meaning that $H = 1$.
- $P_1$'s goal is to pay as few coins as possible, and $P_2$'s goal is to earn as many coins as possible. 

Can you predict the number of coins that $P_2$ will earn?

## Input Format

The first line contains a single integer, $T$, denoting the number of test cases.	
Each of the $T$ subsequent lines contains a single integer, $N$, defining the initial tower height for a test case.

## Output Format

For each test case, print a single integer denoting the number of coins earned by $P_2$ on a new line.

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 10^{18}$

## Sample Input

4
2
7

## Sample Output

4
8

## Explanation

Test Case 0:

Our players make the following moves:

-
-  splits the initial tower into  smaller towers of sizes  and .

-  chooses the first tower and earns  coin.

-
-  splits the tower into  smaller towers of sizes  and .

-  chooses the first tower and earns  coin.

-
-  splits the tower into  smaller towers of size .

-  chooses the second tower and earns  coins.

The total number of coins earned by  is , so we print  on a new line.
