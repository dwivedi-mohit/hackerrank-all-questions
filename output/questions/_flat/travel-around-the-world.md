# Travel around the world

---

| Field | Value |
|---|---|
| **Slug** | `travel-around-the-world` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 120 |
| **URL** | https://www.hackerrank.com/challenges/travel-around-the-world |

---

## Preview

Generalized TSP, counting total number of staring point for the journey so that fuel is sufficient to complete the journey

## Problem Statement

There are N cities and N directed roads in Steven's world. The cities are numbered from 0 to N - 1. Steven can travel from city *i* to city *(i + 1) % N*, ( 0-> 1 -> 2 -> .... -> N - 1 -> 0). 

Steven wants to travel around the world by car. The capacity of his car's fuel tank is C gallons. There are a[i] gallons he can use at the beginning of city *i* and the car takes b[i] gallons to travel from city *i* to *(i + 1) % N*.

 
How many cities can Steven start his car from so that he can travel around the world and reach the same city he started? 

**Note**


The fuel tank is initially empty.

## Input Format

The first line contains two integers (separated by a space): city number *N* and capacity *C*.

The second line contains *N* space-separated integers: a[0], a[1], … , a[N - 1].

The third line contains *N* space-separated integers: b[0], b[1], … , b[N - 1].

## Output Format

The number of cities which can be chosen as the start city.

## Constraints

2 &le; N &le; 10<sup>5</sup>  

1 &le; C &le; 10<sup>18</sup>

0 &le; a[i], b[i] &le; 10<sup>9</sup>

## Sample Tests

### Test 1

```
3 3
3 1 2
2 2 2
```

### Test 2

```
2
```
