# Queries with Fixed Length

- **Domain:** databases
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.8160676532769556
- **Total Submissions:** 1419
- **Solved Count:** 1158
- **URL:** https://www.hackerrank.com/challenges/three-month-preparation-kit-queries-with-fixed-length

## Problem Statement

Consider an $n$-integer sequence, $A = \{a_0, a_1, \ldots, a_{n-1} \}$. We perform a query on $A$ by using an integer, $d$, to calculate the result of the following expression:

$$\huge{\min_{\Large{0 \le i \le n-d}} ( \max_{\Large{i \le j \lt i + d}} a_j )}$$

In other words, if we let $m_i = \max(a_i, a_{i+1}, a_{i+2}, \ldots, a_{i+d-1})$, then you need to calculate $\min(m_0, m_1, \ldots, m_{n-d})$.  

Given $arr$ and $q$ queries, return a list of answers to each query.

**Example**   
$arr = [2, 3, 4, 5, 6]$   
$queries = [2, 3]$  

The first query uses all of the subarrays of length $2$:  $[2, 3], [3, 4], [4, 5], [5, 6]$.  The maxima of the subarrays are $[3, 4, 5, 6]$.  The minimum of these is $3$.  

The second query uses all of the subarrays of length $3$: $[2, 3, 4], [3, 4, 5], [4, 5, 6]$.  The maxima of the subarrays are $[4, 5, 6]$.  The minimum of these is $4$.  

Return $[3, 4]$.  

**Function Description**   

Complete the *solve* function below.  

*solve* has the following parameter(s):  

- *int arr[n]:* an array of integers  
- *int queries[q]:* the lengths of subarrays to query  

**Returns**  

- *int[q]:* the answers to each query   


## Input Format

The first line consists of two space-separated integers, $n$ and $q$. 	
The second line consists of $n$ space-separated integers, the elements of $arr$.		
Each of the $q$ subsequent lines contains a single integer denoting the value of $d$ for that query. 

## Constraints

- $1 \leq n \leq 10^5$
- $0 \leq arr[i] \lt 10^6$
- $1 \leq q \leq 100$
- $1 \leq d \leq n$

## Sample Input

5 5
1 2 3 4 5
1
2
3
4
5

## Sample Output

2
3
4
5

## Explanation

Each prefix has the least maximum value among the consecutive subsequences of the same size.
