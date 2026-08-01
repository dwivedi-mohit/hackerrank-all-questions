# Lovely Triplets

- **Domain:** algorithms
- **Difficulty:** Advanced
- **Max Score:** 80
- **Success Ratio:** 0.8099569171852561
- **Total Submissions:** 2089
- **Solved Count:** 1692
- **URL:** https://www.hackerrank.com/challenges/lovely-triplets

## Problem Statement

Daniel loves graphs. He thinks a graph is *special* if it has the following properties:

* It is undirected.
* The length of each edge is $1$.
* It includes *exactly* $P$ different *lovely triplets*. 

A *triplet* is a set of $3$ different nodes. A triplet is *lovely* if the minimum distance between each pair of nodes in the triplet is *exactly* $Q$. Two triplets are different if $1$ or more of their component nodes are different. 

Given $P$ and $Q$, help Daniel draw a *special graph*.

## Input Format

A single line containing $2$ space-separated integers, $P$ (the number of different lovely triplets you must have in your graph) and $Q$ (the required *distance* between each pair of nodes in a lovely triplet), respectively.



## Output Format

For the first line, print $2$ space-separated integers, $N$ (the number of nodes in the graph) and $M$ (the number of edges in the graph), respectively.	
On each line $i$ of the $M$ subsequent lines, print two space-separated integers, $u_i$ and $v_i$, describing an edge between nodes $u_i$ and $v_i$.

Your output must satisfy the following conditions:

* $0 \le N,M \le 100$<br>
* $1 \le u_i,v_i \le N$<br>

If there is more than one correct answer, print any one of them.

## Constraints

* $1 \le P \le 5000$
* $2 \le Q \le 9$

## Sample Input

3 2

## Sample Output

7 7
1 2
2 3
3 4
4 5
5 6
6 1
1 7

## Explanation

There are exactly  lovely triplets in this graph: , , and .

Observe that each node in a lovely triplet is  edges away from the other nodes composing the lovely triplet.
