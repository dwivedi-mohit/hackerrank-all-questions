# Journey to the Moon

---

| Field | Value |
|---|---|
| **Slug** | `journey-to-the-moon` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/journey-to-the-moon |

---

## Preview

Compute in how many ways we can pick a pair of astronauts belonging to different countries

## Problem Statement

The member states of the UN are planning to send $2$ people to the moon. They want them to be from different countries.  You will be given a list of pairs of astronaut ID's.  Each pair is made of astronauts from the same country.  Determine how many pairs of astronauts from different countries they can choose from.

__Example__


$n = 4$

$astronaut = [1, 2], [2, 3]$ 


There are $4$ astronauts numbered $0$ through $3$.  Astronauts grouped by country are $[0]$ and $[1, 2, 3]$.  There are $3$ pairs to choose from: $[0,1], [0,2]$ and $[0,3]$.

**Function Description**


Complete the *journeyToMoon* function in the editor below.  


journeyToMoon has the following parameter(s):


- *int n:* the number of astronauts

- *int astronaut[p][2]:* each element $astronaut[i]$ is a $2$ element array that represents the ID's of two astronauts from the same country


**Returns**

- *int:* the number of valid pairs

## Input Format

The first line contains two integers $n$ and $p$, the number of astronauts and the number of pairs.

Each of the next $p$ lines contains $2$ space-separated integers denoting astronaut ID's of two who share the same nationality.

## Constraints

* $1 \le n \le 10^5$

* $1 \le p \le 10^4$

## Sample Tests

### Test 1

```
5 3
0 1
2 3
0 4
```

### Test 2

```
6
```

### Test 3

```
4 1
0 2
```

### Test 4

```
5
```
