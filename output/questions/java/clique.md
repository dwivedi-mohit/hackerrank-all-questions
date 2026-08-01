# Clique

- **Domain:** java
- **Difficulty:** Medium
- **Max Score:** 60
- **Success Ratio:** 0.5846322121957889
- **Total Submissions:** 7314
- **Solved Count:** 4276
- **URL:** https://www.hackerrank.com/challenges/clique

## Problem Statement

A clique in a graph is set of nodes such that there is an edge between any two distinct nodes in the set. Finding the largest clique in a graph is a computationally difficult problem. Currently no polynomial time algorithm  is known for solving this. However, you wonder what is the minimum size of the largest clique in any graph with $n$ nodes and $m$ edges.  

For example, consider a graph with $n=4$ nodes and $m=5$ edges.  The graph below shows $4$ nodes with $4$ edges and no cliques.  It is evident that the addition of any $5^{th}$ edge must create two cliques with $3$ members each.  


![image](https://s3.amazonaws.com/hr-assets/0/1526329612-3c9c0f082d-cliqueExample.png)


## Input Format

The first line contains an integer $t$, the number of test cases.  

Each of the next $t$ lines contains two space-separated integers $n$ and $m$.  


## Output Format

For each test case, print the minimum size of the largest clique that must be formed given $n$ and $m$.   


## Constraints

* $1 \le t \le 100000$  
* $2 \le n \le 10000$  
* $1 \le m \le \frac{n \times (n-1)}{2}$


## Sample Input

3 2
4 6
5 7

## Sample Output

4
3

## Explanation

For the first case, we have two cliques with two nodes each:

For the second test case, the only valid graph having  nodes and  edges is one where each pair of nodes is connected. So the size of the largest clique cannot be smaller than .

For the third test case, it is easy to verify that any graph with  nodes and .  The  solid lines in the graph below indicate the maximum edges that can be added without forming a clique larger than .  The dashed lines could connect any two nodes not connected by solid lines producing a clique of size .

Hints
Turan's theorem gives us an upper bound on the number of edges a graph can have if we wish that it should not have a clique of size . Though the bound is not exact, it is easy to extend the statement of the theorem to get an exact bound in terms of  and . Once this is done, we can binary search for the largest  such that . See: Turan's Theorem
