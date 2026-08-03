# Shared Interest

## Metadata

- **ID:** 320807
- **Type:** code
- **Difficulty:** 9.444444444444445
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Graphs, Data Structures, Disjoint Sets, Hard, Algorithms, Depth First Search, Problem Solving
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates graphs, algorithms, and problem-solving concepts, ideal for senior-level roles. The problem requires finding the maximum product of node pairs in a graph representing friends based on shared interests.

## Problem Statement

Find the maximal product of two friends that share a maximum number of interests.

Given a graph representing friends with various interests, identify which pairs of friends share the highest number of common interests. Out of these pairs, calculate the maximum product.

 

The graph consists of nodes numbered consecutively from 1 to friends_nodes. Friendships, represented as edges in the graph, are based on shared interests, denoted as weights. Friends connected by the same interest form a node pair. For the node pairs with the maximal shared interests, multiply the node numbers and return the highest product.

 

Example

friends_nodes = 4

friends_edges = 5

friends_from = [1, 1, 2, 2, 2]

friends_to = [2, 2, 3, 3, 4]

friends_weight = [2, 3, 1, 3, 4]

From  To    Weight
1     2     2
1     2     3
2     3     1
2     3     3
2     4     4

```

 

The graph shows the following connections:

  Weight
(Interest)    Connectons
    1            2,3
    2            1,2
    3            1,2,3
    4            2,4

```

 

	
- Node pair (2,4) shares only 1 interest (4), and node pair (1,3) shares 1 interest (3).
	
- Node pair (1,2) shares 2 interests (2 and 3), and node pair (2, 3) shares also 2 interests (1 and 3) . So, the maximum number of shared interests is 2.
	
- Multiply the node numbers of the pairs with the maximum number of connections: 1 × 2 = 2 and 2 × 3 = 6.
	
- The maximal product is 6.

 

Function Description 

Complete the function maxShared in the editor with the following parameter(s):

    int friends_nodes:  number of nodes

    int friends_from[friends_edges]:  the first part of node pairs

    int friends_to[friends_edges]: the other part of node pairs

    int friends_weight[friends_edges]:  the interests of node pairs

 

Returns

    int: maximum integer product of all node pairs sharing the most interests

   
- There are nodes friends numbered from 1 to nodes.
   
- There are edges pairs of friends, where each (xi, yi) pair of friends is connected by a shared integer interest described by weighti.
   
- Any two friends, xi and yi, can be connected by zero or more interests because if friends xi and yi share interest ti and friends yi and zi also share interest ti, then xi and zi are also said to share interest ti.

 

Find the maximal product of xi and yi for any directly or indirectly connected (xi, yi) pair of friends such that xi and yi share the maximal number of interests with each other.

 

Complete the maxTokens function in the editor. It has four parameters:

 

   
      
         Name
         Type
         Description
      
      
         nodes
         integer
         The number of friends.
      
      
         from
         integer array
         Each from[i] (where 0 &le; i < edges) denotes the first friend in pair (from[i], to[i]).
      
      
         to
         integer array
         Each to[i] (where 0 &le; i < edges) denotes the second friend in pair (from[i], to[i]).
      
      
         weight
         integer array
         Each weight[i] (where 0 &le; i < edges) denotes the ID number of a interest shared by both from[i] and to[i].
      
      
         Note: edges is the number of pairs of friends that directly share a interest.
      
   

   
- An integer, nodes, denoting the number of friends. 
   
- An array of integers, from, where each from[i] (where 0 &le; i < edges) denotes the first friend in pair (from[i], to[i]).
   
- An array of integers, to, ach to[i] (where 0 &le; i < edges) denotes the second friend in pair (from[i], to[i]).
   
- An array of integers,  weight, where each weight[i] denotes the ID number of a interest shared by both from[i] and to[i].

 

 

The function must return an integer denoting the maximal product of xi and yi such that xi and yi are a pair of friends that share the maximal number of interests with each other.

 

Input Format

The first line contains two space-separated integers describing the respective values of nodes and edges.

Each line i of the edges subsequent lines (where 0 &le; i < edges) contains three space-separated integers describing the respective values of fromi, toi, and weighti.

-->

 

Constraints

	
- 2 ≤ friends_nodes ≤ 100
	
- 1 ≤ friends_edges ≤ min(200, (friends_nodes × (friends_nodes − 1)) / 2)
	
- 1 ≤ friends_weight[i] ≤ 100
	
- 1 ≤ friends_from[i], friends_to[i] ≤ friends_nodes
	
- 1≤ friends_weight[i] ≤ friends_edges
	
- friends_from[i] ≠ friends_to[i]
	
- Each pair of friends can be connected by zero or more interests.

 

 DO NOT REMOVE THIS LINE-->

Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function.

The first line contains two space-separated integers, friends_nodes and friends_edges.

Each of the next friends_edges lines contains three space-separated integers, friends_from[i], friends_to[i] and friends_weight[i] where 0 ≤ i < friends_edges.

Sample Case 0

 

Sample Input 0

STDIN     Function 
-----     -------- 
4 5     →  friends_nodes = 4  friends_edges = 5
1 2 1   →  friends_from = [1,1,2,2,2]  friends_to = [2,2,3,3,4]  friends_weight = [1,2,1,3,3] 
1 2 2
2 3 1
2 3 3
2 4 3

```

 

Sample Output 0

6
```

 

Explanation 0

	
		
			Each pair of friends_nodes = 4 friends is connected by the following interests:

			 
			
				
- Pair (1, 2) shares 2 interests (i.e., interests 1 and 2)
				
- Pair (1, 3) shares 1 interest (i.e., interest 1)
				
- Pair (1, 4) shares 0 interests
				
- Pair (2, 3) shares 2 interests (i.e., interests 1 and 3)
				
- Pair (2, 4) shares 1 interest (i.e., interest 3)
				
- Pair (3, 4) shares 1 interest (i.e., interest 3)
			
			
			
			
			

			The pairs connected by the maximal number of interests are (1, 2) and (2, 3). Their products are 1 × 2 = 2 and 2 × 3 = 6. The result is the larger of these values, which is 6.

## Sample Input/Output

## Preview

Find the maximal product of two friends that share a maximum number of interes
