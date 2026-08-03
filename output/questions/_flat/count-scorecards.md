# Count Scorecards

---

| Field | Value |
|---|---|
| **Slug** | `count-scorecards` |
| **Domain** | algorithms |
| **Difficulty** | Expert |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/count-scorecards |

---

## Preview

How many ways are there to fill the scorecard so that it results into a valid tournament scorecard?

## Problem Statement

In a tournament, $n$ players play against each other exactly once. Each game results in exactly one player winning. There are no ties. You have been given a scorecard containing the scores of each player at the end of the tournament. The score of a player is the total number of games the player won in the tournament. However, the scores of some players might have been erased from the scorecard. How many possible scorecards are consistent with the input scorecard?

## Input Format

The first line contains a single integer $t$ denoting the number of test cases. $t$ test cases follow.


The first line of each test case contains a single integer $n$. The second line contains $n$ space-separated integers $s_1, s_2, \ldots, s_n$. $s_i$ denotes the score of the $i$th player. If the score of the $i$th player has been erased, it is represented by $-1$.

## Output Format

For each test case, output a single line containing the answer for that test case modulo $10^9 + 7$.

## Constraints

- $1 \le t \le 20$
- $1 \le n \le 40$
- $-1 \le s_i < n$

## Sample Tests

### Test 1

```
5
3
-1 -1 2
3
-1 -1 -1
4
0 1 2 3
2
1 1
4
-1 -1 -1 2
```

### Test 2

```
2
7
1
0
12
```
