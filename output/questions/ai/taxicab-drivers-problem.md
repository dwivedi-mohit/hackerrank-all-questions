# Taxicab Driver's Problem

- **Domain:** ai
- **Difficulty:** Advanced
- **Max Score:** 150
- **Success Ratio:** 0.7451456310679612
- **Total Submissions:** 2884
- **Solved Count:** 2149
- **URL:** https://www.hackerrank.com/challenges/taxicab-drivers-problem

## Problem Statement

Burger Town is a city that consists of $N$ special junctions and $N - 1$ pathways. There is exactly one shortest path between each pair of junctions. Junction $i$ is located at $(x_i, y_i)$ and the distance between two junctions $i, j$ is defined by the Taxicab geometry. 

Tim has recently afforded a taxicab to work as a taxicab driver. His vehicle was very cheap, but has a very big flaw. It can only drive $H$ units horizontally and $V$ units vertically before refueling. 

If a customer wants to be brought from a junction $i$ to another junction $j$, then this car is only capable of driving the route, iff the sum of horizontal distances and the sum of vertical distances on this path are less than or equal to $H$ and $V$ respectively. 

Also, there is a unique path between any two junctions.  

<img src="https://s3.amazonaws.com/hr-challenge-images/6367/1431544255-d42b5c89d0-drawing1.svg" />

Now he has thoughts about returning the vehicle back to the seller. But he first wants to know, if it's even worth it. That's why he wants to know the number of unordered pairs $(i, j)$ such that it is not possible to drive a customer from junction $i$ to junction $j$. 

**Input Format**

On the first line you will be given $N$, $H$ and $V$ separated by a single space.  
Each of the next $N$ lines contains two space separated integers $x_i, y_i$, denoting the location of junction $i$.
Each of the next $N - 1$ lines contains two space separated integers describing a path existing between $u_i, v_i$, i.e., there is a path between $u_i$ and $v_i$.  

**Output Format**

Output the number of unordered pairs $(i, j)$ such that it is not possible to drive from $i$ to $j$. 

**Constraints**

$2 \leq N \leq 10^5$

$0 \leq H, V \leq 10^{14}$

$0 \leq x_i, y_i \leq 10^9$

**Sample Input**

    3 2 1
    0 0
    1 1
    2 0
    1 2
    2 3

**Sample Output**

	1
    
**Explanation**

The car is only capable of driving $H = 2$ units horizontally and $V = 1$ unit vertically. The horizontal distance between junction 1 and 3(via 2) is equal to 2($0 \rightarrow 1 \rightarrow 2$), which fits under the horizontal limit of the car. The vertical distance between 1 and 3 is also equal to 2($0 \rightarrow 1 \rightarrow 0$), but this is not possible for this car since $2 > V$.


## Input Format

On the first line you will be given ,  and  separated by a single space.

Each of the next  lines contains two space separated integers , denoting the location of junction .
Each of the next  lines contains two space separated integers describing a path existing between , i.e., there is a path between  and .

## Output Format

Output the number of unordered pairs  such that it is not possible to drive from  to .

## Sample Input

3 2 1
0 0
1 1
2 0
1 2
2 3

## Explanation

The car is only capable of driving  units horizontally and  unit vertically. The horizontal distance between junction 1 and 3(via 2) is equal to 2(), which fits under the horizontal limit of the car. The vertical distance between 1 and 3 is also equal to 2(), but this is not possible for this car since .
