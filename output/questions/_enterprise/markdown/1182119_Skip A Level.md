# Skip A Level

## Metadata

- **ID:** 1182119
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Arrays, Greedy Algorithms, Interviewer Guidelines
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates arrays, greedy algorithms, and problem-solving concepts, ideal for junior-level roles. The problem requires determining the maximum points Alex can earn in a game while managing entry fees and allowing for one level skip.

## Problem Statement

Alex plays a game with n levels in a fixed order (Level 1 to Level n).

You are given:

	
- 
k: the number of coins Alex starts with
	
- 
costs[i]: the entry fee required to play level i (1-based level order)

Each time Alex completes a level:

	
- Alex pays that level’s entry fee
	
- Alex earns 1 point

Alex may choose to stop playing at any time, and may skip at most one level total:

	
- Skipping a level means Alex does not pay its cost and does not earn a point for it
	
- All other played levels must still be in increasing order

Find the maximum number of points Alex can earn without the total paid cost exceeding k, using at most one skip.

 

Example

k = 14

n = 5

costs = [2, 4, 1, 8, 6]

 

Completing the game without skipping any level, entry fees = 2 + 4 + 1 + 8 + 6 = 21 > k

Skipping the 4th level, entry fees = 2 + 4 + 1 + 6 = 13 ≤ k, points collected = 4, as levels 1, 2, 3, and 5 were completed.

 

It can be proven that Alex cannot collect more than 4 points. Hence, the answer is 4.

 

Function Description

Complete the function maximumPoints in the editor with the following parameter(s):

    int k: the initial number of coins in Alex's wallet

    int costs[n]:  the costs of each level 

 

Returns

    int: the maximum number of points Alex can collect after skipping at most one level

 

Constraints

	
- 1 ≤ k ≤ 109
	
- 1 ≤ n ≤ 105 
	
- 1 ≤ costs[i] ≤ 109 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, k.

The second line contains an integer, n, the size of the array costs.

Each line i of the n subsequent lines (where 1 ≤ i ≤ n) contains an integer that describes costs[i].

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN    FUNCTION
-----    --------
10    →  k = 10
5     →  n = 5
5     →  costs = [5, 2, 3, 1, 4]
2
3
1
4

```

 

Sample Output

4
```

Explanation

Completing the game without skipping any level, entry fees = 5 + 2 + 3 + 1 + 4 = 15 > k

Skipping the 4th level, entry fees = 5 + 2 + 3 + 4 = 14 > k

Skipping the 1st level, entry fees = 2 + 3 + 1 + 4 = 10 ≤ k, points collected = 4, as levels 2, 3, 4, and 5 were completed.

 

Sample Case 1

Sample Input For Custom Testing

STDIN    FUNCTION
-----    --------
15    →  k = 15
6     →  n = 6
3     →  costs = [3, 2, 6, 4, 6, 1]
2
6
4
6
1

```

Sample Output

4
```

Explanation

Completing the last level without skipping any level, entry fees = 3 + 2 + 6 + 4 + 6 + 1 = 22 > k

Skipping the 3rd level and stopping after the 5th level, entry fees = 3 + 2 + 4 + 6 = 15 ≤ k, points collected = 4, as levels 1, 2, 4, and 5 were completed.

## Sample Input/Output

## Preview

Alex plays a game with n levels in a fixed order (Level 1 to Level n).
