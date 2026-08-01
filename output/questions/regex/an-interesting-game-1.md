# Gaming Array

- **Domain:** regex
- **Difficulty:** Medium
- **Max Score:** 35
- **Success Ratio:** 0.785288522511097
- **Total Submissions:** 15770
- **Solved Count:** 12384
- **URL:** https://www.hackerrank.com/challenges/an-interesting-game-1

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

## Sample Input

2
5
5 2 6 3 4
2
3 1

## Sample Output

ANDY
BOB

## Explanation

Andy and Bob play the following two games:

- Initially, the array looks like this:

In the first move, Bob removes  and all the elements to its right, resulting in :

In the second move, Andy removes  and all the elements to its right, resulting in :

At this point, the array is empty and Bob cannot make any more moves. This means Andy wins, so we print ANDY on a new line.

- In the first move, Bob removes  and all the elements to its right, resulting in . As there are no elements left in the array for Andy to make a move, Bob wins and we print BOB on a new line.
