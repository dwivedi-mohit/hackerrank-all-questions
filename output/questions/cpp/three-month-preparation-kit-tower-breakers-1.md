# Tower Breakers

- **Domain:** cpp
- **Difficulty:** Easy
- **Max Score:** 100
- **Success Ratio:** 0.9613331597448249
- **Total Submissions:** 7681
- **Solved Count:** 7384
- **URL:** https://www.hackerrank.com/challenges/three-month-preparation-kit-tower-breakers-1

## Problem Statement

Two players are playing a game of Tower Breakers! Player $1$ always moves first, and both players always play optimally.The rules of the game are as follows:   
  
- Initially there are $n$ towers.
- Each tower is of height $m$.   
- The players move in alternating turns. 
- In each turn, a player can choose a tower of height $x$ and reduce its height to $y$, where $1 \le y \lt x$ and $y$ [evenly divides](https://en.wiktionary.org/wiki/evenly_divisible) $x$.  
- If the current player is unable to make a move, they lose the game.   

Given the values of $n$ and $m$, determine which player will win. If the first player wins, return $1$.  Otherwise, return $2$.  
   
**Example**. 
$n=2$   
$m=6$    

There are $2$ towers, each $6$ units tall.  Player $1$ has a choice of two moves:   
- remove $3$ pieces from a tower to leave $3$ as $6 \text{ modulo } 3=0$   
- remove $5$ pieces to leave $1$   

Let Player $1$ remove $3$. Now the towers are $3$ and $6$ units tall.

Player $2$ matches the move. Now the towers are both $3$ units tall. 

Now Player $1$ has only one move. 

Player $1$ removes $2$ pieces leaving $1$.  Towers are $1$ and $2$ units tall.  
Player $2$ matches again.  Towers are both $1$ unit tall.  

Player $1$ has no move and loses. Return $2$.

**Function Description**  

Complete the *towerBreakers* function in the editor below.   

towerBreakers has the following paramter(s):  

- *int n:* the number of towers  
- *int m:* the height of each tower  

**Returns**  

- *int:* the winner of the game   

## Input Format

The first line contains a single integer $t$, the number of test cases.	 
Each of the next $t$ lines describes a test case in the form of $2$ space-separated integers, $n$ and $m$.  



## Constraints

- $1 \leq t \leq 100 $
- $1 \leq n,m \leq 10^6 $

## Sample Input

STDIN   Function
-----   --------
2       t = 2
2 2     n = 2, m = 2
1 4     n = 1, m = 4

## Sample Output

1

## Explanation

We'll refer to player  as  and player  as

In the first test case,  chooses one of the two towers and reduces it to . Then  reduces the remaining tower to a height of . As both towers now have height ,  cannot make a move so  is the winner.

In the second test case, there is only one tower of height .  can reduce it to a height of either  or .  chooses  as both players always choose optimally. Because  has no possible move,  wins.
