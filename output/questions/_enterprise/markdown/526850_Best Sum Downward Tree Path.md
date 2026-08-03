# Best Sum Downward Tree Path

## Metadata

- **ID:** 526850
- **Type:** code
- **Difficulty:** 9.166666666666668
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Depth First Search, Trees, Algorithms, Problem Solving, Implementation, Medium
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates depth first search, tree traversal, and algorithmic problem-solving concepts, ideal for mid-level roles. The problem requires determining the maximum sum of values along any downward path in a tree structure.

## Problem Statement

For a tree with n nodes rooted at node 0 (nodes numbered from 0 to n-1), where each node i has a value given by values[i], determine the maximum sum of values along any path that starts at a node u and only goes downward in the tree.

 

Consider only paths of the form u1, u2, u3, ..., uk where each node ui is a child of node ui - 1 for 1 < i ≤ k. For example, given the following tree (labeled node number / value):

 

Two possible paths are 0 → 1 → 2 → 3 which has a sum of 5 + 7 + (-10) + 4 = 6 and 1 → 2 → 3 with a sum of 7 + (-10) + 4 = 1.  The highest sum path is 0 → 4 with a sum of 5 + 15 = 20.

 

Function Description 

 

Complete the function bestSumDownwardTreePath in the editor with the following parameter(s):

    int parent[n]: each parent[i] represents the parent node for node i, parent[i] = -1 means node i is the root

    int values[n]:  each values[i] represents the value of node i

 

Return

    int: the largest sum of values along a path down the tree from any node u

 

Constraints

	
- 1 ≤ n <= 105
	
- parent[0] = -1 
	
- 0 ≤ parent[i] ≤ n-1 for 1 ≤ i ≤ n-1
	
- -1000 ≤ values[i] ≤ 1000 
	
- the tree described is valid

 

 DO NOT REMOVE THIS LINE-->

Input Format Format for Custom Testing

Input from stdin will be processed as follows and passed to the function.

 

In the first line, there is a single integer n, that describes the number of nodes in the tree and the size of the parent array.

Each of the next n lines contains a single integer, parent[i].

In the next line, the integer n is repeated and is the size of the values array.

Each of the next n lines contains an integer, values[i].

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input

STDIN   Function
-----   --------
5       parent[] size n = 3
-1      parent = [-1, 0, 1, 2, 0]
0
1
2
0
5       values[] size n = 5
-2      values = [-2, 10, 10, -3, 10]
10
10
-3
10

```

Sample Output

20
```

 

Explanation

The tree looks like the following - (labels are node number/value):

 

The path with the largest sum of values starts at node 1 and finishes at node 2. Its sum is 10+10 = 20. Notice that there is a path with a larger sum, i.e., from node 2 to node 4 with a sum of 28, but it is not a path going only down the tree.

## Sample Input/Output

## Preview

For a tree with n nodes rooted at node 0 (nodes numbered from 0 to n-1), where
