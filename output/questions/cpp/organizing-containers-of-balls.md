# Organizing Containers of Balls

- **Domain:** cpp
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.8774373884442249
- **Total Submissions:** 89081
- **Solved Count:** 78163
- **URL:** https://www.hackerrank.com/challenges/organizing-containers-of-balls

## Problem Statement

David has several containers, each with a number of balls in it.  He has just enough containers to sort each type of ball he has into its own container.  David wants to sort the balls using his sort method.

David wants to perform some number of swap operations such that:

* Each container contains only balls of the same type.
* No two balls of the same type are located in different containers.


**Example**   

$containers = [[1, 4], [2, 3]]$   

David has $n=2$ containers and $2$ different types of balls, both of which are numbered from $0$ to $n-1 = 1$. The distribution of ball types per container are shown in the following diagram.   

![image](https://s3.amazonaws.com/hr-challenge-images/0/1485811368-9e78c98652-swapping-balls.png)

In a single operation, David can *swap* two balls located in different containers.

The diagram below depicts a single swap operation:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1485811849-e97b84e218-swapping-balls-ps-1.png)

In this case, there is no way to have all green balls in one container and all red in the other using only swap operations.  Return `Impossible`.  

You must perform $q$ queries where each query is in the form of a matrix, $M$. For each query, print ``Possible`` on a new line if David can satisfy the conditions above for the given matrix.  Otherwise, print ``Impossible``.  

**Function Description**  

Complete the *organizingContainers* function in the editor below.   

organizingContainers has the following parameter(s):  

- *int containter[n][m]*: a two dimensional array of integers that represent the number of balls of each color in each container  

**Returns**   

- *string:*  either `Possible` or `Impossible`     

## Input Format

The first line contains an integer $q$, the number of queries.  

Each of the next $q$ sets of lines is as follows:  

1. The first line contains an integer $n$, the number of containers (rows) and ball types (columns).		
2. Each of the next $n$ lines contains $n$ space-separated integers describing row $containers[i]$.

## Output Format

For each query, print ``Possible`` on a new line if David can satisfy the conditions above for the given matrix.  Otherwise, print ``Impossible``.

## Constraints

* $1 \le q \le 10$  
* $1 \le n \le 100$  
* $0 \le containers[i][j] \le 10^9$

**Scoring**

* For $33\%$ of score, $1 \le n \le 10$.  
* For $100\%$ of score, $1 \le n \le 100$.

## Sample Input

2
2
1 1
1 1
2
0 2
1 1

## Sample Output

Possible
Impossible

## Explanation

We perform the following  queries:

- The diagram below depicts one possible way to satisfy David's requirements for the first query:

Thus, we print Possible on a new line.

- The diagram below depicts the matrix for the second query:

No matter how many times we swap balls of type  and  between the two containers, we'll never end up with one container only containing type  and the other container only containing type . Thus, we print Impossible on a new line.
