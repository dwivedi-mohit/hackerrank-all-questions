# Poisonous Plants

---

| Field | Value |
|---|---|
| **Slug** | `poisonous-plants` |
| **Domain** | data-structures |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/poisonous-plants |

---

## Preview

Find the number of days after which all the plants die, given that a plant's pesticide value is greater than the one to it's left.

## Problem Statement

There are a number of plants in a garden. Each of the plants has been treated with some amount of pesticide. After each day, if any plant has more pesticide than the plant on its left, being weaker than the left one, it dies.



You are given the initial values of the pesticide in each of the plants. Determine the number of days after which no plant dies, i.e. the time after which there is no plant with more pesticide content than the plant to its left.



**Example**


$p = [3,6,2,7,5]$  // pesticide levels

Use a $1$-indexed array.  On day $1$, plants $2$ and $4$ die leaving $p' = [3,2,5]$.  On day $2$, plant $3$ in $p'$ dies leaving $p'' = [3,2]$.  There is no plant with a higher concentration of pesticide than the one to its left, so plants stop dying after day $2$.


**Function Description**

Complete the function *poisonousPlants* in the editor below.


poisonousPlants has the following parameter(s):

- *int p[n]*: the pesticide levels in each plant


Returns

- *int*: the number of days until plants no longer die from pesticide

## Input Format

The first line contains an integer $n$, the size of the array $p$.

The next line contains $n$ space-separated integers $p[i]$.

## Constraints

$1 \le n \le 10^5$

$0 \le p[i] \le 10^9$

## Sample Tests

### Test 1

```
7
6 5 8 4 7 10 9
```

### Test 2

```
2
```
