# Minimum Loss

- **Domain:** data-structures
- **Difficulty:** Medium
- **Max Score:** 35
- **Success Ratio:** 0.6688055486336074
- **Total Submissions:** 48156
- **Solved Count:** 32207
- **URL:** https://www.hackerrank.com/challenges/minimum-loss

## Problem Statement

Lauren has a chart of distinct projected prices for a house over the next several years.  She must buy the house in one year and sell it in another, and she must do so at a loss.  She wants to minimize her financial loss.  

**Example**   
$price = [20, 15, 8, 2, 12]$   

Her minimum loss is incurred by purchasing in year $2$ at $price[1]=15$ and reselling in year $5$ at $price[4]=12$.  Return $15 - 12 = 3$.  

**Function Description**  

Complete the *minimumLoss* function in the editor below.   

minimumLoss has the following parameter(s):  

- *int price[n]:* home prices at each year  

**Returns**   

- *int:* the minimum loss possible  

## Input Format

The first line contains an integer $n$, the number of years of house data. 		
The second line contains $n$ space-separated long integers that describe each $price[i]$.

## Constraints

* $2\le n \le 2 \times 10^5$
* $ 1 \le price[i] \le 10^{16} $
* All the prices are distinct. 
* A valid answer exists.

**Subtasks**

* $2 \le n \le 1000$ for $50\%$ of the maximum score. 

## Sample Input

3
5 10 3

## Sample Output

2

## Explanation

Lauren buys the house in year  at  and sells it in year  at  for a minimal loss of .
