# Counting Road Networks

- **Domain:** data-structures
- **Difficulty:** Expert
- **Max Score:** 90
- **Success Ratio:** 0.7919010123734533
- **Total Submissions:** 1778
- **Solved Count:** 1408
- **URL:** https://www.hackerrank.com/challenges/counting-road-networks

## Problem Statement

Lukas is a Civil Engineer who loves designing road networks to connect $n$ cities numbered from $1$ to $n$. He can build any number of bidirectional roads as long as the resultant network satisfies these constraints:

1. It must be possible to reach any city from any other city by traveling along the network of roads.  
2. No two roads can directly connect the same two cities.   
3. A road cannot directly connect a city to itself.  

In other words, the roads and cities must form a simple connected labeled graph.

You must answer $q$ queries, where each query consists of some $n$ denoting the number of cities Lukas wants to design a bidirectional network of roads for. For each query, find and print the number of ways he can build roads connecting $n$ cities on a new line; as the number of ways can be quite large, print it modulo $663224321$.

## Input Format

The first line contains an integer, $q$, denoting the number of queries.  	
Each of the $q$ subsequent lines contains an integer denoting the value of $n$ for a query.

## Output Format

For each of the $q$ queries, print the number of ways Lukas can build a network of bidirectional roads connecting $n$ cities, modulo $663224321$, on a new line.

## Constraints

+ $1 \le q, n \le 10^5$

## Sample Input

3
1
3
10

## Sample Output

1
4
201986643

## Explanation

We answer the first two queries like this:

- When , the only option satisfying Lukas' three constraints is to not build any roads at all. Thus, we print the result of  on a new line.

- When , there are four ways for Lukas to build roads that satisfy his three constraints:

Thus, we print the result of  on a new line.
