# Direct Connections

---

| Field | Value |
|---|---|
| **Slug** | `direct-connections` |
| **Domain** | data-structures |
| **Difficulty** | Hard |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/direct-connections |

---

## Preview

In the land of EV, they want to be well-connected. For each person in a city, there should be a cable from that city to every other city. Find the total length of cable needed.

## Problem Statement

Enter-View $(EV)$ is a linear, street-like country. By linear, we mean all the cities of the country are placed on a single straight line - the $x$-axis. Thus every city's position can be defined by a single coordinate, $x_i$, the distance from the left borderline of the country. You can treat all cities as single points.

Unfortunately, the dictator of telecommunication of EV (Mr. S. Treat Jr.) doesn't know anything about the modern telecom technologies, except for peer-to-peer connections. Even worse, his thoughts on peer-to-peer connections are extremely faulty: he believes that, if $P_{i}$ people are living in city $i$, there must be at least $P_{i}$ cables from city $i$ to every other city of EV - this way he can guarantee no congestion will ever occur!

Mr. Treat hires you to find out how much cable they need to implement this telecommunication system, given the coordination of the cities and their respective population. 

Note that The connections between the cities can be shared. Look at the example for the detailed explanation.

**Input Format**


A number $T$ is given in the first line and then comes $T$ blocks, each representing a scenario.

Each scenario consists of three lines. The first line indicates the number of cities (<i>N</i>). The second line indicates the coordinates of the <i>N</i> cities. The third line contains the population of each of the cities. The cities needn't be in increasing order in the input.

**Output Format**


For each scenario of the input, write the length of cable needed in a single line modulo $1,000,000,007$.

**Constraints**


$1 ≤ T ≤ 20$

$1 ≤ N ≤ 200,000$

$P_{i} ≤ 10,000$

Border to border length of the country $≤  1,000,000,000$

**Sample Input**


    2

    3

    1 3 6

    10 20 30

    5

    5 55 555 55555 555555

    3333 333 333 33 35

**Sample Output**


    280

    463055586

## Sample Tests

### Test 1

```
2 
3 
1 3 6 
10 20 30 
5 
5 55 555 55555 555555 
3333 333 333 33 35
```

### Test 2

```
280 
463055586
```
