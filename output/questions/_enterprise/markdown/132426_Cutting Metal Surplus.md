# Cutting Metal Surplus

## Metadata

- **ID:** 132426
- **Type:** code
- **Difficulty:** 10.0
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Data Structures, Medium, Algorithms, Arrays, Problem Solving
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, data structures, and algorithms concepts, ideal for mid-level roles. The task requires determining the optimal rod length to maximize profit from cutting metal rods while considering cutting costs and sale prices.

## Problem Statement

Cut metal rods in such a way that the profit is maximal.

A construction company owner has surplus metal rods of arbitrary lengths. A contractor will buy rods of the same exact integer length (saleLength). Rods can be cut to increase the number of sellable rods, but each cut costs costPerCut. Any leftover rods not matching saleLength are discarded.

 

The total profit is calculated as:

    totalProfit = totalUniformRods × saleLength × salePrice − totalCuts × costPerCut

 

Find the saleLength that maximizes profit.

 

Example

lengths = [30, 59, 110]

costPerCut = 1

salePrice = 10

 

Testing two possible lengths:

For saleLength = 30:

	
- Rod 30: No cuts needed → 1 piece
	
- Rod 59: Cut off 29 units (1 cut) → 1 piece
	
- Rod 110: Cut off 20 units + 2 more cuts → 3 pieces
	
- Total: 5 pieces, 4 cuts
	
- Revenue = (10 × 5 × 30) - (4 × 1) = 1496

For saleLength = 5:

	
- Rod 30: 5 cuts → 6 pieces
	
- Rod 59: Cut off 4 units (1 cut) + 10 more cuts → 11 pieces
	
- Rod 110: 21 cuts → 22 pieces
	
- Total: 39 pieces, 37 cuts
	
- Revenue = (10 × 39 × 5) - (37 × 1) = 1913

Testing shows that using saleLength = 5 yields the maximum profit.

 

Function Description

Complete the function maxProfit in the editor with the following parameter(s):

    int costPerCut:  cost to make a cut

    int salePrice:  per unit length sales price

    int lengths[n]: rod lengths

 

Returns

    int: the maximum possible profit

 

Constraints

	
- 1 ≤ n ≤ 50
	
- 1 ≤ lengths[i] ≤ 104

	
- 1 ≤ salePrice, costPerCut ≤ 1000

 

 DO NOT REMOVE THIS LINE-->

Input Format for Custom Testing

The first line contains an integer, costPerCut.

The second line contains an integer, salePrice.

The next line contains an integer n, the size of the array lengths.

Each of the next n lines contains an integer lengths[i] where 0 ≤ i < n.

Sample Case 0

Sample Input

STDIN     Function
-----     -----
1      →  costPerCut = 1
10     →  salePrice = 10
3      →  lengths[] size n = 3
26     →  lengths = [26, 103, 59] 
103
59
```

 

Sample Output

1770
```

 

Explanation

Since costPerCut = 1 is very inexpensive, a large number of cuts can be made to reduce the number of wasted pieces. The optimal rod length for maximizing profit is 6, and the rods are cut as shown:

	
- 
`lengths[0] = 26`: Cut off a piece of length 2 and discard it, resulting in a rod of length 24. Then, cut this rod into 4 pieces of length 6.
	
- 
`lengths[1] = 103`: Cut off a piece of length 1 and discard it, resulting in a rod of length 102. Then, cut this rod into 17 pieces of length 6.
	
- 
`lengths[2] = 59`: Cut off a piece of length 5 and discard it, resulting in a rod of length 54. Then, cut this rod into 9 pieces of length 6.

 

After performing totalCuts = (1 + 3) + (1 + 16) + (1 + 8) = 30 cuts, there are totalUniformRods = 4 + 17 + 9 = 30 pieces of length saleLength = 6 that can be sold at salePrice = 10. This yields a total profit of salePrice × totalUniformRods × saleLength − totalCuts × costPerCut = 10 × 30 × 6 − 30 × 1 = 1770.

 

Sample Case 1

Sample Input

STDIN     Function
-----     -----
100    →  costPerCut = 100
10     →  salePrice = 10
3      →  lengths[] size n = 3
26     →  lengths = [26, 103, 59]
103
59
```

 

Sample Output

1230
```

 

Explanation

Since costPerCut = 100, cuts are expensive and must be minimal. The optimal rod length for maximizing profit is 51, and the rods are cut as shown:

	
- 
`lengths[0] = 26`: Discard this rod entirely.
	
- 
`lengths[1] = 103`: Cut off a piece of length 1 and discard it, resulting in a rod of length 102. Then, cut this rod into 2 pieces of length 51.
	
- 
`lengths[2] = 59`: Cut off a piece of length 8 and discard it, resulting in a rod of length 51.

 

After performing totalCuts = (0) + (1 + 1) + (1) = 3 cuts, there are totalUniformRods = 0 + 2 + 1 = 3 pieces of length saleLength = 51 that can be sold at salePrice = 10 each. This yields a total profit of salePrice × totalUniformRods × saleLength − totalCuts × costPerCut = 10 × 3 × 51 − 3 × 100 = 1230.

## Sample Input/Output

## Preview

Cut metal rods in such a way that the profit is maximal.
