# Football Scores

## Metadata

- **ID:** 295396
- **Type:** code
- **Difficulty:** 16.38888888888889
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Data Structures, Medium, Binary Search, Algorithms, Arrays, Problem Solving
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates data structures, binary search, and algorithms concepts, ideal for mid-level roles. The problem requires calculating how many matches team A scored less than or equal to team B's goals for each match.

## Problem Statement

Given two arrays representing the number of goals scored by two football teams in their respective matches, compute for each match of team B the total number of matches where team A scored less than or equal to the number of goals scored by team B in that match.

 

Example

teamA = [1, 2, 3]

teamB = [2, 4]

	
- For teamB[0] = 2 goals: team A has 2 matches with scores ≤ 2 (scores 1 and 2)
	
- For teamB[1] = 4 goals: team A has 3 matches with scores ≤ 4 (scores 1, 2, and 3)

The result is [2, 3].

 

Function Description

Complete the function counts in the editor with the following parameter(s):

    int teamA[n]:  first array of positive integers

    int teamB[m]:  second array of positive integers

 

Returns

    int[m]: the number of matches where team A scored less than or equal to the number of goals scored by team B in that match

 

Constraints

	
- 2 ≤ n, m ≤ 105

	
- 1 ≤ teamA[j] ≤ 109, where 0 ≤ j < n.
	
- 1 ≤ teamB[i] ≤ 109, where 0 ≤ i < m.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer n, the number of elements in teamA.

The next n lines each contain an integer describing teamA[j] where 0 ≤ j < n.

The next line contains an integer m, the number of elements in teamB.

The next m lines each contain an integer describing teamB[i] where 0 ≤ i < m.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input 0

STDIN       Function
-----       --------
4       →   teamA[] size n = 4
1       →   teamA = [1, 4, 2, 4]
4
2
4
2       →   teamB[] size m = 2
3       →   teamB = [3, 5]
5
```

Sample Output 0

2
4
```

Explanation 0

	
- For teamB[0] = 3, we have 2 elements in teamA (1 and 2) that are ≤ teamB[0].
	
- For teamB[1] = 5, we have 4 elements in teamA (1, 4, 2, and 4) that are ≤ teamB[1].

Thus, the function returns the array [2, 4] as the answer.

Sample Case 1

Sample Input 1

STDIN     Function 
-----       -------- 
5       →   teamA[] size n = 5
2       →   teamA = [2, 10, 5, 4, 8]
10
5
4
8
4      →   teamB[] size m = 4
3      →   teamB = [3, 1, 7, 8]
1
7
8
```

Sample Output 1

1
0
3
4
```

Explanation 1

	
- For teamB[0] = 3, we have 1 element in teamA (2) that is ≤ teamB[0].
	
- For teamB[1] = 1, there are no elements in teamA that are ≤ teamB[1].
	
- For teamB[2] = 7, we have 3 elements in teamA (2, 5, and 4) that are ≤ teamB[2].
	
- For teamB[3] = 8, we have 4 elements in teamA (2, 5, 4, 8) that are ≤ teamB[3].

Thus, the function returns the array [1, 0, 3, 4] as the answer.

## Sample Input/Output

## Preview

Given two arrays representing the number of goals scored by two football teams
