# Real Estate Broker

---

| Field | Value |
|---|---|
| **Slug** | `real-estate-broker` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/real-estate-broker |

---

## Preview

Sell as many houses as is possible!

## Problem Statement

You are a real estate broker in ancient Knossos. You have $m$ unsold houses, and each house $j$ has an area, $x_j$, and a minimum price, $y_j$. You also have $n$ clients, and each client $i$ wants a house with an area greater than $a_i$ and a price less than or equal to $p_i$.

Each client can buy *at most* one house, and each house can have *at most* one owner. What is the maximum number of houses you can sell?

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of clients) and $m$ (the number of houses). 		
Each line $i$ of the $n$ subsequent lines contains two space-separated integers describing the respective values of $a_i$ and $p_i$ for client $i$.		
Each line $j$ of the $m$ subsequent lines contains two space-separated integers describing the respective values of $x_j$ and $y_j$ for house $j$.

## Output Format

Print a single integer denoting the maximum number of houses you can sell.

## Constraints

* $ 1 \le n,m \le 1000 $
* $ 1 \le a_i, p_i \le 10^9 $, where $0 \le i \lt n$.
* $ 1 \le x_j, y_j \le 10^9 $, where $0 \le j \lt m$.

## Sample Tests

### Test 1

```
3 3
5 110
9 500
20 400
10 100
2 200
30 300
```

### Test 2

```
2
```
