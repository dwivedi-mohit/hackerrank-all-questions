# Kingdom Connectivity

- **Domain:** java
- **Difficulty:** Hard
- **Max Score:** 75
- **Success Ratio:** 0.6655259365994236
- **Total Submissions:** 5552
- **Solved Count:** 3695
- **URL:** https://www.hackerrank.com/challenges/kingdom-connectivity

## Problem Statement

It has been a prosperous year for King Charles and he is rapidly expanding his empire. In fact, he recently invaded his neighboring country and set up a new kingdom! This kingdom has many cities connected by **one-way roads.** To ensure higher connectivity, two cities are sometimes directly linked by more than one road.

In the new kingdom, King Charles has made one of the cities his financial capital and another city his warfare capital. He wants a better connectivity between these two capitals. The connectivity of a pair of cities, $a$ and $b$, is defined as the number of different paths from city $a$ to city $b$. A path may use a road more than once if possible. Two paths are considered different if they do not use the same sequence of roads the same number of times.

There are $n$ cities numbered $1$ to $n$ in the new kingdom and $m$ **one-way roads**. City $1$ is the financial capital and city $n$ is the warfare capital.  Determine the number of different paths between cities $1$ and $n$. Since the number may be large, print the result modulo $10^9$ or $1000000000$.   

**Note:** Two roads may connect the same cities, but they are still considered distinct for path connections. 

For example, there are $n = 5$ cities connected by $m = 6$ roads as shown in the following graph:

![image](https://s3.amazonaws.com/hr-assets/0/1544118885-4df6f8d3d2-kingdomconnectionsexample.png)  

There are two direct paths and one cyclic path.  Direct paths are $1 \rightarrow 2 \rightarrow 4 \rightarrow 5$ and $1 \rightarrow 2 \rightarrow 3$ and $1 \rightarrow 2 \rightarrow 4 \rightarrow 5$.  The cycle $3 \leftrightarrow 4$ can be repeated any number of times, so there are infinite paths.  If the connection $4 \rightarrow 3$ did not exist, there would be only the two direct paths.

**Function Description**

Complete the *countPaths* function in the editor below.  It should print your result, modulo $10^9$ if there are limited paths or `INFINITE PATHS` if they are unlimited. There is no expected return value.   

countPaths has the following parameters:  
- *n*: the integer number of cities  
- *edges*: a 2D integer array where $edges[i][0]$ is the source city and $edges[i][1]$ is the destination city for the directed road $i$   


## Input Format

The first line contains two integers $n$ and $m$.  
Each of the following $m$ lines contains two space-separated integers that represent source and destination cities for a directed connection.


## Output Format

Print the number of different paths from city $1$ to city $n$ modulo $10^9$. If there are infinitely many different paths, print `INFINITE PATHS`.
 

## Constraints

* $2 \le n \le 10^4$  
* $1 \le m \le 10^5$   
* $1 \le edges[i][0], edges[i][1] \le n$  

## Sample Output

2

## Explanation

There are two possible paths from city  to city :
