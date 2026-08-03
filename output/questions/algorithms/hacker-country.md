# Hacker Country

---

| Field | Value |
|---|---|
| **Slug** | `hacker-country` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/hacker-country |

---

## Preview

What is the minimum cost of a road trip in Hacker Country?

## Problem Statement

There are *N* cities in *Hacker Country*. Each pair of cities are directly connected by a unique directed road, and each road has its own toll that must be paid every time it is used. You're planning a road trip in *Hacker Country*, and its itinerary must satisfy the following conditions:


+ You can start in any city.
+ You must use $2$ or more different roads (meaning you will visit $2$ or more cities).
+ At the end of your trip, you should be back in your city of origin.
+ The average cost (sum of tolls paid per road traveled) should be minimum.

Can you calculate the *minimum average cost* of a trip in *Hacker Country*?

**Time Limits**

Time limits for this challenge are provided [here](https://www.hackerrank.com/environment).

## Input Format

The first line is an integer, $N$ (number of cities).

The $N$ subsequent lines of  $N$ space-separated integers each describe the respective tolls or traveling from city $i$ to city $j$; in other words, the $j^{th}$ integer of the $i^{th}$ line denotes the toll for traveling from city $i$ to city $j$.


**Note:** As there are no roads connecting a city to itself, the $i^{th}$ integer of line $i$ will always be $0$.

**Constraints**

$1 \lt N \leq 500$

$0 \lt toll \ cost \leq 200$

$roads \ traveled \geq 2$

## Output Format

Print the *minimum cost* as a rational number $p \ / \ q$ (tolls paid over roads traveled). The *greatest common divisor* of $p$ and $q$ should be $1$.

## Sample Tests

### Test 1

```
2
0 1
2 0
```

### Test 2

```
3/2
```
