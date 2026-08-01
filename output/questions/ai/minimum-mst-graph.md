# Minimum MST Graph

- **Domain:** ai
- **Difficulty:** Expert
- **Max Score:** 80
- **Success Ratio:** 0.7603252032520326
- **Total Submissions:** 3075
- **Solved Count:** 2338
- **URL:** https://www.hackerrank.com/challenges/minimum-mst-graph

## Problem Statement

Allison loves graph theory and just started learning about [Minimum Spanning Trees(MST)](https://en.wikipedia.org/wiki/Minimum_spanning_tree). She has three integers, $n$, $m$, and $s$, and uses them to construct a graph with the following properties:

* The graph has $n$ nodes and $m$ undirected edges where *each edge has a positive integer length*.
* No edge may directly connect a node to itself, and each pair of nodes can only be directly connected by *at most* one edge.
* The graph is *connected*, meaning each node is reachable from any other node.
* The *value* of the minimum spanning tree is $s$. Value of the MST is the sum of all the lengths of all edges of which are part of the tree.
* The sum of the lengths of all edges is as small as possible.

For example, let's say $n=4$, $m=5$ and $s=4$. We need to construct a graph with $4$ nodes and $5$ edges. The value of minimum spanning tree must be $4$. The diagram belows shows a way to construct such a graph while keeping the lengths of all edges is as small as possible:

![image](https://s3.amazonaws.com/hr-assets/0/1487251853-4d9507b76b-minmst6.png)

Here the sum of lengths of all edges is $7$.

Given $n$, $m$, and $s$ for $g$ graphs satisfying the conditions above, find and print the minimum sum of the lengths of all the edges in each graph on a new line.

**Note:** It is guaranteed that, for all given combinations of $n$, $m$, and $s$, we can construct a valid graph.


## Input Format

The first line contains an integer, $g$, denoting the number of graphs. 	
Each of the $g$ subsequent lines contains three space-separated integers describing the respective values of $n$ (the number of nodes in the graph), $m$ (the number of edges in the graph), and $s$ (the value of the MST graph).

## Output Format

For each graph, print an integer on a new line denoting the minimum sum of the lengths of all edges in a graph satisfying the given conditions.

## Constraints

For $\text{20%}$ of the maximum score: 

* $1$ $\leq$ $g$ $\leq$ $100$
* $2$ $\leq$ $n$ $\leq$ $10$
* $1$ $\leq$ $m$ $\leq$ $50$
* $1$ $\leq$ $s$ $\leq$ $20$

For $\text{50%}$ of the maximum score: 

* $1$ $\leq$ $g$ $\leq$ $100$
* $2$ $\leq$ $n$ $\leq$ $50$
* $1$ $\leq$ $m$ $\leq$ $2000$
* $1$ $\leq$ $s$ $\leq$ $200$

For $\text{70%}$ of the maximum score: 

* $1$ $\leq$ $g$ $\leq$ $100$
* $2$ $\leq$ $n$ $\leq$ $10^5$
* $1$ $\leq$ $m$ $\leq$ $10^{10}$
* $1$ $\leq$ $s$ $\leq$ $10^{6}$

For $\text{100%}$ of the maximum score: 

* $1$ $\leq$ $g$ $\leq$ $1000$
* $2$ $\leq$ $n$ $\leq$ $10^8$
* $1$ $\leq$ $m$ $\leq$ $10^{16}$
* $1$ $\leq$ $s$ $\leq$ $10^{10}$

## Sample Input

4 5 4
4 3 6

## Sample Output

6

## Explanation

- Graph :

The answer for this sample is already explained the problem statement.

- Graph :

We must construct a graph with  nodes,  edges, and an MST value of . Recall that a connected graph with  nodes and  edges is already a tree, so the MST will contain all  edges and the total length of all the edges of the graph will be equal to the value of the minimum spanning tree. So the answer is .
