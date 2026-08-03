# Minimum Processing Time

## Metadata

- **ID:** 1587474
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Arrays, Dynamic Programming, Interviewer Guidelines
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates dynamic programming, arrays, and problem-solving concepts, ideal for mid-level roles. The problem requires determining the minimum processing time for data files by efficiently allocating them to two processors based on their processing times.

## Problem Statement

There are n data files where each contains a specific amount of data represented as data[i]. Each file must be processed using either Processor A or Processor B. Processor A takes processTimeA seconds to process a single unit of data, and Processor B requires processTimeB seconds.

 

Determine the minimum time needed to process all the data files by efficiently allocating them to the processors.

 

Example

n = 5

data = [4, 4, 6, 2, 5]

processTimeA = 3

processTimeB = 2

	
- Assign the first and second files to Processor A: 4 × 3 + 4 × 3 = 24 seconds
	
- Assign the third, fourth, and fifth files to Processor B: 6 × 2 + 2 × 2 + 5 × 2 = 26 seconds

The minimum total processing time is max(24, 26) = 26 seconds.

 

Function Description

Complete the function getMinProcessingTime in the editor with the following parameter(s):

    int data[n]: the data sizes within each file to be processed

    int processTimeA: the time taken by Processor A to process a single unit of data

    int processTimeB: the time taken by Processor B to process a single unit of data

 

Returns

    int: the minimum time for all the files to be processed

 

Constraints

	
- 1 ≤ n ≤ 100
	
- 1 ≤ data[i] ≤ 103

	
- 1 ≤ processTimeA, processTimeB ≤ 103

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer n, the size of data[].

Each of the next n lines contains an integer, data[i].

The next line contains an integer processTimeA.

The next line contains an integer processTimeB.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
4        →    data[] size n = 4
1        →    data = [1, 2, 3, 4]
2
3
4
2        →    processTimeA = 2
4        →    processTimeB = 4
```

Sample Output

14
```

Explanation

Assign the first and second files to processor B and the third and fourth files to processor A. Processor B runs for 1 × 4 + 2 × 4 = 12 seconds, while processor A runs for 3 × 2 + 4 × 2 = 6 + 8 = 14 seconds.

The result is max(12, 14) = 14 seconds.

Sample Case 1

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
6        →    data[] size n = 6
2        →    data = [2, 4, 8, 3, 6, 2]
4
8
3
6
2
3        →    processTimeA = 3
4        →    processTimeB = 4
```

Sample Output

44
```

Explanation

Assigning the first, second, and third files to processor A and the fourth, fifth, and sixth files to processor B. Processor A runs for 2 × 3 + 4 × 3 + 8 × 3 = 6 + 12 + 24 = 42 seconds, while processor B runs for 3 × 4 + 6 × 4 + 2 × 4 = 12 + 24 + 8 = 44 seconds.

The answer is max(42, 44) = 44 seconds.

## Sample Input/Output

## Preview

There are n data files where each contains a specific amount of data represent
