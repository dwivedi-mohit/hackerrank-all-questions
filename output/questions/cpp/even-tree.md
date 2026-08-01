# Even Tree

- **Domain:** cpp
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.8972014280778533
- **Total Submissions:** 43415
- **Solved Count:** 38952
- **URL:** https://www.hackerrank.com/challenges/even-tree

## Problem Statement

You are given a tree (a simple connected graph with no cycles). 

Find the maximum number of edges you can remove from the tree to get a [forest](http://en.wikipedia.org/wiki/Tree_(graph_theory)) such that each connected component of the forest contains an even number of nodes.

As an example, the following tree with $4$ nodes can be cut at most $1$ time to create an even forest.  


![image](https://s3.amazonaws.com/hr-assets/0/1533926256-3a1cc069a7-evenforestexb.png)  

**Function Description**  

Complete the *evenForest* function in the editor below.  It should return an integer as described.  

evenForest has the following parameter(s):  

- *t_nodes*: the number of nodes in the tree  
- *t_edges*: the number of undirected edges in the tree  
- *t_from*: start nodes for each edge  
- *t_to*: end nodes for each edge, (Match by index to *t_from*.)  

## Input Format

The first line of input contains two integers $t_nodes$ and $t_edges$, the number of nodes and edges.  
The next $t_edges$ lines contain two integers $t_from[i]$ and $t_to[i]$ which specify nodes connected by an edge of the tree. The root of the tree is node $1$.

## Output Format

Print the number of removed edges.

## Constraints

* $2 \le n \le 100$ 
* $n \in \mathbb Z_\text{even}^+$  

*Note:* The tree in the input will be such that it can always be decomposed into components containing an even number of nodes. $\mathbb Z_\text{even}^+ $ is the set of positive even integers.
