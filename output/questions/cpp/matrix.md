# Matrix

- **Domain:** cpp
- **Difficulty:** Hard
- **Max Score:** 70
- **Success Ratio:** 0.6862098318791232
- **Total Submissions:** 9398
- **Solved Count:** 6449
- **URL:** https://www.hackerrank.com/challenges/matrix

## Problem Statement

The kingdom of Zion has cities connected by bidirectional roads.  There is a unique path between any pair of cities. Morpheus has found out that the machines are planning to destroy the whole kingdom.  If two machines can join forces, they will attack.  Neo has to destroy roads connecting cities with machines in order to stop them from joining forces.  There must not be any path connecting two machines.

Each of the roads takes an amount of time to destroy, and only one can be worked on at a time.  Given a list of edges and times, determine the minimum time to stop the attack.

For example, there are $n = 5$ cities called $0 - 4$.  Three of them have machines and are colored red.  The time to destroy is shown next to each road.  If we cut the two green roads, there are no paths between any two machines.  The time required is $3 + 2 = 5$.  

![image](https://s3.amazonaws.com/hr-assets/0/1528209077-f7699103c6-matrixExample.png)  

**Function Description**

Complete the function *minTime* in the editor below.  It must return an integer representing the minimum time to cut off access between the machines.

minTime has the following parameter(s):

- *roads*: a two-dimensional array of integers, each $roads[i] = [city1, city2, time]$ where cities are connected by a road that takes $time$ to destroy  
- *machines*: an array of integers representing cities with machines  

## Input Format

The first line of the input contains two space-separated integers, $n$ and $k$, the number of cities and the number of machines.  

Each of the following $n-1$ lines contains three space-separated integers, $city1,\ city2$, and $time$.  There is a bidirectional road connecting $city1$ and $city2$, and to destroy this road it takes $time$ units.

Each of the last $k$ lines contains an integer, $machine[i]$, the label of a city with a machine.   


## Output Format

Return an integer representing the minimum time required to disrupt the connections among all machines.


## Constraints

- $2 \le n \le 10^5$  
- $2 \le k \le n$  
- $1 \le time[i] \le 10^6$  


## Sample Input

5 3
2 1 8
1 0 5
2 4 5
1 3 4
2
4
0

## Explanation

The machines are located at the cities ,  and . Neo can destroy the green roads resulting in a time of .  Destroying the road between cities  and  instead of between  and  would work, but it's not minimal.
