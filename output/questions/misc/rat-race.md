# Rat Race

---

| Field | Value |
|---|---|
| **Slug** | `rat-race` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 20 |
| **Contest** | 101hack24 |
| **URL** | https://www.hackerrank.com/challenges/rat-race |

---

## Preview

Help Bidhan predict the outcome of a rat race.

## Problem Statement

$N$ rats are put in a rate race. Distance of different rats from the finishing line may be different. Two different rats' speed may be different from each other. Each rat's speed doesn't change.


Given distance and speed of each rat, tell us which of the rats win the race.

## Input Format

The first line of input contains $N$, the number of participating rats.

The next line contains $N$ space-separated integers where the $i^{th}$ integer denotes the speed of the $i^{th}$ rat.

The next line contains $N$ space-separated integers where the $i^{th}$ integer denotes the distance of the $i^{th}$ rat from the finishing line.

**Contraints**

$1 \le N \le 100$

$1 \le$ _Speed, Distance_ $\le 100$

**Note**


Time taken by a rat to complete race can be in fractions.

## Output Format

Print the number of each rat that will win the race in a separate line. The number of the rats is determined by their order in input ($1$ being the number of the $1^{st}$ rat in input, $2$ being the number of the $2^{nd}$ rat, and so on).

## Sample Tests

### Test 1

```
3
2 5 1
4 10 3
```

### Test 2

```
1
2
```
