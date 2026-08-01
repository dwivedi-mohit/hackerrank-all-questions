# Huarongdao

- **Domain:** cpp
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.7471400394477318
- **Total Submissions:** 2535
- **Solved Count:** 1894
- **URL:** https://www.hackerrank.com/challenges/huarongdao

## Problem Statement




Huarongdao is a well-known game in China. The purpose of this game is to move the Cao Cao block out of the board. 

Acme is interested in this game, and he invents a similar game. There is a N\*M board. Some blocks in this board are movable, while some are fixed. There is only one empty position. In one step, you can move a block to the empty position, and it will take you one second. The purpose of this game is to move the Cao Cao block to a given position. Acme wants to finish the game as fast as possible. 

But he finds it hard, so he cheats sometimes. When he cheats, he spends K seconds to pick a block and put it in an empty position. However, he is not allowed to pick the Cao Cao block out of the board .

**Note** 

1. Immovable blocks cannot be moved while cheating. 
2. A block can be moved only in the directions UP, DOWN, LEFT or RIGHT. 


## Input Format

The first line contains four integers N, M, K, Q separated by a single space.  N lines follow.  
Each line contains M integers 0 or 1 separated by a single space. If the j<sub>th</sub> integer is 1, then the block in i<sub>th</sub> row and j<sub>th</sub> column is movable. If the j<sub>th</sub> integer is 0 then the block in i<sub>th</sub> row and j<sub>th</sub> column is fixed.
Then Q lines follows, each line contains six integers EX<sub>i</sub>, EY<sub>i</sub>, SX<sub>i</sub>, SY<sub>i</sub>, TX<sub>i</sub>, TY<sub>i</sub> separated by a single space. The i<sub>th</sub> query is the Cao Cao block is in row SX<sub>i</sub> column SY<sub>i</sub>, the exit is in TX<sub>i</sub>, TY<sub>i</sub>, and the empty position is in row EX<sub>i</sub> column EY<sub>i</sub>. It is guaranteed that the blocks in these positions are movable. Find the minimum seconds Acme needs to finish the game. If it is impossible to finish the game, you should answer -1.


## Output Format

You should output Q lines, i-th line contains an integer which is the answer to i-th query.


## Constraints

N,M &le; 200  
1 &le; Q &le; 250  
10 &le; K&le; 15  
1 &le; EX<sub>i</sub>,  SX<sub>i</sub>,  TX<sub>i</sub>&le; N  
1 &le; EY<sub>i</sub>, SY<sub>i</sub>,TY<sub>i</sub> &le; M


## Sample Input

5 5 12 1
1 1 1 1 1
1 1 1 1 1
0 1 1 1 1
1 1 1 1 1
0 1 0 1 1
1 5 4 3 4 1

## Explanation

Move the block in (1, 4) to (1, 5);

Move the block in (1, 3) to (1, 4);

Move the block in (1, 2) to (1, 3);

Move the block in (2, 2) to (1, 2);

Move the block in (3, 2) to (2, 2);

Move the block in (4, 2) to (3, 2);

Move the block in (4, 3) to (4, 2);

Move the block in (4, 1) to (4, 3) by cheating;

Move the block in (4, 2) to (4, 1).

So, 1 + 1 + 1 + 1 + 1 + 1 + 1 + 12 + 1 = 20.
