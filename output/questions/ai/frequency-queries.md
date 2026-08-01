# Frequency Queries

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.6634720552721918
- **Total Submissions:** 92343
- **Solved Count:** 61267
- **URL:** https://www.hackerrank.com/challenges/frequency-queries

## Problem Statement

You are given $q$ queries. Each query is of the form two integers described below:  
- $1$ $x$: Insert x in your data structure.   
- $2$ $y$: Delete one occurence of y from your data structure, if present.  
- $3$ $z$: Check if any integer is present whose frequency is exactly $z$. If yes, print 1 else 0.

The queries are given in the form of a 2-D array $queries$ of size $q$ where $queries[i][0]$ contains the operation, and $queries[i][1]$ contains the data element.   

**Example**    
$queries = [(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)]$   

The results of each operation are:  

	Operation	Array	Output
    (1,1)		[1]
    (2,2)		[1]
    (3,2)					0
    (1,1)		[1,1]
    (1,1)		[1,1,1]
    (2,1)		[1,1]
    (3,2)					1
    
 Return an array with the output: $[0,1]$.
 
 **Function Description**
 
Complete the *freqQuery* function in the editor below.   

freqQuery has the following parameter(s):

- *int queries[q][2]:* a 2-d array of integers  

**Returns**   
- *int[]:* the results of queries of type $3$

## Input Format

The first line contains of an integer $q$, the number of queries.   
Each of the next $q$ lines contains two space-separated integers, $queries[i][0]$ and $queries[i][1]$.  

## Output Format

  

## Constraints

- $1 \leq q \leq 10^{5}$  
- $1 \leq x,y,z \leq 10^{9}$  
- All $queries[i][0] \in \{1,2,3\}$  
- $1 \leq queries[i][1] \leq 10^{9}$  

## Sample Input

8
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2

## Sample Output

0
1

## Explanation

For the first query of type , there is no integer whose frequency is  (). So answer is .

For the second query of type , there are two integers in  whose frequency is  (integers =  and ). So, the answer is .
