# Self-Driving Bus

- **Domain:** fp
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.7501306847882906
- **Total Submissions:** 3826
- **Solved Count:** 2870
- **URL:** https://www.hackerrank.com/challenges/self-driving-bus

## Problem Statement

Treeland is a country with $n$ cities and $n-1$ roads. There is exactly *one* path between any two cities. 	

The ruler of Treeland wants to implement a self-driving bus system and asks tree-loving Alex to plan the bus routes. Alex decides that each route must contain a subset of *connected* cities; a subset of cities is *connected* if the following two conditions are true:

1. There is a path between every pair of cities which belongs to the subset.
2. Every city in the path must belong to the subset.

<img src="https://s3.amazonaws.com/hr-challenge-images/13863/1453203150-be95d05a3f-tree.png" title="tree.png" />

In the figure above, $\{2,3,4,5\}$ is a *connected* subset, but $\{6,7,9\}$ is not  (for the second condition to be true, $8$ would need to be part of the subset).

Each self-driving bus will operate within a *connected segment* of Treeland. A connected segment $[L, R]$ where $1 \le L \le R \le n$ is defined by the connected subset of cities $S = \{x \ | x \in Z\ and\ \ L \le x \le R\}$. 

In the figure above, $[2,5]$ is a connected segment that represents the subset $\{2,3,4,5\}$. Note that a single city can be a segment too.

Help Alex to find number of connected segments in Treeland.

## Input Format

The first line contains a single positive integer, $n$.	
The $n - 1$ subsequent lines each contain two positive space-separated integers, $a_i$ and $b_i$, describe an edge connecting two nodes in tree $T$.




## Output Format

Print a single integer: the number of segments $[L, R]$, which are connected in tree $T$.

## Constraints

* $1 \le n \le 2\times10^5$<br>
* $1 \le a_i, b_i \le n$<br>

**Subtasks**	

* For $25\%$ score: $1 \le n \le 2\times 10^3$<br>
* For $50\%$ score: $1 \le n \le 10^4$<br>

## Sample Input

1 3
3 2

## Explanation

The connected segments for our test case are: , , , , and . These segments can be represented by the respective subsets: , , , , and .

Note:  is not a connected segment. It represents the subset  and the path between  and  goes through  which is not a member of the subset.
