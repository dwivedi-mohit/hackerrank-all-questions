# Tic tac toe

- **Domain:** data-structures
- **Difficulty:** Advanced
- **Max Score:** 10
- **Success Ratio:** 0.37550845643331193
- **Total Submissions:** 4671
- **Solved Count:** 1754
- **URL:** https://www.hackerrank.com/challenges/tic-tac-toe

## Problem Statement

Tic-tac-toe is a pencil-and-paper game for two players, X (ascii value 88) and O (ascii value 79), who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal row wins the game. Empty space is represented by
_ (ascii value 95), and the <b>X</b> player goes first.

Here is an example game won by the first player, X:

![picture alt](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Tic-tac-toe-game-1.svg/500px-Tic-tac-toe-game-1.svg.png "Title is optional")

The function <b>nextMove</b> takes in a char <i>player</i>, and the 3x3 <i>board</i> as an array. Complete the function to print 2 space separated integers *r* and *c* which denote the row and column that will be marked in your next move. The top left position is denoted by (0,0).

__How does it work?__ <br />
Your code is run alternately with the opponent bot for every move.

__Example input:__

    X  
    ___  
    ___  
    _XO  

__Example output:__  

    1 0 

__Explanation:__  
The board results in the following state after the above move   

    ___  
    X__  
    _XO  


## Explanation

The board results in the following state after the above move

___
X__
_XO
