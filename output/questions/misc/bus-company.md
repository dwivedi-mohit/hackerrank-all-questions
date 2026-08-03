# Bus Company

---

| Field | Value |
|---|---|
| **Slug** | `bus-company` |
| **Domain** | misc |
| **Difficulty** | Advanced |
| **Score** | 120 |
| **Contest** | 101hack28 |
| **URL** | https://www.hackerrank.com/challenges/bus-company |

---

## Preview

You are given a bus route with $m$ stations and $n$ potential passengers. You have one bus with $k$ places. For each passenger you know the starting station, the ending station, and the number of coins they will give you if you drive them to ending station. How many coins can you earn at most?

## Problem Statement

Everybody knows how much money a bus company can earn. Mika and Zloba decided to earn some extra money. So they started a new bus company.

Now they have only one bus with $k$ seats. The bus is moving along a route containing $m$ stations. All of the $m$ stations are arranged in a line and numbered from $1$ to $m$. The bus starts its journey from station $1$ and stops at station $m$.

A total of $n$ passengers want to be driven by this bus. For each passenger you are given two numbers: its starting station and its ending station, the $i$<sup>$th$</sup> passenger starts trip at the station $a_i$ and ends it at the station $b_i$ ($a_i < b_i$). Passenger can only enter the bus at its starting station and must leave it at its ending station. For this drive, every passenger wants to pay some amount of coins. If the bus picks up the $i$<sup>$th$</sup> passenger, the company will receive $c_i$ coins. Passengers are strange people (everybody wants exactly one seat), so it is possible that the bus can't pick up all the passengers. Mika and Zloba are doing their best; they want to earn as much money as possible.

Help our heroes and find the maximum amount of coins they can earn.

**Input Format**<br>

The first line contains three numbers $n$, $m$, and $k$ ($1 \leq n,k \leq 100, 2 \leq m \leq 100$), the number of passengers, the number of stations on the route, and the number of seats on the bus, respectively.

Each of the next $n$ lines contains three numbers $a_i$, $b_i$, and $c_i$ ($1 \leq a_i < b_i \leq m, 1 \leq c_i \leq 100$), the starting station, the ending station, and the amount of coins which Mika and Zloba will earn for driving the $i$<sup>$th$</sup> passenger.


**Output Format**<br>

In the single line print one integer number - the maximum amount of coins which can be earned by Mika and Zloba.

**Sample Input 1:**<br>

    2 4 1
    1 4 2
    2 3 5
  

**Sample Output 1:**<br>

    5

**Sample Input 2:**<br>

    5 5 2
    1 2 2
    1 3 5
    1 4 3
    4 5 1
    2 4 4

**Sample Output 2:**<br>

    12

## Sample Tests

### Test 1

```
2 4 1
1 4 2
2 3 5
```

### Test 2

```
5
```

### Test 3

```
5 5 2
1 2 2
1 3 5
1 4 3
4 5 1
2 4 4
```

### Test 4

```
12
```
