# Selecting Stocks

## Metadata

- **ID:** 617315
- **Type:** code
- **Difficulty:** 15.555555555555555
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Hard, Dynamic Programming, Algorithms, Problem Solving, Interviewer Guidelines
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates dynamic programming, algorithms, and problem-solving concepts, ideal for senior-level roles. The problem requires determining the maximum profit an investor can earn by selecting the optimal combination of stocks within their budget.

## Problem Statement

An investor with limited funds wants to invest in the stock market. They can buy at most one share of each company and cannot exceed their available funds. The future values of the stocks after one year have been predicted.

 

Your task is to determine the maximum profit the investor can earn by selecting the optimal combination of stocks to buy.

 

Example

Available funds: saving = 250

Current stock values: currentValue = [175, 133, 109, 210, 97]

Predicted future values: future_value =[200, 125, 128, 228, 133]

 

Optimal investment strategy:

	
- Buy stocks at indices 2 and 4, with values 109 and 97
	
- Total investment: 109 + 97 = 206
	
- Future value: 128 + 133 = 261
	
- Profit: 261 - 206 = 55

Therefore, the maximum possible profit is 55.

 

Function Description

Complete the function selectStock in the editor with the following parameter(s):

    int saving:  amount available for investment

    int currentValue[n]:  the current stock values

    int futureValue[n]:  the values of the stocks after one year

 

Returns

    int: the maximum profit after one year

Constraints

	
- 0 < n ≤ 100
	
- 0 < saving ≤ 30000
	
- 0 ≤ currrentValue[i], futureValue[i]  ≤ 300

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, the number of elements in currrentValue.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, currrentValue[i].

The next line contains an integer, n, the number of elements in futureValue.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, futureValue[i].

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN    Function
-----    --------
30    →  saving = 30
4     →  currentValue[] size n = 4
1     →  currentValue = [1, 2, 4, 6]
2
4
6
4     →  futureValue[] size n = 4
5     →  futureValue = ]5, 3, 5, 6]
3
5
6

```

Sample Output

6
```

Explanation

The investor can buy all 4 stocks and gain a profit of (5-1)+(3-2)+(5-4)+(6-6) = 4+2+1+0 = 6.

Sample Case 1

Sample Input For Custom Testing

STDIN    Function
-----    --------
500   →  saving = 500
5     →  currentValue[] size n = 5
150   →  currentValue = [150, 199, 200, 168, 153]
199
200
168
153
5     →  futureValue[] size n = 5
140   →  futureValue = [140, 175, 199, 121, 111]
175
199
121
111

```

Sample Output

0
```

Explanation

All the stocks lose value during the year, so no investment is made. There is no way to make a profit.

## Sample Input/Output

## Preview

An investor with limited funds wants to invest in the stock market. They can bu
