# Journey Scheduling

---

| Field | Value |
|---|---|
| **Slug** | `journey-scheduling` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 75 |
| **URL** | https://www.hackerrank.com/challenges/journey-scheduling |

---

## Preview

Help Fedya to find the distance he'll travel in his journey.

## Problem Statement

Fedya is a seasoned traveller and is planning his trip to Treeland. Treeland is a country with an ancient road system which is in the form of a tree structure. $N$ cities of Treeland are numbered by $N$ positive integers: $1, 2, 3, ..., N$.

Fedya has not yet decided the starting point (city) of his journey and the cities he will visit. But there are a few things you know about Fedya's trip:

- Fedya is fond of travelling to great distances. So if he is currently located in city $V$, his destination will be a city which is most distant from city $V$.

- There might be more than 1 such cities. In that case, Fedya will choose a city that was already visited as less times as possible in this journey.

- There still might be more than 1 such cities. In that case, Fedya will go to the city with the smallest number.

Fedya has prepared a list of $M$ possible journeys. Each one is characterized by two integers - the starting city $V$ and the total number of cities to be visited, $K$. For each of them, he is keen to know the total distance travelled by him.

## Input Format

The first line of input will contain two space separated integers $N$ and $M$ - the number of cities and the number of possible journeys.

Then, there will be $(N-1)$ lines, each of them will contain two space separated integers $X$ $Y$, denoting the bi-directional road between the cities with numbers $X$ and $Y$ with the unitary length.

Then there will be $M$ lines, each of them will have two space separated integers $V$ and $K$, denoting a journey.


**Constraints**

$1 \leq N, M \leq 10^5$<br>
$1 \leq V, X, Y \leq N$<br>
$1 \leq K \leq 10^9$

## Output Format

For each journey, output the travelled distance on a separate line.

## Sample Tests

### Test 1

```
8 7
2 1
3 2
4 2
5 1
6 1
7 1
8 7
4 6
3 4
6 3
7 6
4 6
7 1
2 6
```

### Test 2

```
24
16
11
23
24
3
23
```
