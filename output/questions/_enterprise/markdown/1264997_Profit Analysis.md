# Profit Analysis

## Metadata

- **ID:** 1264997
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Dynamic Programming, Heaps, Queues
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates dynamic programming, heaps, and queues concepts, ideal for mid-level roles. The problem requires finding the maximum net profit from a contiguous segment of monthly profits and losses, constrained by a maximum length of k months.

## Problem Statement

You need to analyze the performance of investments in a stock. The profit and loss (PnL) for each month is represented in an array where each value indicates the profit earned (positive value) or loss incurred (negative value) in that month.

 

Your task is to find the maximum net profit that can be gained from any contiguous segment of months, with the constraint that the segment cannot exceed a given number of months k.

 

Example

n = 6

pnl = [-3, 4, 3, -2, 2, 5]

k = 4

 

The optimal subarray is [3, -2, 2, 5] with a total profit of 3 + (-2) + 2 + 5 = 8. While the subarray [4, 3, -2, 2, 5] has a higher profit of 12, its length exceeds the constraint k = 4.

 

The answer is 8.

 

Function Description

Complete the function getMaxProfit in the editor with the following parameters:

    pnl[n]: monthly profits and losses

    k: maximum number of months to consider

 

Returns

    long_int: the sum of a contiguous subarray of size k or less that has the largest sum

 

Constraints

	
- 1 ≤ n ≤ 2 * 105

	
- -109 ≤ pnl[i] ≤ 109

	
- 1 ≤ k ≤ n

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, denoting the number of elements in pnl.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer denoting pnl[i].

The last line contains an integer, k.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
7        →    pnl[] size n = 7
4        →    pnl = [4, 3, -2, 9, -4, 2, 7]
3
-2
9
-4
2
7
6        →    k = 6
```

Sample Output

15
```

Explanation

 

We can select the subarray [3, -2, 9, -4, 2, 7] with a sum of 15 and size 6, which is equal to k.

Sample Case 1

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
8        →    pnl[] size n = 8  
2        →    pnl = [2, 5, -7, 8, -6, 4, 1, -9]
5
-7
8
-6
4
1
-9
5        →    k = 5
```

Sample Output

8
```

Explanation

We can select the subarray [2, 5, -7, 8] with a sum of 8 and size 4, which is less than k.

## Sample Input/Output

## Preview

You need to analyze the performance of investments in a stock. The profit and
