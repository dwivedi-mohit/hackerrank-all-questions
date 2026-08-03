# C: Diagonal Sum

## Metadata

- **ID:** 1192693
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Dynamic Memory Allocation, Arrays, Pointers, Medium
- **Skills:** C (Intermediate)
- **Languages:** c

## Summary

This coding question evaluates dynamic memory allocation, arrays, and pointers concepts, ideal for mid-level roles. The problem requires implementing functions to allocate a matrix, take input, and calculate the sums of both diagonals.

## Problem Statement

For a given n × n matrix, implement the following functions:

	
- 
allocate_memory: Dynamically allocate an n × n matrix.
	
- 
take_input: Assign values to the allocated matrix.
	
- 
first_diagonal_sum: Calculate the sum of the first diagonal (from top left to bottom right) and return it as an integer.
	
- 
second_diagonal_sum: Calculate the sum of the second diagonal (from top right to bottom left) and return it as an integer.

Example

[ [1 2], [3 4] ]

 

as a matrix:

1 2
3 4

```

 

The first diagonal is 1 4. Its sum is 5.

The second diagonal is 2 3. Its sum is 5.

 

Constraints

	
- 2 ≤ n ≤ 50
	
- 1 ≤ matrix[i][j] ≤ 103

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains a single integer n.

The next n lines each contain n space-separated integers.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

3
1 4 3 
5 5 6 
7 8 10

```

 

Sample Output

16 15
```

Explanation

The sum of the first diagonal is (1 + 5+ 10) = 16 and the sum of the second diagonal is ( 3 + 5 + 7) = 15.

Sample Case 1

Sample Input For Custom Testing

4 
1 5 1 2 
3 2 1 4 
1 2 3 4 
8 4 10 5
```

Sample Output

11 13
```

Explanation

The sum of the first diagonal is (1 + 2 + 3+ 5) = 11 and the sum of the second diagonal is ( 2 + 1 + 2 + 8) = 13.

## Sample Input/Output

## Preview

For a given n × n matrix, implement the following functions:
