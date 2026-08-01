# Mohit and Swiggy

- **Domain:** fp
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.11436950146627566
- **Total Submissions:** 341
- **Solved Count:** 39
- **URL:** https://www.hackerrank.com/challenges/mohit-and-swiggy

## Problem Statement

*Mohit* is a delivery executive of the company called *Swiggy*. *Swiggy* recently started batching orders, so *Mohit* needs to carry out orders from restaurants. 

There are $N$ junctions with its own restaurant in each and $M$ bidirectional roads. It's guaranteed that the graph is connected. *Mohit* is currently located at a collection booth which is denoted as a junction $0$ in the graph. He needs to visit all $N$ restaurants in some order according to the given rules and come back to the collection booth. 

Let's say Mohit is currently at junction $v$. He can go to the neighboring junction $u$ if **one of the following statements** is true:

- There is a road connecting $v$ and $u$, and Mohit haven't visited junction $u$ before. 
- Mohit arrived junction $v$ from junction $u$. It means he just goes back to where he came from. 

Your job is to calculate the minimum distance covered by Mohit. Note that Mohit has to finish his trip at the junction $0$ at the end. 


## Input Format

First line contains two integers $N$ and $M$ $-$ denoting the number of junctions and the number of roads, respectively. 

Next $M$ lines contain $u_i$, $v_i$, and $w_i$ $-$ denoting the road between $u_i$ and $v_i$ with distance $w_i$. It's guaranteed that $u_i \neq v_i$ and there are no two roads connecting the same pair of junctions. 

## Output Format

Output the answer.

## Constraints

- $1 \leq N \leq 5*10^5$
- $N \leq M \leq 10^6$
- $1 \leq X \leq N$
- $0 \leq u_i, v_i \leq N$ and $u_i \neq v_i$
- $1 \leq w_i \leq 2000$

## Sample Input

2 3
0 1 1
2 0 3
1 2 2

## Sample Output

6

## Explanation

First, Mohit goes to the  restaurant, then to the  restaurant. He then goes back to the collection booth by first going back to  restaurant, then to collection booth. So the answer would be .
