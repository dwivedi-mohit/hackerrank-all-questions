# Highway Construction

- **Domain:** databases
- **Difficulty:** Hard
- **Max Score:** 75
- **Success Ratio:** 0.7016129032258065
- **Total Submissions:** 124
- **Solved Count:** 87
- **URL:** https://www.hackerrank.com/challenges/highway-construction

## Problem Statement

You are planning the next FIFA World Cup and you are counting the number of highways that need to be built to connect the cities with the venue.  
Your country has $n$ cities and all cities lie on a single straight road called “Highway Road”. If you want to go from City $x$ to City $y$ ( where $x \leq y$ ), you need to go through city $x, x+1, x+2, \cdots , y-1, y$. 

The requirements for the highways are as follows:

1. All games will be held in the $n^{th}$ city.
2. New bidirectional roads, called _"Super Highways"_, need to be built such that it is possible to visit the $n^{th}$ city from any other city directly.  

You also have the cost to fulfil the second condition. The engineering team knows that if the length of a Super Highway is $l$, then it will cost $l^k$, where $k$ is an integer constant.The length of Super Highway between city $x$ and $y$ is $|x-y|$.  

For this problem, you need to find only a rough estimation of the cost, hence, find Total Cost Modulo $1000000009$. 



## Input Format

First line will contain a single positive integer $q$ denoting the number of queries. Then for each case there will be two positive integers, $n$ and $k$.


## Output Format

For each case find the cost to build Super Highways such that it is possible to visit $n^{th}$ city from any other city directly. You have to print this value Modulo $1000000009$.


## Constraints

+ $1 \leq q \leq 200$  
+ $1 \leq n \leq 10^{18}$  
+ $1 \leq k \leq 1000$

## Sample Input

1
4 2

## Sample Output

13

## Explanation

There are four cities. We need to build Super Highways that connect city  to city  and city  to city . No need to connect city 3 with city  since they are adjacent on “Highway Road”. So cost is .
