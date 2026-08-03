# Happiness of a Kingdom

---

| Field | Value |
|---|---|
| **Slug** | `happiness` |
| **Contest** | codeagon-2017 |
| **Difficulty** | Hard |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/happiness |

---

## Problem Statement

Once upon a time, there was a kingdom called `Kekoland` that had $n$ towns connected by $m$ undirected roads. Each town had a single citizen inhabiting it. The happiness of each citizen was determined by the number of other citizens they could reach using the given roads. The happiness of the kingdom was the sum of all citizens' happiness.

After Kekoland's best days eventually, poverty arrived. As the roads required a lot of money for maintenance, the King `Keko the First` decided to close exactly $2$ of the roads.

`Keko the First` was a good king.  He wanted his kingdom to be as happy as possible, and he closed $2$ roads such that it maximized the happiness of the kingdom. After thousands of years, you find the map of Kekoland but it is a map of the kingdom prior to the road closure. You wonder how happy the kingdom was after the roads were closed. Find and print the maximum happiness of the kingdom after closing exactly $2$ roads. 

**Note:** All pairs of towns don't have to be reachable after closing the roads.

## Input Format

The first line contains two integers $n$ and $m$, denoting the number of towns and number of roads.  
Next $m$ lines contains two integers $x_i$ and $y_i$, meaning that there is a road between $x_i$ and $y_i$, $x_i \ne y_i$. Also, it is guaranteed that the same edge will not be given twice.

## Output Format

Print a single integer, maximum happiness after closing exactly 2 roads.

## Constraints

- $1 \leq n \leq 5 \times 10^5$
- $2 \leq m \leq 10^6$
- $1 ≤ x_i,\, y_i ≤ n$
