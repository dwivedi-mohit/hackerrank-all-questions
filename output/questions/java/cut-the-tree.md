# Cut the Tree

- **Domain:** java
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.7366162055565223
- **Total Submissions:** 17241
- **Solved Count:** 12700
- **URL:** https://www.hackerrank.com/challenges/cut-the-tree

## Problem Statement

There is an undirected tree where each vertex is numbered from $1$ to $n$, and each contains a data value.  The *sum* of a tree is the sum of all its nodes' data values.  If an edge is cut, two smaller trees are formed.  The *difference* between two trees is the absolute value of the difference in their sums.  

Given a tree, determine which edge to cut so that the resulting trees have a minimal *difference* between them, then return that difference.  

**Example**   
$data = [1, 2, 3, 4, 5, 6]$   
$edges = [(1,2),(1,3),(2,6),(3,4),(3,5)]$   


In this case, node numbers match their weights for convenience.  The graph is shown below.   

![image](https://s3.amazonaws.com/hr-assets/0/1525451112-5ca073ae7a-cutthetreeexample.png)

The values are calculated as follows:  

    Edge	Tree 1	Tree 2	Absolute
    Cut		Sum		 Sum	 Difference
    1		 8		   13		  5
    2		 9		   12		  3
    3		 6		   15		  9
    4		 4		   17		 13
    5		 5		   16		 11
    
The minimum absolute difference is $3$.

**Note:** The given tree is *always* rooted at vertex $1$.  

**Function Description**  

Complete the *cutTheTree* function in the editor below.    

cutTheTree has the following parameter(s):  

- *int data[n]:* an array of integers that represent node values  
- *int edges[n-1][2]:* an 2 dimensional array of integer pairs where each pair represents nodes connected by the edge  

**Returns**  

- *int:* the minimum achievable absolute difference of tree sums  

## Input Format

The first line contains an integer $n$, the number of vertices in the tree.	 	
The second line contains $n$ space-separated integers, where each integer $u$ denotes the $node[u]$ data value, $data[u]$.		
Each of the $n - 1$ subsequent lines contains two space-separated integers $u$ and $v$ that describe edge $u \leftrightarrow v$ in tree $t$.		

## Constraints

- $3 \le n \le 10^5$  
- $1 \le data[u] \le 1001$, where $1 \le u \le n$.

## Sample Input

STDIN                       Function
-----                       --------
6                           data[] size n = 6
100 200 100 500 100 600     data = [100, 200, 100, 500, 100, 600]
1 2                         edges = [[1, 2], [2, 3], [2, 5], [4, 5], [5, 6]]
2 3
2 5
4 5
5 6

## Explanation

We can visualize the initial, uncut tree as:

There are  edges we can cut:

- Edge  results in

- Edge  results in

- Edge  results in

- Edge  results in

- Edge  results in

The minimum difference is .
