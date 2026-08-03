# Lifting Weights

## Metadata

- **ID:** 797864
- **Type:** code
- **Difficulty:** 8.333333333333334
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Binary Search, Algorithms, Problem Solving, Medium
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, algorithms, and binary search concepts, ideal for mid-level roles. The problem requires determining the maximum weight of plates that can be added to a barbell without exceeding its capacity.

## Problem Statement

An athlete is lifting weights. The barbell has a maximum capacity of maxCapacity. Each barbell plate has a specific weight given by weight[i]. Determine the maximum weight of plates that can be added to the barbell without exceeding maxCapacity.

 

Example

weights = [7, 1, 5, 6, 2]

maxCapacity = 7

 

There are 3 ways to reach the maximum weight that is optimal: {7}, {1, 6}, and {2, 5}. Return 7.

 

Function Description

 

Complete the weightCapacity function in the editor with the following parameters:

    int weights[n]: each element is the weight of a plate

    maxCapacity: the capacity of the barbell

 

Returns

 

    int: the maximum weight that can be added

 

Constraints

	
- 1 ≤ n ≤ 42 
	
- 1 ≤ maxCapacity ≤ 109

	
- 1 ≤ weights[i][ ]≤ 109

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

Locked stub code in the editor reads the following input from stdin and passes it to the function:

 

The first line contains an integer, n, the number of elements in weights.

Each line i of the n subsequent lines contains an integer, weights[i].

The last line contains an integer, maxCapacity.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input 0

STDIN      Function 
-----      --------
3        → weights[] size n = 3
1        → weights[] = [ 1, 3, 5 ]
3
5
7        → maxCapacity = 7

```

Sample Output 0

6
```

Explanation 0

All the possible combinations of weights are {}, {1}, {3}, {5}, {1, 3}, {1, 5}, {3, 5}, and {1, 3, 5}. Choose {1, 5}.

 

Sample Case 1

Sample Input 1

STDIN      Function
-----      --------
4        → weights[] size n = 4
4        → weights[] = [ 4, 8, 5, 9 ]
8
5
9
20       → maxCapacity = 20

```

Sample Output 1

18
```

Explanation

All the possible combinations of weights are: {}, {4}, {8}, {5}, {9}, {4, 8}, {4, 5}, {4, 9}, {8, 5}, {8, 9}, {5, 9}, {4, 8, 5}, {4, 8, 9}, {4, 5, 9}, {8, 5, 9},  {4, 8, 5, 9}.

Choose {4, 5, 9}.

## Sample Input/Output

## Preview

An athlete is lifting weights. The barbell has a maximum capacity of maxCapaci
