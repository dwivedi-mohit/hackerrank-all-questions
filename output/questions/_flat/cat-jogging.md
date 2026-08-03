# Jogging Cats

---

| Field | Value |
|---|---|
| **Slug** | `cat-jogging` |
| **Domain** | algorithms |
| **Difficulty** | Advanced |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/cat-jogging |

---

## Preview

Find the number of unique paths Big and Little Cat can go jogging on.

## Problem Statement

It's almost summertime, so Big Cat and Little Cat are getting in shape. They decide the core of their fitness plan is to start jogging every day.

Their city consists of $N$ intersections connected by $M$ bidirectional roads. The cats decide that their jogging route should be cyclic (i.e., starting and ending at the same intersection) and consist of $4$ different roads.

The cats also love exploring new places, so each day they want to choose a new route to jog on that is not equal to any of their previous routes. Two routes are considered to be equal if their sets of component roads are equal.

Given a map of the city, can you help our heroic cats determine the maximum number of days they can go jogging so that every route traveled is different?

## Input Format

The first line contains a pair of space-separated integers, $N$ (the number of intersections) and $M$ (the number of roads), respectively.

Each line $i$ of the $M$ subsequent lines contains a pair of space-separated integers, $X_i$ and $Y_i$, defining a bidirectional road connecting intersections $X_i$ and $Y_i$.

## Output Format

Print the maximum number of days for which the cats can go jogging without repeating a route.

## Constraints

* $1 \leq N \leq 5 \cdot 10^4$
* $1 \leq M \leq 10^5$
* $1 \leq X_i, Y_i \leq N$
* Each bidirectional road connects $2$ distinct intersections (i.e., no road connects an intersection to itself).
* Each pair of intersections is directly connected by no more than $1$ road.

## Sample Tests

### Test 1

```
4 6
1 2
2 3
3 4
4 1
1 3
2 4
```

### Test 2

```
3
```
