# Tree Splitting

- **Domain:** c
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.8343949044585988
- **Total Submissions:** 2041
- **Solved Count:** 1703
- **URL:** https://www.hackerrank.com/challenges/tree-splitting

## Problem Statement

Given a tree with vertices numbered from $1$ to $n$. You need to process $m$ queries. Each query represents a vertex number encoded in the following way:

**Queries are encoded in the following way**: Let, $m_j$ be the $j^{th}$ query and $ans_j$ be the answer for the $j^{th}$ query where $1 \le j \le \ m$ and $ans_0$ is always $0$. Then vertex $v_j = ans_{j - 1} \oplus m_j$.
We are assure that $v_j$ is between $1$ and $n$, and hasn't been removed before. 

**Note:** $\oplus$ is the bitwise XOR operator.

For each query, first decode the vertex $v$ and then perform the following:

 1. Print the size of the connected component containing $v$.  
 2. Remove vertex $v$ and all edges connected to $v$.  
  


## Input Format

The first line contains a single integer, $n$, denoting the number of vertices in the tree.		
Each line $i$ of the $n - 1$ subsequent lines (where $0 \le i \lt n$) contains $2$ space-separated integers describing the respective nodes, $u_i$ and $v_i$, connected by edge $i$.		
The next line contains a single integer, $m$, denoting the number of queries.	
Each line $j$ of the $m$ subsequent lines contains a single integer, vertex number $m_j$.  

## Output Format

For each query, print the size of the corresponding connected component on a new line.

**Sample Input 0**

    3
    1 2
    1 3
    3
    1
    1
    2
    
**Sample Output 0**

	3
    1
    1

**Sample Input 1**
	
    4
    1 2
    1 3
    1 4
    4
    3
    6
    2
    6

**Sample Output 1**
	
    4
    3
    2
    1

## Constraints

- $1 \le n, m \le 2 \cdot 10^5.$  

## Sample Input

3
1 2
1 3
3
1
1
2

## Sample Output

3
1
1

## Explanation

Sample Case 0:

We have,  = 0 and connected component :

 has vertex =  =  = . The size of connected component containing  is .

So,  = .
Removing vertex  and all of it's edges, we get two disconnected components :

 has vertex =  =  = . The size of connected component containing  is .

So,  = .

Removing vertex  and all of it's edges, we are left with only one component :

 has vertex =  =  = . The size of connected component containing  is .

So,  = .

Removed vertex .

Sample Case 1:

We have,  =  and connected component :

 has vertex =  =  = . The size of connected component containing  is .

So,  = .

Removing vertex  and all of it's edges, we get component :

 has vertex =  =  = . The size of connected component containing  is .

So,  = .

Removing vertex  and all of it's edges, now, we get two disconnected components :

 has vertex =  =  = . The size of connected component containing  is .

So,  = .

Removing vertex  and all of it's edges, now we are left with only one component :

 has vertex =  =  = . The size of connected component containing  is .

So,  = .

Removed vertex .
