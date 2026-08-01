# HackerRank City

- **Domain:** sql
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.8470557582073996
- **Total Submissions:** 3838
- **Solved Count:** 3251
- **URL:** https://www.hackerrank.com/challenges/hr-city

## Problem Statement

HackerRank-city is an acyclic connected graph (or [tree](https://en.wikipedia.org/wiki/Tree_(graph_theory))). Its not an ordinary place, the construction of the whole tree takes place in $N$ steps. The process is described below:

*	It initially has $1$ node.
*	At each step, you must create $3$ duplicates of the current tree, and create $2$ new nodes to connect all $4$ copies in the following **`H`** shape:
		
<img src="https://s3.amazonaws.com/hr-challenge-images/15974/1453287425-a21e2a7db5-nik2.png" title="nik2.png" />
	
At each $i^{th}$ step, the tree becomes $4$ times bigger plus $2$ new nodes, as well as $5$ new edges connecting everything together. The length of the new edges being added at step $i$ is denoted by input $A_{i}$.
    
Calculate the sum of distances between each pair of nodes; as these answers may run large, print your answer modulo $1000000007$.



## Input Format

The first line contains an integer, $N$ (the number of steps). The second line contains $N$ space-separated integers describing  $A_0$, $A_1, \ldots, A_{N-2}, A_{N-1}$.<br>

**Constraints**<br>
$1\le N \le 10^6$<br>
$1 \le A_i \le 9$<br>

**Subtask**		
For $50\%$ score $1 \le N\le 10$

## Output Format

Print the sum of distances between each pair of nodes [modulo](https://en.wikipedia.org/wiki/Modulo_operation) $1000000007$.<br>

**Sample Input 0**
    
    1
	1

**Sample Output 0**

	29
    
**Sample Input 1**
    
    2
	2 1

**Sample Output 1**

	2641

## Constraints

Subtask

For  score

## Sample Input

1
1

## Sample Output

29

## Explanation

Sample 0

In this example, our tree looks like this:

Let  denote the distance between nodes  and .

.

We print the result of  as our answer.

Sample 1

In this example, our tree looks like this:

We calculate and sum the distances between nodes in the same manner as Sample 0 above, and print the result of our , which is .
