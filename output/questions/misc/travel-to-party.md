# Travel to Party

---

| Field | Value |
|---|---|
| **Slug** | `travel-to-party` |
| **Domain** | misc |
| **Difficulty** | Expert |
| **Score** | 85 |
| **Contest** | 101hack54 |
| **URL** | https://www.hackerrank.com/challenges/travel-to-party |

---

## Preview

Help friends make a cool party.

## Problem Statement

<!-- image: illustrate the layout of the cities in the sample -->
There are numerous cities in a country Treeland, and the first of these cities is the *capital*. The cities are connected by bus routes, such that for each city $i \neq 1$, there is a bus that goes from this city to city $p_i$ ($p_i < i$), *exactly in this direction*. 

The country has a definite number of national dishes. Each city has a special dish, so this and only this dish can be bought there. Every city's special dish is one of the types of the national dishes.

Some friends from several cities are meeting in one city for a party. They choose a city such that if they start to travel to this city simultaneously, they will meet as soon as it possible. Traveling by bus takes one unit of time.

They want to buy some dishes for the party following some requirements:

1. Each friend must buy an equal amount of dishes.
2. There must be no two same types of dishes in the party.
3. Each friend can buy only those types of dishes that correspond to the cities he/she visited.

For each given query, you should calculate the maximum possible number of dishes in the party.
Complete the function `maximumDishes` which takes in three integers and prints the answer for each query in a line.

## Input Format

The first line contains three space-separated integers $n$, $m$ and $q$, denoting: 

- $n$ - number of cities 
- $m$ - number of types of national dishes
- $q$ - number of queries 

The second line contains $n - 1$ space-separated integers $p_2$, ..., $p_n$, denoting the bus routes.     


The third line contains $n$ space-separated integers $a_1$, ..., $a_n$, denoting the special dish in every city.

The following lines describe the queries. Each query is given in the following format: integer $c$, denoting the number of friends, and then $c$ space-separated integers $v_1$, ..., $v_c$, denoting the cities the friends are originally located in.

*All arrays are $1$-indexed.*

## Output Format

Print $q$ lines. The $i^\text{th}$ line should contain a single integer denoting the answer on the $i^\text{th}$ query.

## Constraints

- $2 \leq n \leq 3 \cdot 10 ^ 5$
- $1 \leq m \leq 1000$
- $1 \leq q \leq 5 \cdot 10 ^ 4$
- $1 \leq p_i < i$
- $1 \leq a_i \leq m$
- $2 \leq c \leq 5$
- $1 \leq v_i \leq n$

It is **not** guaranteed that $v_i$ are different for one particular query.

Additionally, for $24\%$ of the total points:

- $n, q \leq 3000$
- $c = 2$

## Sample Tests

### Test 1

```
5 3 4
1 2 2 1
2 3 1 3 1
2 3 4
3 5 2 2
4 3 4 2 5
2 2 2
```

### Test 2

```
2
3
0
0
```

### Test 3

```
11 6 3
1 2 2 4 5 4 5 8 9 4
5 6 1 1 2 3 2 3 4 5 2
3 3 10 8
4 6 5 10 10
2 9 6
```

### Test 4

```
6
4
2
```
