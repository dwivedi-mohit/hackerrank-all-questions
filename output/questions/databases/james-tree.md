# Magic Number Tree

- **Domain:** databases
- **Difficulty:** Medium
- **Max Score:** 60
- **Success Ratio:** 0.75
- **Total Submissions:** 84
- **Solved Count:** 63
- **URL:** https://www.hackerrank.com/challenges/james-tree

## Problem Statement

James has a tree with $n$ nodes $n-1$ edges where the $i^{th}$ edge has a length, $w_i$. He wants to play a game involving $n$ moves. During each move, he performs the following steps:

* Randomly chooses some node $x_i$ from the tree. Each node has an equal probability of being chosen.
* Calculates the distance from node $x_i$ to each node reachable from $x_i$ using one or more edges.
* Deletes node $x_i$.

For example, the diagram below shows what happens when we choose a random node and delete it from the tree:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1483093526-099fca06d4-magic11.png)

After $n$ moves, the tree is empty and the game ends.

James defines the magic number, $m$, as the sum of all numbers calculated in step $2$ of each move. Let $E_{m}$ be the [expected value](https://en.wikipedia.org/wiki/Expected_value) of $m$.

Give the tree's edges and their respective lengths, calculate and the print the value of $(E_{m} \times n!)\ \text{mod}\ (10^9+9)$. It is guaranteed that $E_{m} \times n!$ is an integer.


**Note**

Due to a bug in the system, you might see ``accepted`` verdict in this problem even if you don't pass all the test cases. Please ignore that verdict, only the score you get is important in the ranklist.

## Input Format

The first line contains an integer, $n$, denoting the number of nodes. 	
Each of the $n-1$ subsequent lines contains three space-separated integers describing the respective values of $u_i$, $v_i$, and $w_i$, meaning that there is an edge of length $w_i$ connecting nodes $u_i$ and $v_i$.  

## Output Format

Print a single integer denoting the value of $(E_{m} \times n!)\ \text{mod}\ (10^9+9)$.

## Constraints

* $1 \le n \le 5000$
* $1 \le u_i,v_i \le n$
* $1 \le w_i \le 10^9$

**Subtasks**

* For $30\%$ of the max score $n \le 10$
* For $60\%$ of the max score $n \le 400$

## Sample Input

2 1 2
3 2 3

## Explanation

Let  be the distance between node  and node . Here are the  different variants:

-

-

- .

- .

- .

- .

The expected value of the magic number is . We then print the value of .
