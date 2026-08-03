# Optimizing Delivery

## Metadata

- **ID:** 1445175
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Hard, Graphs, Real-World, Shortest Paths
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates graphs, shortest paths, and problem-solving concepts, ideal for senior-level roles. The problem requires calculating the minimum time for a delivery agent to complete multiple deliveries in a city represented as a graph.

## Problem Statement

A food delivery app is implementing a feature allowing delivery agents to handle multiple orders simultaneously. The city's road network is represented as a graph with the following components:

	
- 
connection_nodes junctions (numbered from 0)
	
- 
m bidirectional roads connecting these junctions
	
- Each road between junctions connection_from[i] and connection_to[i] has a travel time of connection_cost[i]

There are k different orders to be delivered, each at a unique location. The delivery agent starts at junction 0, must complete deliveries at all k locations in any order, and then return to junction 0.

 

Calculate the minimum time needed to complete all deliveries and return to the starting point. If it is impossible to complete the deliveries, return -1.

 

Example

Consider connection_nodes = 3, m = 3, connection_from = [0, 1, 0], connection_to = [1, 2, 2], connection_cost = [10, 20, 50] and deliveries = [1, 2]

 

There are three junctions and three roads with associated travel times of 10, 20, and 50. Two orders need to be delivered at locations 1 and 2. The agent can travel along this path: 0 → 1 → 2 → 1 → 0. This gives the minimum total travel time of 10+20+20+10 = 60.

 

Function Description 

Complete the function getMinimumTime in the editor with the following parameter(s):

    int connection_nodes: the number of junctions

    int connection_from[m]: the first node of each connection

    int connection_to[m]: the second node of each connection

    int connection_weight[m]: the cost of each connection

    int deliveries[k]: the delivery locations

 

Returns

    long int: the minimum time required to complete all the deliveries and return to 0, or if it is not possible, return -1

 

Constraints

	
- 1 ≤ connection_nodes ≤ 105

	
- 1 ≤ m ≤ min(105, n*(n-1)/2)
	
- 1 ≤ k ≤ 10
	
- 1 ≤ connection_weight[i] ≤ 109

	
- 0 ≤ connection_from[i],connection_to[i],deliveries[i] ﹤n

	
- There are no multiple edges or self-loops.

 

Input Format for Custom Testing

The first line contains two integers, connection_nodes, and m, the number of junctions and the number of connections.

Each of the next m lines contains three integers connection_from[i], connection_to[i], and connection_weight[i].

The next line contains an integer k, the number of delivery locations.

Each of the next k lines contains an integer, deliveries[i].

Sample Case 0

Sample Input 0

STDIN          FUNCTION
-----          --------
5 6       →    connection_nodes = 5, m = 6
0 1 10    →    connection_from[] = [0, 0, 4, 4, 1, 1], connection_to[] = [1, 4, 1, 3, 2, 3], connection_weight[] = [10, 3, 5, 4, 2, 4]
0 4 3
4 1 5
4 3 4
1 2 2
1 3 4
2        →     k = 2
1        →     deliveries = [1, 3]
3
```

Sample Output 0

19

```

Explanation

Two orders need to be delivered at locations 1 and 3. The agent can travel along this path: 0 → 4 → 3 → 1 → 4 → 0. This gives the minimum total travel time of 3 + 4 + 4 + 5 + 3 = 19. 

Sample Case 1

Sample Input 1

STDIN          FUNCTION
-----          --------
3 3      →     connection_nodes = 3, m = 3
0 1 10   →     connection_from[] = [0, 1, 2], connection_to[] = [1, 2, 0], connection_weight[] = [10, 30, 10]
1 2 30
2 0 10
2        →     k = 2
1        →     deliveries = [1, 2]
2

```

Sample Output 1

40

```

Explanation

Two orders need to be delivered at locations 1 and 2. The agent can travel along this path: 0 → 1 → 0 → 2 → 0. This gives the minimum total travel time of 10 + 10 + 10 + 10 = 40.

## Sample Input/Output

## Preview

A food delivery app is implementing a feature allowing delivery agents to hand
