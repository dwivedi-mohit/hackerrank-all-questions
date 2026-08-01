# Dynamic Array

- **Domain:** mathematics
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.8812721804032656
- **Total Submissions:** 251348
- **Solved Count:** 221506
- **URL:** https://www.hackerrank.com/challenges/dynamic-array

## Problem Statement

- Declare a 2-dimensional array, $arr$, with $n$ empty arrays, all zero-indexed.
- Declare an integer, $lastAnswer$, and initialize it to 0.

You need to process two types of queries:

1. Query: $1\ x\ y$
   - Compute $idx = (x \oplus lastAnswer) % n$.
   - Append the integer $y$ to $arr[idx]$.

2. Query: $2\ x\ y$
   - Compute $idx = (x \oplus lastAnswer) % n$.
   - Set $lastAnswer = arr[idx][y \% size(arr[idx])]$.
   - Store the new value of $lastAnswer$ in an answers array.

**Notes:**  
- $\oplus$ is the *bitwise XOR* operation, which corresponds to the `^` operator in most languages. Learn more about it on [Wikipedia](https://en.wikipedia.org/wiki/Exclusive_or).  
- $\%$ is the modulo operator.   
- Finally, $size(arr[idx])$ is the number of elements in $arr[idx]$.  

**Function Description**  

Complete the $dynamicArray$ function with the following parameters:  
- $int\ n$: the number of empty arrays to initialize in $arr$  
- $int\ queries[q][3]$: 2-D array of integers

**Returns**  

- $int[]$:  the results of each type 2 query in the order they are presented  

## Input Format

The first line contains two space-separated integers, $n$, the size of $arr$ to create, and $q$, the number of queries, respectively.		
Each of the $q$ subsequent lines contains a query string, $queries[i]$.

## Constraints

- $1 \leq  n, q \leq  10^5$
- $0 \leq x, y \leq 10^9$
- It is guaranteed that query type $2$ will never query an empty array or index.

## Sample Input

STDIN    Function
-----    --------
2 5      size of arr[] n = 2, size of queries[] q = 5
1 0 5    queries = [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]
1 1 7
1 0 3
2 1 0
2 1 1

## Sample Output

3

## Explanation

Initial Values:

 = [ ]

 = [ ]

Query 0: Append  to .

 = [5]

 = [ ]

Query 1: Append  to .

 = [5]

 = [7]

Query 2: Append  to .

 = [5, 3]

 = [7]

Query 3: Assign the value at index  of  to . Store  in your answer array.

 = [5, 3]

 = [7]

Query 4: Assign the value at index  of  to . Store  in your answer array.

 = [5, 3]

 = [7]

Return your answer array [7, 3]. The code stub prints its elements on separate lines.
