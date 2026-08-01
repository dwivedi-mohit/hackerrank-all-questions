# Binary Search Tree : Lowest Common Ancestor

- **Domain:** c
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9349575185662727
- **Total Submissions:** 177607
- **Solved Count:** 166055
- **URL:** https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor

## Problem Statement

You are given pointer to the root of the binary search tree and two values $v1$ and $v2$. You need to return the lowest common ancestor ([LCA](https://en.wikipedia.org/wiki/Lowest_common_ancestor)) of $v1$ and $v2$ in the binary search tree.  


![image](https://s3.amazonaws.com/hr-assets/0/1529959649-81b68736f7-lcaexample.png)  
[//]: # "![image](https://s3.amazonaws.com/hr-assets/0/1502911253-5a96d423eb-lca.png)"

In the diagram above, the lowest common ancestor of the nodes $4$ and $6$ is the node $3$.  Node $3$ is the lowest node which has nodes $4$ and $6$ as descendants.

**Function Description**  

Complete the function *lca* in the editor below.  It should return a pointer to the lowest common ancestor node of the two values given.  

lca has the following parameters:  
-  root: a pointer to the root node of a binary search tree  
-  v1: a node.data value  
-  v2: a node.data value  

## Input Format

The first line contains an integer, $n$, the number of nodes in the tree.  
The second line contains $n$ space-separated integers representing $node.data$ values.  
The third line contains two space-separated integers, $v1$ and $v2$.  

To use the test data, you will have to create the binary search tree yourself.  Here on the platform, the tree will be created for you.

## Output Format

Return the a pointer to the node that is the lowest common ancestor of $v1$ and $v2$.

## Constraints

$1 \le n, node.data \le 25$  
$1 \le v1,v2 \le 25$  
$v1 \ne v2$  
The tree will contain nodes with *data* equal to $v1$ and $v2$.  

## Sample Input

4 2 3 1 7 6
1 7

 and .

## Sample Output

[reference to node 4]

## Explanation

LCA of  and  is , the root in this case.

Return a pointer to the node.
