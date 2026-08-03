# Connected Sum

## Metadata

- **ID:** 932081
- **Type:** code
- **Difficulty:** 14.722222222222221
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Disjoint Sets, Data Structures, Algorithms, Hard, Problem Solving
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates graph traversal, connected components, and mathematical calculations, ideal for senior-level roles. The problem requires calculating the sum of the ceilings of the square roots of the sizes of connected components in a graph of radioactive rods.

## Problem Statement

Find the cost of retrieving n radioactive rods.

Given a set of nodes and a list of connected pairs, determine the order (number of nodes) in each connected component in the graph. For each component, calculate the ceiling of the square root of its order, and return the sum of these values across all connected components.

 

Example

graph_nodes = 10

graph_from = [1, 1, 2, 3, 7]

graph_to = [2, 3, 4, 5, 8]

There are graph_edges = 5 edges to consider. There are 2 isolated sets with more than one node, {1, 2, 3, 4, 5} and {7, 8}.  The ceilings of their square roots are 51/2 ≅ 2.236 and ceil(2.236) = 3, 21/2 ≅ 1.414 and ceil(1.414) = 2.  The other three isolated nodes are separate and the square root of their orders is 11/2 = 1 respectively.   The sum is 3 + 2 + (3 * 1) = 8.

 

Function Description 

Complete the function connectedSum in the editor below.

 

connectedSum has the following parameter(s):

    int graph_nodes: the number of nodes

    int graph_from[graph_edges]:  an array of integers that represent one end of an edge

    int graph_to[graph_edges]:  an array of integers that represent the other end of an edge

 

Returns:    

    int: an integer that denotes the sum of the values calculated

 

Constraints

	
- 2 ≤ graph_nodes ≤ 105
	
- 1 ≤ graph_edges ≤ 105
	
- 1 ≤ graph_from[i], graph_to[i] ≤ n
	
- graph_from[i] ≠ graph_to[i]

 

 DO NOT REMOVE THIS LINE-->

Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function.

 

The first line contains two space-separated integers, graph_nodes, the number of nodes, and graph_edges, the number of edges.

Each of the next m lines contains two space-separated integers, graph_from[i] and graph_to[i], two nodes connected by an edge.

Sample Case 0

Sample Input 0

STDIN      Function 
-----      --------- 
4 2   →    graph_nodes = 4 nodes, graph_edges = 2 edges
1 2   →    graph_from[] = [1, 1], graph_to[] = [2, 4]
1 4

```

Sample Output 0

3
```

 

Explanation 0

 

The diagram below shows the components:

-->

 

The values to sum are:

	
- Set {1, 2, 4}: c = ceil(sqrt(3)) = 2

	
- Set {3}: c = ceil(sqrt(1)) = 1

 

2 + 1 = 3

 

Sample Case 1

Sample Input 1

STDIN      Function
-----      ---------
8 4   →    graph_nodes = 8 nodes, graph_edges = 4 edges
8 1   →    graph_from[] = [8, 5, 7, 8], graph_to[] = [1, 8, 3, 6]
5 8
7 3
8 6

```

 

Sample Output 1

6
```

 

Explanation 1

 

The diagram below shows the components:

-->

 

The values to sum for each group are:

	
- Set {2}: c = ceil(sqrt(1)) = 1

	
- Set {4}: c = ceil(sqrt(1)) = 1

	
- Set {1, 5, 6, 8}: c = ceil(sqrt(4)) = 2

	
- Set {3, 7}: c = ceil(sqrt(2)) = 2

 

1 + 1 + 2 + 2 = 6

## Sample Input/Output

## Preview

Find the cost of retrieving n radioactive rods.
