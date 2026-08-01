# Food Delivery Service

- **Domain:** mathematics
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.20081967213114754
- **Total Submissions:** 244
- **Solved Count:** 49
- **URL:** https://www.hackerrank.com/challenges/food-delivery-service

## Problem Statement

Atul has started working as a food delivery executive for Swiggy and he needs to deliver food in a magical place called Swiggy-City where houses are numbered from $1$ to $N$. Atul starts from house number 1.  From any house number $u$ he can move to house number $v$ such that.

- $v = u + 1$ or $v = u - 1$  
- $v = u * 2$ or $v = u / 2$  
- The number $v$ can be achieved by sorting the digits of number $u$ in descending order. 

Note that $v$ should be a whole number and within boundaries during any time ($1 \leq v \leq N$). 

Since Atul is stressed out and wants to deliver as many food packets as possible, please help him to get to the house number $X$ from house number $1$ using a minimum number of operations.  

## Input Format

First line contains a single integer $T$, denoting the number of tests. 

Next $T$ lines contain two integers $N$ and $X$, denoting the number of houses in Swiggy-City and the house number Atul wants to reach. 

## Output Format

Output $T$ lines containing a single integer which is the answer for each test. 

## Constraints

- $1 \leq T \leq 5$
- $1 \leq N \leq 10^6$
- $1 \leq X \leq N$

## Sample Input

1
100 61

## Sample Output

5

## Explanation

Atul can reach house number  from house number  in the following order: . So the answer is .
