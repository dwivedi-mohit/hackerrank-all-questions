# Gaming Array 1

- **Domain:** cpp
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.9209367493995196
- **Total Submissions:** 4996
- **Solved Count:** 4601
- **URL:** https://www.hackerrank.com/challenges/three-month-preparation-kit-an-interesting-game-1

## Problem Statement

Andy wants to play a game with his little brother, Bob.  The game starts with an array of distinct integers and the rules are as follows:

- Bob always plays first.   
- In a single move, a player chooses the maximum element in the array.  He removes it and all elements to its right. For example, if the starting array $arr = [2, 3, 5, 4, 1]$, then it becomes $arr' = [2, 3]$ after removing $[5, 4, 1]$.  
- The two players alternate turns. 
- The last player who can make a move wins.  

Andy and Bob play $g$ games. Given the initial array for each game, find and print the name of the winner on a new line. If Andy wins, print `ANDY`; if Bob wins, print `BOB`.

To continue the example above, in the next move Andy will remove $3$.  Bob will then remove $2$ and win because there are no more integers to remove.  

**Function Description**  

Complete the *gamingArray* function in the editor below.  

gamingArray has the following parameter(s):  

- *int arr[n]:* an array of integers   

**Returns**   
- *string:* either `ANDY` or `BOB`  

## Input Format

The first line contains a single integer $g$, the number of games.

Each of the next $g$ pairs of lines is as follows:

- The first line contains a single integer, $n$, the number of elements in $arr$.
- The second line contains $n$ distinct space-separated integers $arr[i]$ where $0 \le i \lt n$.  

## Constraints

* Array $arr$ contains $n$ distinct integers.

For $35\%$ of the maximum score:

* $1 \le g \le 10$  
* $1 \le n \le 1000$  
* $1 \le arr[i] \le 10^5$    
* The sum of $n$ over all games does not exceed $1000$.

For $100\%$ of the maximum score:

* $1 \le g \le 100$  
* $1 \le n \le 10^5$  
* $1 \le a_i \le 10^9$  
* The sum of $n$ over all games does not exceed $10^5$.
