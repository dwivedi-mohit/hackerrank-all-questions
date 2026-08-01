# Diameter Minimization

- **Domain:** ai
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.8165413533834587
- **Total Submissions:** 1995
- **Solved Count:** 1629
- **URL:** https://www.hackerrank.com/challenges/diameter-minimization

## Problem Statement

We define the [diameter](https://en.wikipedia.org/wiki/Distance_(graph_theory)) of a [strongly-connected](https://en.wikipedia.org/wiki/Strongly_connected_component) [oriented](https://en.wikipedia.org/wiki/Orientation_(graph_theory)) graph, $G = (V, E)$, as the minimum integer $d$ such that for each $u, v \in G$ there is a path from $u$ to $v$ of length $\le d$ (recall that a path's length is its number of edges).  

Given two integers, $n$ and $m$, build a strongly-connected oriented graph with $n$ vertices where each vertex has [outdegree](https://en.wikipedia.org/wiki/Directed_graph#Indegree_and_outdegree) $m$ and *the graph's diameter is as small as possible* (see the *Scoring* section below for more detail). Then print the graph according to the *Output Format* specified below.  

Here's a sample strongly-connected oriented graph with $3$ nodes, whose outdegree is $2$ and diameter is $1$.  


![image](https://s3.amazonaws.com/hr-assets/0/1487903169-c6a2be14b5-ScreenShot2017-02-24at7.52.34am.png)

**Note:** Cycles and multiple edges between vertices are allowed.

## Input Format

Two space-separated integers describing the respective values of $n$ (the number of vertices) and $m$ (the outdegree of each vertex).

## Output Format

First, print an integer denoting the diameter of your graph on a new line.		
Next, print $n$ lines where each line $i$ ($0 \le i \lt n$) contains $m$ space-separated integers in the inclusive range from $0$ to $n-1$ describing the endpoints for each of vertex $i$'s outbound edges.

## Constraints

- $2 \le n \le 1000$
- $2 \le m \le \min(n, 5)$

**Scoring**  	

We denote the diameter of your graph as $d$ and the diameter of the graph in the author's solution as $s$. Your score for each test case (as a real number from $0$ to $1$) is:

- $1$ if $d \le s + 1$
- $\frac{s}{d}$ if $s + 1 < d \le 5 \times s$
- $0$ if $5 \times s < d$

## Sample Input

5 2

## Sample Output

2
1 4
2 0
3 1
4 2
0 3

## Explanation

The diagram below depicts a strongly-connected oriented graph with  nodes where each node has an outdegree of :

The diameter of this graph is , which is minimal as the outdegree of each node must be . We cannot construct a graph with a smaller diameter of  because it requires an outbound edge from each vertex to each other vertex in the graph (so the outdegree of that graph would be ).
