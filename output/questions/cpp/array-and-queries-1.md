# Array and Queries

- **Domain:** cpp
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.47897727272727275
- **Total Submissions:** 1760
- **Solved Count:** 843
- **URL:** https://www.hackerrank.com/challenges/array-and-queries-1

## Problem Statement

Given an array, you are asked to perform a number of queries and divide the array into what are called, _beautiful_ subsequences. 

The array $A$ has length $n$. A function $f(A)$  is defined to be a minimal possible $x$, such that it's possible to divide array $A$ into $x$ _beautiful_ subsequences. Note that each element of an array should belong to exactly one subsequence, and subsequence does not necessarily need to be consecutive.   

A subsequence $S$ with length $len$ is called *beautiful* if and only if:  

- $len = 1$ or  
- Let $S'$ be a sorted version of $S$. It must hold that $S'_{i} = S'_{i + 1} - 1$ for every $i \in [1, len - 1].$  

For instance, if $A = [1, 2, 3, 4, 3, 5]$, $f(A)$ would be $2$. Because, you can divide $A$ into $2$ _beautiful_ subsequences either like $[1, 2, 3]$ and $[4, 3, 5]$ or like $[1, 2, 3, 4, 5]$ and $[3]$.  

You have to answer $q$ queries. Each query is of the type:  

- $id$  $val$: you need to change a value of $A_{id}$ to $val$, i.e. $A_{id} = val$. Here $id$ is $1-indexed$.  

After each query, for the value of $f(A)$, lets denote that value as $ans_i$, where $i$ indicates the $i^{th}$ query.  

You need to find $\sum\limits_{i=1}^{q} i \times ans_i$ modulo $(10^9 + 7)$.


## Input Format

The first line contains a single integer $n$, representing the length of array $A$.  
The next line contains the array $A$ given as space-separated integers.  
The next line contains a single integer $q$, representing the number of queries.  
Each of the $q$ lines contain two integers $id$ and $val$, which is described above.  

## Output Format

Print the required answer in one line.  

## Constraints

- $1 \le n, q \le 3 \times 10^5$  
- $1 \le A_i \le 10^9$  
- $1 \le id \le n$  
- $1 \le val \le 10^9$  

## Sample Input

5
2 2 1 1 1
2
3 2
5 5

## Sample Output

11

## Explanation

The initial array  is

- After  query the array becomes  this can be divided into  subsequences as ,  and .

- After  query the array becomes  this can be divided into  subsequences as , ,  and .

Hence, calculating  we get
