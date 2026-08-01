# Longest Mod Path

- **Domain:** mathematics
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.8627450980392157
- **Total Submissions:** 1428
- **Solved Count:** 1232
- **URL:** https://www.hackerrank.com/challenges/longest-mod-path

## Problem Statement

In the middle of a nightmare, [Maxine](http://life-is-strange.wikia.com/wiki/Maxine_Caulfield) suddenly finds herself in a mysterious room with the following items: 

1. A piece of paper with the word *score* and the integer $0$ written on it.
2. A map of the castle where the room is located.
    - There are $N$ rooms uniquely labeled from $1$ to $N$.  
    - There are $N$ bidirectional corridors connecting pairs of rooms. The value of *score* changes every time she travels up or down a corridor, and this value differs depending on her direction of travel along the corridor. Each corridor can be traveled any number of times in either direction.
    - Every room is reachable from every other room.  
    - Maxine is located in the room labeled $S$.  
    - The exit is located in the room labeled $E$. Once this room is reached, *score* is reduced *modulo* $M$ and Maxine can (but is not required to) exit that level! 

Assume some corridor $i$ (where $1 \le i \le N$) is associated with an integer, $x_i$, and connects rooms $a_i$ and $b_i$. Then:

- Traveling corridor $i$ from room $a_i$ to room $b_i$ *increases score* by $x_i$.
- Traveling corridor $i$ from room $b_i$ to room $a_i$ *decreases score* by $x_i$. 

There are $Q$ levels to Maxine's nightmare castle, and each one has a different set of values for $S$, $E$, and $M$. Given the above information, help Maxine by finding and printing her maximum possible score for each level. Only you can help her wake up from this nightmare!
 
**Note:** Recall that the result of a modulo operation is *always non-negative*.  For example, $(-8) \bmod 5 = 2$.  

## Input Format

The first line contains a single integer, $N$, denoting the number of rooms. 	
Each of the $N$ subsequent lines describes a corridor in the form of three space-separated integers denoting the respective values for $a_i$, $b_i$, and $x_i$.		
The next line contains a single integer, $Q$, denoting the number of queries. 	
Each of the $Q$ subsequent lines describes a level in the form of three space-separated integers denoting its respective $S$, $E$, and $M$ values. 

## Output Format

For each of the $Q$ levels, print the maximum possible score for that level on a new line.

## Constraints

* $1 \le N \le 10^5$  
* $1 \le a_i, b_i \le N$, $a_i \ne b_i$  
* $1 \le x_i \le 10^9$  
* $1 \le Q \le 10^5$  

For each level:

* The room layout is the same
* $1 \le S, E \le N$  
* $1 \le M \le 10^9$  



**Subtask**

* $1 \le N, Q, M \le 300$ for $30\%$ of max score.

## Sample Input

1 3 5
2 3 8
2 1 31
1
1 2 13

## Explanation

The Sample Input represents the following setup:

We want to travel from room  to room  while maximizing the value of score. There are at least two ways to achieve the maximum score value of :

- Travel through corridors  times:

.

- Travel through corridors  times:

, because  is the smallest non-negative integer  such that  divides .
