# Breaking the Records

---

| Field | Value |
|---|---|
| **Slug** | `breaking-best-and-worst-records` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/breaking-best-and-worst-records |

---

## Preview

Given an array of Maria's basketball scores all season, determine the number of times she breaks her best and worst records.

## Problem Statement

Maria plays college basketball and wants to go pro.  Each season she maintains a record of her play.  She tabulates the number of times she breaks her season record for *most points* and *least points* in a game.  Points scored in the first game establish her record for the season, and she begins counting from there.

**Example**

$scores = [12, 24, 10, 24]$ 


Scores are in the same order as the games played.  She tabulates her results as follows:

<pre>
									 Count
    Game  Score  Minimum  Maximum   Min Max
     0      12     12       12       0   0
     1      24     12       24       0   1
     2      10     10       24       1   1
     3      24     10       24       1   1
</pre>

Given the scores for a season, determine the number of times Maria breaks her records for *most* and *least* points scored during the season.

**Function Description**


Complete the *breakingRecords* function in the editor below. 

breakingRecords has the following parameter(s):


- *int scores[n]:* points scored per game 


**Returns** 


- *int[2]:* An array with the numbers of times she broke her records. Index $0$ is for breaking *most points* records, and index $1$ is for breaking *least points* records.

## Input Format

The first line contains an integer $n$, the number of games.  		
The second line contains $n$ space-separated integers describing the respective values of $score_0, score_1, \ldots, score_{n-1}$.

## Constraints

* $1 \le n \le 1000$
* $0 \le scores[i] \le 10^8$

## Sample Tests

### Test 1

```
Count
 Game Score Minimum Maximum Min Max
 0 12 12 12 0 0
 1 24 12 24 0 1
 2 10 10 24 1 1
 3 24 10 24 1 1
```

### Test 2

```
9
10 5 20 20 4 5 2 25 1
```

### Test 3

```
2 4
```

### Test 4

```
10
3 4 21 36 10 28 35 5 24 42
```

### Test 5

```
4 0
```
