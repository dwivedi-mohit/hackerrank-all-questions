# Minimum Health

## Metadata

- **ID:** 1255831
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Problem Solving, Medium, Priority Queue, Heaps
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, heaps, and arrays concepts, ideal for mid-level roles. The problem requires calculating the minimum initial health Charlie needs to defeat the rankth strongest player at each level in a video game.

## Problem Statement

Alex and Charlie are playing a video game with multiple levels. Initially, there are m players in the first level, and n additional levels. Each level introduces one new player. Every player has a strength value.

 

Alex has completed the game by beating the rankth strongest player at each level. Now Charlie wants to do the same. When Charlie beats a player, Charlie's health decreases by that player's strength.

 

What is the minimum initial health Charlie needs to start with in order to beat the rankth strongest player at each level?

 

Example

initial_players = [1, 2]

new_players = [3, 4]

rank = 2

	
- Level 1: Players have strengths [1, 2], and Charlie beats the 2nd strongest (1)
	
- Level 2: Players have strengths [1, 2, 3], and Charlie beats the 2nd strongest (2)
	
- Level 3: Players have strengths [1, 2, 3, 4], and Charlie beats the 2nd strongest (3)

Total health needed = 1 + 2 + 3 = 6

 

Function Description

Complete the function getMinimumHealth in the editor with the following parameter(s):

    int initial_players[m]:  the strength of initial m players of the game

    int new_players[n]:  the strength of the new players that appear one per round after the first level

    int rank: the rank that Charlie needs to win every level

 

Returns

    long: the initial health needed

 

Constraints

	
- 1 ≤ n, m ≤ 105

	
- 1 ≤ rank ≤ m

	
- 1 ≤ initial_players[i], new_players[i] ≤ 109

 

Input Format for Custom Testing

The first line contains an integer m, the size of the array initial_players.

Each of the next m lines contains an integer initial_players[i].

The next line contains an integer n, the size of the array new_players.

Each of the next n lines contains an integer new_players[i].

The last line contains an integer rank.

Sample Case 0

Sample Input 0

STDIN	    FUNCTION
-----	    --------
3      →    the size of initial_players[] m = 3
1      →    initial_players = [1, 1, 3]
1
3
3      →    the size of new_players[] n = 3
2      →    new_players = [2, 2, 4]
2
4
2      →    rank = 2

```

Sample Output 0

8

```

Explanation

For the first level, players are [1, 1, 3], Charlie beats strength 1.

second level, [1, 1, 2, 3], beat strength 2

third level, [1, 1, 2, 2, 3], beat strength 2

fourth level, [1, 1, 2, 2, 3, 4], beat strength 3.

 

Total health needed is = 1 + 2 + 2 + 3 = 8.

Sample Case 1

Sample Input 1

STDIN	    FUNCTION
-----	    --------
3      →    the size of initial_players[] m = 3
1      →    initial_players = [1, 2, 3]
2
3
3      →    the size of new_players[] n = 3
6      →    new_players = [6, 5, 4]
5
4
1      →    rank = 1

```

Sample Output 1

21

```

Explanation

level 1, players are [1, 2, 3], since rank = 1, Charlie beats rank 3

level 2, players are [1, 2, 3, 6]

level 3, [1, 2, 3, 5, 6]

level 4, [1, 2, 3, 4, 5, 6]

 

Total health needed is = 3 + 6 + 6 + 6 = 21.

## Sample Input/Output

## Preview

Alex and Charlie are playing a video game with multiple levels. Initially, the
