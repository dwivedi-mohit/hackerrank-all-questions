# Similar Pair

- **Domain:** java
- **Difficulty:** Advanced
- **Max Score:** 70
- **Success Ratio:** 0.5745834947694692
- **Total Submissions:** 7743
- **Solved Count:** 4449
- **URL:** https://www.hackerrank.com/challenges/similarpair

## Problem Statement

A pair of nodes, $(a, b)$, is a *similar pair* if the following conditions are true:

1. node $a$ is the ancestor of node $b$
2. $abs(a - b) \le k$

Given a tree where each node is labeled from $1$ to $n$, find the number of similar pairs in the tree.

For example, given the following tree:  


![image](https://s3.amazonaws.com/hr-assets/0/1526312674-07a423e94f-similarpairsExample.png)  
  
We have the following pairs of ancestors and dependents:  

```
Pair	abs(a-b)	Pair	abs(a-b)
1,2	1		3,4	1
1,3	2		3,5	2
1,4	3		3,6	3
1,5	4
1,6	5
```
If $k=3$ for example, we have $6$ pairs that are *similar*, where $abs(a-b) \le k$.

**Function Description**

Complete the *similarPair* function in the editor below.  It should return an integer that represents the number of pairs meeting the criteria.

similarPair has the following parameter(s):  

- *n*: an integer that represents the number of nodes  
- *k*: an integer
- *edges*: a two dimensional array where each element consists of two integers that represent connected node numbers  

## Input Format

The first line contains two space-separated integers $n$ and $k$, the number of nodes and the similarity threshold. 	
Each of the next $n-1$ lines contains two space-separated integers defining an edge connecting nodes $p[i]$ and $c[i]$, where node $p[i]$ is the parent to node $c[i]$.

## Output Format

Print a single integer denoting the number of similar pairs in the tree.

## Constraints

- $1 \le n \le 10^5$  
- $0 \le k \le n$  
- $1 \le p[i], c[i] \le n$  

## Sample Input

5 2
3 2
3 1
1 4
1 5

## Explanation

The similar pairs are , , , and , so we print  as our answer.

Observe that  and  are not similar pairs because they do not satisfy  for .
