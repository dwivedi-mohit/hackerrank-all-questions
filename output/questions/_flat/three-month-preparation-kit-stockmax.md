# Stock Maximize

---

| Field | Value |
|---|---|
| **Slug** | `three-month-preparation-kit-stockmax` |
| **Domain** |  |
| **Difficulty** | Medium |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/three-month-preparation-kit-stockmax |

---

## Preview

Your algorithms have become so good at predicting the market
 that can predict the share price of Wooden Orange Toothpicks
 Inc.

## Problem Statement

Your algorithms have become so good at predicting the market that you now know what the share price of Wooden Orange Toothpicks Inc. (WOT) will be for the next number of days.

Each day, you can either buy one share of WOT, sell any number of shares of WOT that you own, or not make any transaction at all. What is the maximum profit you can obtain with an optimum trading strategy?

**Example**

$prices=[1,2]$


Buy one share day one, and sell it day two for a profit of $1$. Return $1$. 

$prices=[2, 1]$ 


No profit can be made so you do not buy or sell stock those days. Return $0$.

**Function Description**


Complete the *stockmax* function in the editor below.


stockmax has the following parameter(s):


- *prices*: an array of integers that represent predicted daily stock prices  


**Returns** 


- *int:*  the maximum profit achievable

## Input Format

The first line contains the number of test cases $t$.

Each of the next $t$ pairs of lines contain:

- The first line contains an integer $n$, the number of predicted prices for WOT.

- The next line contains n space-separated integers $prices[i]$, each a predicted stock price for day $i$.

## Output Format

Output $t$ lines, each containing the maximum profit which can be obtained for the corresponding test case.

## Constraints

+ $1 \le t \le 10$

+ $1 \le n \le 50000$
+ $1 \le prices[i] \le 100000$

## Sample Tests

### Test 1

```
STDIN Function
----- --------
3 q = 3
3 prices[] size n = 3
5 3 2 prices = [5, 3, 2]
3 prices[] size n = 3
1 2 100 prices = [1, 2, 100]
4 prices[] size n = 4
1 3 1 2 prices =[1, 3, 1, 2]
```

### Test 2

```
0
197
3
```
