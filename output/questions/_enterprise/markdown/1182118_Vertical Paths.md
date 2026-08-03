# Vertical Paths

## Metadata

- **ID:** 1182118
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Hard, Trees, Interviewer Guidelines, Depth First Search
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates tree traversal, depth-first search, and path cost calculation concepts, ideal for senior-level roles. The problem requires counting vertical paths in a tree where the path cost modulo k equals zero.

## Problem Statement

You are given a tree with edge_nodes nodes numbered 1 to edge_nodes, each with an assigned value. The cost of a path is defined as the sum of all values (cost[i]) assigned to nodes in the path. The root of the tree is node number 1.

 

Cost of path example

 

 

The cost of the path 6 -> 5 -> 3 -> 1 in the above tree is 42 + 31 + 20 + 10 = 103.

 

A Vertical Path in a tree is a path going up toward the root. It is not necessary for the path to end at the root.

 

Given a tree and an integer k, find the number of vertical paths such that (cost of the path) % k = 0, where % represents the modulo operation (remainder after division).

 

Example

cost = [1, 1, 1, 1]

edge_nodes = 4

edge_from = [1, 1, 4]

edge_to = [2, 4, 3]

k = 2

 

 

 

There are 8 vertical paths:

	
- Path: 1 (cost = 1)
	
- Path: 2 (cost = 1)
	
- Path: 4 (cost = 1)
	
- Path: 2→1 (cost = 1+1 = 2)
	
- Path: 4→1 (cost = 1+1 = 2)
	
- Path: 3 (cost = 1)
	
- Path: 3→4 (cost = 1 + 1 = 2)
	
- Path: 3→4→1 (cost = 1 + 1 + 1 = 3)

Of these, only (2→1), (4→1), and (3→4) have (cost of path) % k = 0.

Therefore, the answer is 3.

 

Function Description

Complete the function countVerticalPaths in the editor with the following parameters:

    int cost[edge_nodes]: the array representing the value of each node.

    int edge_nodes: number of nodes in the tree.

    int edge_from[edge_nodes - 1]: the ith integer denotes one endpoint of the ith edge.

    int edge_to[edge_nodes - 1]: the ith integer denotes the other endpoint of the ith edge

    int k: the modulo divisor

 

Returns

    int: the number of vertical paths with (cost of the path) % k = 0

    

Note: The tests are generated in such a way that the returned value fits in int32

 

Constraints

	
- 1 ≤ edge_nodes ≤ 2*105

	
- 0 ≤ cost[i]  ≤ 108

	
- 1 ≤ k ≤ 105

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains one integer, edge_nodes, denoting the size of the cost array.

The next n lines each contain an element of the cost array.

The next line contains two integers, edge_nodes and edge_nodes - 1,  denoting the number of nodes and the number of edges, respectively.

Each line i of the edge_nodes - 1 subsequent lines (where 0 ≤ i < edge_nodes - 1) contains two integers, edge_from[i] and edge_to[i].

The next line contains an integer k.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN       Function
-----       --------
5           size of cost[] = 5
1           cost = [1, 2, 2, 1, 2]   
2
2
1
2         
5 4         edge_nodes = 5, edge_nodes - 1 = 4
2 3         edge_from = [2, 2, 1, 2]
2 1         edge_to = [3, 1, 4, 5]
1 4
2 5       
2           k = 2

```

Sample Output

6
```

Explanation

There are 6 vertical paths that meet the condition:

1. 2 (cost = 2)

2. 5 -> 2 (cost = 2 + 2 = 4)

3. 4 -> 1 (cost = 1 + 1 = 2)

4. 3 (cost = 2)

5. 3 -> 2 (cost = 2 + 2 = 4)

6. 5 (cost = 2)

 

 

These path costs are evenly divisible by 2.

 

Sample Case 1

Sample Input For Custom Testing

STDIN       Function
-----       --------
5           size of cost[] = 5
2           cost = [2, 3, 0, 3, 0]   
3
0
3
0         
5 4         edge_nodes = 5, edge_nodes - 1 = 4
2 3         edge_from = [2, 3, 3, 3]
3 1         edge_to = [3, 1, 4, 5]
3 4
3 5       
3           k = 3

```

Sample Output

7
```

Explanation

There are 7 vertical paths that meet the condition:

1. 4 (cost = 3)

2. 4 -> 3 (cost = 3 + 0 = 3)

3. 2 (cost = 3)

4. 2 -> 3 (cost = 3 + 0 = 3)

5. 5 (cost = 0)

6. 3 (cost = 0)

7. 5 -> 3 (cost = 0 + 0 = 0)

 

 

These path costs are evenly divisible by 3.

## Sample Input/Output

## Preview

You are given a tree with edge_nodes nodes numbered 1 to edge_nodes, each with
