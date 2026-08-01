# Sorted Subsegments

- **Domain:** sql
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.5158211065936008
- **Total Submissions:** 5657
- **Solved Count:** 2918
- **URL:** https://www.hackerrank.com/challenges/sorted-subsegments

## Problem Statement

Consider an array $A = [a_0, a_1, \ldots, a_{n-1}]$ of $n$ integers. We perform $q$ queries of the following type on $A$:

- Sort all the elements in the subsegment $a_{l_i}, a_{l_i + 1}, \ldots, a_{r_i}$.

Given $A$, can you find and print the value at index $k$ (where $0 \le k \lt n$) after performing $q$ queries?

## Input Format

The first line contains three positive space-separated integers describing the respective values of $n$ (the number of integers in $A$), $q$ (the number of queries), and $k$ (an index in $A$).		
The next line contains $n$ space-separated integers describing the respective values of $a_0, a_1, \ldots, a_{n-1}$.		
Each line $j$ of the $q$ subsequent lines contain two space-separated integers describing the respective $l_j$ and $r_j$ values for query $j$.

## Output Format

Print a single integer denoting the value of $a_k$ after processing all $q$ queries.

**Sample Input 0**

    3 1 1
    3 2 1
    0 1

**Sample Output 0**

    3
    
**Explanation 0**

$A = [3, 2, 1]$		
There is only one query to perform. When we sort the subarray ranging from index $0$ to index $1$, we get $A' = [2, 3, 1]$. We then print the element at index $1$, which is $3$. 

**Sample Input 1**

    4 2 0
    4 3 2 1
    0 2
    1 3

**Sample Output 1**

	2 
    
**Explanation 1**		

$A = [4, 3, 2, 1]$		
There are $q=2$ queries:

1. When we sort the subarray ranging from index $0$ to index $2$, we get $A' = [2, 3, 4, 1]$. 
2. When we sort the subarray of $A'$ from index $1$ to index $3$, we get $A'' = [2, 1, 3, 4]$.

Having performed all of the queries, we print the element at index $0$, which is $2$.

## Constraints

- $1 \le n, q \le 75000$
- $0 \le k \le n - 1$
- $-10^9 \le a_i \le 10^9$
- $0 \le l_i \le r_i < n$

## Sample Input

3 1 1
3 2 1
0 1

## Sample Output

3

## Explanation

There is only one query to perform. When we sort the subarray ranging from index  to index , we get . We then print the element at index , which is .
