# Stock Market Prediction

## Metadata

- **ID:** 519243
- **Type:** code
- **Difficulty:** 8.055555555555555
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Data Structures, Problem Solving, Hard, Stacks, Algorithms, Theme:  Finance
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, data structures, and algorithms concepts, ideal for senior-level roles. The problem requires implementing a function to find the nearest day with a smaller stock price based on given queries.

## Problem Statement

In a prediction game, the first player gives the second player stock market data for consecutive days. Then:

	
- Player 1 tells player 2 a specific day number (1-based indexing).
	
- Player 2 must find the nearest day on which the stock price was smaller than the given day.
	
- If there are two equally near days with smaller prices, choose the earlier day.
	
- If no such day exists, the answer is -1.

 

Example

n = 10

stockData = [5, 6, 8, 4, 9, 10, 8, 3, 6, 4]

queries = [6, 5, 4]

 

     

For query day 6 (price 10):

	
- Days 5 and 7 both have smaller prices (9 and 8) and are both 1 day away.
	
- We choose day 5 because it is earlier.
	
- Answer: 5

For query day 5 (price 9):

	
- Day 4 has a smaller price (4) and is 1 day away.
	
- Answer: 4

For query day 4 (price 4):

	
- Day 8 has a smaller price (3) and is 4 days away.
	
- Answer: 8

The answer array is [5, 4, 8].

 

Function Description

 

Complete the predictAnswer function in the editor with the folowing parameters:

    int stockData[n]: the value of each stockData[i] is the stock price on the i+1th day (where 0 ≤ i < n).

    int queries[q]: the day number in the query

 

Return

    int[q]:  the value at each index i is the answer to queries[i]

 

Constraints

	
- 1 ≤ n ≤ 105

	
- 1 ≤ stockData[i] ≤ 109

	
- 1 ≤ q ≤ 105

	
- 1 ≤ queries[j] ≤ 109

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, denoting the number of elements in stockData.

Each line i of the n subsequent lines contains an integer, stockData[i], the stock price on the i+1th day.

Next line contains an integer, q, the number of elements in queries.

Each line j of the q subsequent lines contains an integer, queries[j], the day number of the jth query.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input 0

STDIN     Function
-----     --------
10   →    stockData[] size n = 10
5    →    stockData = [5, 6, 8, 4, 9, 10, 8, 3, 6, 4]
6
8
4
9
10
8
3
6
4 
3    →    queries[] size q = 3
3    →    queries = [3, 1, 8]
1
8

```

Sample Output 0

2
4
-1
```

Explanation 0

     

	
- If the day number is 3, both days 2 and 4 are smaller.  Choose the earlier day, day 2.
	
- If the day number is 1, day 4 is the closest day with a smaller price.
	
- If the day number is 8, there is no day where the price is less than 3.  The answer is -1.
	
- The return array is [2, 4, -1]

## Sample Input/Output

## Preview

In a prediction game, the first player gives the second player stock market da
