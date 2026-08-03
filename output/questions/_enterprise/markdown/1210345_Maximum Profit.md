# Maximum Profit

## Metadata

- **ID:** 1210345
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Greedy Algorithms, Medium
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, greedy algorithms, and sorting concepts, ideal for mid-level roles. The task is to determine the maximum profit from selling items based on their categories and prices in an optimal order.

## Problem Statement

A shop owner has n items for sale, with each item having:

	
- A unique number from 1 to n

	
- A category designated by category[i]

	
- A selling price of price[i]

The profit from selling an item is calculated as: - price[i] × (number of different categories sold up to and including that item)

 

Determine the maximum possible total profit by arranging the items in the optimal selling order.

 

Example

Consider n = 4, category = [3, 1, 2, 3] and price = [2, 1, 4, 4].

One optimal order is:

	
- First, sell the 2nd item; category[2] = 1, price[2] = 1, number of different categories sold = 1, so profit = 1 * 1 = 1
	
- Then, sell the 1st item; category[1] = 3, price[1] = 2, number of different categories sold = 2, so profit = 2 * 2 = 4
	
- Then, sell the 3rd item; category[3] = 2, price[3] = 4, number of different categories sold = 3, so profit = 4 * 3 = 12
	
- Then, sell the 4th item; category[4] = 3, price[4] = 4, number of different categories sold = 3, so profit = 4 * 3 = 12

Thus, total profit = 1 + 4 + 12 + 12 = 29.

 

Function Description

Complete the function findMaximumProfit in the editor with the following parameters:

    int category[n]: the categories of the items

    int price[n]: the prices of the items

 

Returns

    long_int: the maximum possible total profit

 

Constraints

	
- 1 ≤ n ≤ 105

	
- 1 ≤ category[i] ≤ 109

	
- 1 ≤ price[i] ≤ 109

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, the number of elements in category.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, category[i].

The next line contains an integer, n, the number of elements in price.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, price[i].

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
3        →    category[] size n = 3
2        →    category = [2, 1, 2]
1 
2 
3        →    price[] size n = 3 
3        →    price = [3, 2, 4]
2 
4 
```

Sample Output

16
```

Explanation

 

An optimal order:

	
- First, sell the 2nd item; category[2] = 1, price[2] = 2, number of different categories sold = 1, so profit = 2 * 1 = 2
	
- Then, sell the 1st item; category[1] = 2, price[1] = 3, number of different categories sold = 2, so profit = 3 * 2 = 6
	
- Then, sell the 3rd item; category[3] = 2, price[3] = 4, number of different categories sold = 2, so profit = 4 * 2 = 8

Total profit = 2 + 6 + 8 = 16.

Sample Case 1

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
4        →    category[] size n = 4 
3        →    category = [3, 2, 2, 3] 
2 
2 
3 
4        →    price[] size n = 4 
2        →    price = [2, 7, 3, 4] 
7 
3 
4

```

Sample Output

30
```

Explanation

An optimal order:

	
- First, sell the 1st item; category[1] = 3, price[1] = 2, number of different categories sold = 1, so profit = 2 * 1 = 2
	
- Then, sell the 3rd item; category[3] = 2, price[3] = 3, number of different categories sold = 2, so profit = 3 * 2 = 6
	
- Then, sell the 2nd item; category[2] = 2, price[2] = 7, number of different categories sold = 2, so profit = 7 * 2 = 14
	
- Then, sell the 4th item; category[4] = 3, price[4] = 4, number of different categories sold = 2, so profit = 4 * 2 = 8

Total profit = 2 + 6 + 14 + 8 = 30.

## Sample Input/Output

## Preview

A shop owner has n items for sale, with each item having:
