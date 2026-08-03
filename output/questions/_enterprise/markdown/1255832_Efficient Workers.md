# Efficient Workers

## Metadata

- **ID:** 1255832
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Sorting, Prefix Sum, Medium, Arrays
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates sorting, prefix sums, and problem-solving concepts, ideal for mid-level roles. The problem requires determining which worker to exclude to minimize the total pairing cost based on efficiency ratings.

## Problem Statement

A group of workers with different efficiency ratings needs to be paired to complete a task. When workers are paired, the cost is the absolute difference between their efficiency ratings.

 

The total cost of the task is the sum of all pair costs. Since there is an odd number of workers, one worker will not be paired. Your goal is to select which worker to exclude in order to minimize the total cost.

 

Example

efficiency = [4, 2, 8, 1, 9]

 

If worker 0 (with efficiency 4) is excluded, and we form the pairs (1, 3) and (2, 4) with efficiencies [(2, 1), (8, 9)], the cost is: |2 - 1| + |8 - 9| = 1 + 1 = 2.

 

This is the minimum possible cost, so return 2.

 

Function Description

Complete the function findMinCost in the editor with the following parameter(s):

    int efficiency[n]: the efficiency of each worker

 

Returns

   int: the minimum possible cost

 

Constraints

	
- 3 ≤ n < 105

	
- 1 ≤ efficiency[i] ≤ 109

	
- 
n is odd.

 

Input Format for Custom Testing

The first line contains an integer n, the size of the array efficiency.

Each of the next n lines contains an integer efficiency[i].

Sample Case 0

Sample Input 0

STDIN	    FUNCTION
-----	    --------
5      →    n = 5
4      →    efficiency = [4, 1, 2, 16, 8]
1
2
16
8

```

Sample Output 0

5	

```

Explanation

Exclude worker 3 and make the pairs (1, 2) and (0, 4). The cost of the task is |1 - 2| + |4 - 8| = 5.

Sample Case 1

Sample Input 1

STDIN        FUNCTION
-----        --------
7      →    n = 7
2      →    efficiency=  = [2, 13, 12, 9, 6, 3, 2]
16
12
9
6
3
2

```

Sample Output 1

4

```

Explanation

Exclude worker 3 and make the pairs (0, 6), (1, 2), and (4, 5). The cost is |2 - 2| + |13 - 12| + |6 - 3| = 4.

## Sample Input/Output

## Preview

A group of workers with different efficiency ratings needs to be paired to com
