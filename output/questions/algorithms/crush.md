# Array Manipulation

- **Domain:** algorithms
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.6475277404255756
- **Total Submissions:** 487105
- **Solved Count:** 315414
- **URL:** https://www.hackerrank.com/challenges/crush

## Problem Statement

Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each array element between two given indices, inclusive.  Once all operations have been performed, return the maximum value in the array.  

**Example**  
$n = 10$  
$queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]$  

Queries are interpreted as follows:  
```
    a b k
    1 5 3
    4 8 7
    6 9 1
```

Add the values of $k$ between the indices $a$ and $b$ inclusive:


![image](https://s3.amazonaws.com/hr-assets/0/1738699658-ff37fa31d8-array_manipulation_example.png)

The largest value is $10$ after all operations are performed.  

**Function Description**  

Complete the function $arrayManipulation$ with the following parameters:

- $int\ n$: the number of elements in the array  
- $int\ queries[q][3]$: a two dimensional array of queries where each $queries[i]$ contains three integers, $a$, $b$, and $k$.  

**Returns**  

- $int$: the maximum value in the resultant array  

## Input Format

The first line contains two space-separated integers $n$ and $q$, the size of the array and the number of queries.  
Each of the next $q$ lines contains three space-separated integers $a$, $b$ and $k$, the left index, right index and number to add.  

## Constraints

- $3 \le n \le 10^{7}$  
- $1 \le m \le 2 * 10^{5} $  
- $1 \le a \le b \le n   $  
- $0 \le k \le 10^{9}  $  


## Sample Input

STDIN       Function
-----       --------
5 3         arr[] size n = 5, queries[] size q = 3
1 2 100     queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
2 5 100
3 4 100

## Explanation

After the first update the list is 100 100 0 0 0.

After the second update list is 100 200 100 100 100.

After the third update list is 100 200 200 200 100.

The maximum value is .
