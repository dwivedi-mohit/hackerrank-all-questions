# Jenny's Subtrees

- **Domain:** java
- **Difficulty:** Hard
- **Max Score:** 70
- **Success Ratio:** 0.7770241627808393
- **Total Submissions:** 11795
- **Solved Count:** 9165
- **URL:** https://www.hackerrank.com/challenges/jenny-subtrees

## Problem Statement

Jenny loves experimenting with [trees](https://en.wikipedia.org/wiki/Tree_(graph_theory)). Her favorite tree has $n$ nodes connected by $n - 1$ edges, and each edge is $1$ unit in length. She wants to cut a *subtree* (i.e., a connected part of the original tree) of radius $r$ from this tree by performing the following two steps:

1. Choose a node, $x$, from the tree.
2. Cut a subtree consisting of *all* nodes which are *not further* than $r$ units from node $x$. 

For example, the blue nodes in the diagram below depict a subtree centered at $x = 1$ that has radius $r = 2$:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1483075128-6989fccb33-jenny3.png)

Given $n$, $r$, and the definition of Jenny's tree, find and print the number of *different* subtrees she can cut out. Two subtrees are considered to be different if they are not  [isomorphic](https://en.wikipedia.org/wiki/Graph_isomorphism).

## Input Format

The first line contains two space-separated integers denoting the respective values of $n$ and $r$.  	
Each of the next $n - 1$ subsequent lines contains two space-separated integers, $x$ and $y$, describing a bidirectional edge in Jenny's tree having length $1$.

## Output Format

Print the total number of different possible subtrees.

## Constraints

+ $1 \le n \le 3000$  
+ $0 \le r \le 3000$  
+ $1 \le x,y \le n$

**Subtasks**

For $50\%$ of the max score:

+ $1 \le n \le 500$  
+ $0 \le r \le 500$ 

## Sample Input

7 1
1 2
1 3
1 4
1 5
2 6
2 7

## Sample Output

3

## Explanation

In the diagram below, blue nodes denote the possible subtrees:

The last  subtrees are considered to be the same (i.e., they all consist of two nodes connected by one edge), so we print  as our answer.
