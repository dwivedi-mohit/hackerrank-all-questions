# Grand Tour

---

| Field | Value |
|---|---|
| **Slug** | `grand-tour` |
| **Domain** | misc |
| **Difficulty** | Advanced |
| **Score** | 100 |
| **Contest** | 101hack24 |
| **URL** | https://www.hackerrank.com/challenges/grand-tour |

---

## Preview

Help Bidhan plan his tour.

## Problem Statement

Mary wants to tour the world. There are $N$ different locations she considers worth visiting. She has collected details of $N$ flights which connect these $N$ locations either directly or indirectly.

Out of these $N$ cities, she has shortlisted $M$ cities and wants to visit these cities in a specific order, if she likes the city a lot, she lists it multiple times indicating her lover for the city and her willingness for sightseeing in the same city multiple times.


She starts at the first city listed in $M$ and sightsees the city. She then continues to the next city in the list ( she can cut down the travel time by using any other city as transit city). If the next city in the list is the same as the current city she is in, she chooses to sightsee the same city again before travelling to the next city in the list $M$.


As travelling from one city to another takes time, what is the minimum amount of time taken by Mary to visit all cities in the list $M$?

## Input Format

The first line of input contains $N$, the number of locations.

The second line contains $N$ space-separated integers, the $i^{th}$ of which denoting the time required to sightsee the $i^{th}$ place.

Each of the next $N$ lines contains three space-separated integers, $S$, $E$, and $T$ indicating that there is flight between city $S$ and city $E$ which runs in both directions and takes $T$ time.

The next line contains $M$, the number of locations in Mary's tour list.

The next line contains $M$ space-separated integers denoting the place she wants to visit in that order ( the first city being the city from which she starts her tour)

**Constraints**

$1 \le N, M \le 10^5$

$1 \le S, E \le N$

$1 \le travel\_time \le 10^3$

$0 \le sightseeing\_time \le 10^3$

## Output Format

Output the time taken for Mary to complete the tour.

## Sample Tests

### Test 1

```
3
2 9 5
2 3 11
3 1 3
1 2 8
4
3 1 1 3
```

### Test 2

```
20
```

### Test 3

```
5 + 3 + 2 + 2 + 3 + 5 = 20
```
