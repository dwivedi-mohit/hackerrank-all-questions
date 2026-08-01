# Prim's (MST) : Special Subtree

- **Domain:** cpp
- **Difficulty:** Medium
- **Max Score:** 60
- **Success Ratio:** 0.8656490284458922
- **Total Submissions:** 26401
- **Solved Count:** 22854
- **URL:** https://www.hackerrank.com/challenges/primsmstsub

## Problem Statement

Given a graph which consists of several edges connecting its nodes, find a subgraph of the given graph with the following properties:  

* The subgraph contains all the nodes present in the original graph.  
* The subgraph is of minimum overall weight (sum of all edges) among all such subgraphs.  
* It is also required that there is __exactly one, exclusive__ path between any two nodes of the subgraph. 

One specific node $S$ is fixed as the starting point of finding the subgraph using [Prim's Algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm).  
Find the total weight or the sum of all edges in the subgraph.

**Example**   
$n = 3$   
$edges = [[1, 2, 2], [2, 3, 2], [1, 3, 3]]$   
$start = 1$   

![image](https://s3.amazonaws.com/hr-assets/0/1537557145-7197b9502a-primsexample.png)  

Starting from node $1$, select the lower weight edge, i.e. $1\leftrightarrow 2$, weight $2$.   

Choose between the remaining edges, $1\leftrightarrow 3$, weight $3$, and $2\leftrightarrow 3$, weight $2$.  

The lower weight edge is $2\leftrightarrow 3$ weight $2$.   

All nodes are connected at a cost of $2+2=4$. The edge $1\leftrightarrow 3$ is not included in the subgraph.   

**Function Description**

Complete the *prims* function in the editor below.  

prims has the following parameter(s):  

- *int n:* the number of nodes in the graph  
- *int edges[m][3]:* each element contains three integers, two nodes numbers that are connected and the weight of that edge  
- *int start*: the number of the starting node  

**Returns**   

- *int:* the minimum weight to connect all nodes in the graph

## Input Format

The first line has two space-separated integers $n$ and $m$, the number of nodes and edges in the graph.  

Each of the next $m$ lines contains three space-separated integers $u$, $v$ and $w$, the end nodes of $edges[i]$, and the edge's weight.  
The last line has an integer $start$, the starting node.  



## Constraints

$2 \le n \le 3000$  
$1 \le m \le (n*(n-1))/2$  
$1 \le u, v, start \le n$  
$0 \le w \le 10^5$  
__There may be multiple edges between two nodes.__

## Sample Input

5 6
1 2 3
1 3 4
4 2 6
5 2 2
2 3 5
3 5 7
1

## Sample Output

15

## Explanation

The graph given in the test case is shown as :

- The starting node is  (in the given test case)

Applying the Prim's algorithm, edge choices available at first are :

 (WT. 3)  and  (WT. 4) , out of which  is chosen (smaller weight of edge).

Now the available choices are :

 (WT. 4) ,  (WT. 5) ,  (WT. 2) and  (WT. 6) , out of which  is chosen by the algorithm.

Following the same method of the algorithm, the next chosen edges , sequentially are :

 and .

Hence the overall sequence of edges picked up by Prim's are:

and the total weight of the MST (minimum spanning tree) is :
