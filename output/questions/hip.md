# Hip

- **Domain:** ai
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.3433734939759036
- **Total Submissions:** 166
- **Solved Count:** 57
- **URL:** https://www.hackerrank.com/challenges/hip

## Problem Statement

Hip is a classic board game invented by [Martin Gardner](https://en.wikipedia.org/wiki/Martin_Gardner). It's a 2 player game played on a 9x9 board. Players take turns placing a token on an unoccupied cell. The player who completes any square such that 4 corners are marked by his token <b>loses</b>. The square may be of any size and can be tilted at any angle.

Here are a couple of game states that shows the players lose by completing a square. <br/><br/>

![image alt](https://ferrari.interviewstreet.com/hackerrank/hip.png)<br/><br/>

The function <b> nextMove</b> takes in a character <i> player</i>

and an 9x9 char <i>board</i> as an input and provides 2 integer

positions row and column space separated as output. The board is 0-indexed.



**Example Input**



    b

    r--------

    ---------

    --r------

    ---b--b--

    --r------

    ---------

    ---------

    ---------

    ---------



**Example Output**



    0 1



The board results in the following state



    rb-------

    ---------

    --r------

    ---b--b--

    --r------

    ---------

    ---------

    ---------

    ---------



First player is identified by token **r**, the second player by **b** and an unoccupied cell is identified by **-** (ascii value:45)

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
