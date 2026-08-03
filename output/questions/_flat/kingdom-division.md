# Kingdom Division

---

| Field | Value |
|---|---|
| **Slug** | `kingdom-division` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/kingdom-division |

---

## Preview

Help King Arthur divide his kingdom between his two children.

## Problem Statement

King Arthur has a large kingdom that can be represented as a [tree](https://en.wikipedia.org/wiki/Tree_(graph_theory)), where nodes correspond to cities and edges correspond to the roads between cities. The kingdom has a total of $n$ cities numbered from $1$ to $n$. 

The King wants to divide his kingdom between his two children, Reggie and Betty, by giving each of them $0$ or more cities; however, they don't get along so he must divide the kingdom in such a way that they will not invade each other's cities. The first sibling will invade the second sibling's city if the second sibling has no other cities directly connected to it. For example, consider the kingdom configurations below:


![image](https://s3.amazonaws.com/hr-challenge-images/0/1485538883-b78be96095-kingdom13.png)

Given a map of the kingdom's $n$ cities, find and print the number of ways King Arthur can divide it between his two children such that they will not invade each other. As this answer can be quite large, it must be modulo $10^9+7$.

## Input Format

The first line contains a single integer denoting $n$ (the number of cities in the kingdom).		
Each of the $n-1$ subsequent lines contains two space-separated integers, $u$ and $v$, describing a road connecting cities $u$ and $v$.

## Output Format

Print the number of ways to divide the kingdom such that the siblings will not invade each other, modulo $10^9+7$.

## Constraints

* $2 \leq n \leq 10^5$
* $1 \leq u,v \leq n$
- It is guaranteed that all cities are connected.

**Subtasks**

* $2 \leq n \leq 20$ for $40\%$ of the maximum score.

## Sample Tests

### Test 1

```
5
1 2
1 3
3 4
3 5
```

### Test 2

```
4
```
