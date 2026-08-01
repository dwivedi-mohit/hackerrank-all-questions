# Variable Sized Arrays

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9409305770655175
- **Total Submissions:** 371275
- **Solved Count:** 349344
- **URL:** https://www.hackerrank.com/challenges/variable-sized-arrays

## Problem Statement

Consider an $n$-element array, $a$, where each index $i$ in the array contains a reference to an array of $k_i$ integers (where the value of $k_i$ varies from array to array). See the *Explanation* section below for a diagram.

Given $a$, you must answer $q$ queries. Each query is in the format `i j`, where $i$ denotes an index in array $a$ and $j$ denotes an index in the array located at $a[i]$. For each query, find and print the value of element $j$ in the array at location $a[i]$ on a new line.

Click [here](http://www.cplusplus.com/reference/vector/vector/) to know more about how to create variable sized arrays in C++.

## Input Format

The first line contains two space-separated integers denoting the respective values of $n$ (the number of variable-length arrays) and $q$ (the number of queries).	
Each line $i$ of the $n$ subsequent lines contains a space-separated sequence in the format <code>k a[i]<sub>0</sub> a[i]<sub>1</sub> &hellip; a[i]<sub>k-1</sub></code> describing the $k$-element array located at $a[i]$.		
Each of the $q$ subsequent lines contains two space-separated integers describing the respective values of $i$ (an index in array $a$) and $j$ (an index in the array referenced by $a[i]$) for a query.

## Output Format

For each pair of $i$ and $j$ values (i.e., for each query), print a single integer that denotes the element located at index $j$ of the array referenced by $a[i]$. There should be a total of $q$ lines of output.

## Constraints

- $1 \leq n \leq 10^5$
- $1 \leq q \leq 10^5$
- $1 \leq \ k \leq 3 \cdot 10^5$
- $n \leq \sum k \leq 3 \cdot 10^5$
- $0 \leq \ i < n$
- $0 \leq \ j < k$ 
- All indices in this challenge are zero-based.
- All the given numbers are non negative and are not greater than $10^6$

## Sample Input

2 2
3 1 5 4
5 1 2 8 9 3
0 1
1 3

## Sample Output

9

## Explanation

The diagram below depicts our assembled Sample Input:

We perform the following  queries:

- Find the array located at index , which corresponds to . We must print the value at index  of this array which, as you can see, is .

- Find the array located at index , which corresponds to . We must print the value at index  of this array which, as you can see, is .
