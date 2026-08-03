# Voting

---

| Field | Value |
|---|---|
| **Slug** | `voting-1` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 20 |
| **Contest** | 101hack30 |
| **URL** | https://www.hackerrank.com/challenges/voting-1 |

---

## Preview

Find the winner in the elections.

## Problem Statement

It’s election time in Byteland. $M$ citizens casted one vote for one person. To win the election, a candidate must earn more votes than half of the total number of voters. 

**Challenge:** Who won the election? It’s guaranteed that, for the given input, there will always be a winner.

## Input Format

The first line of input contains a single integer $M$, denoting the number of citizens.

The $i$<sup>th</sup> line of the following $M$ lines contains a lowercase English letter string, denoting the candidate who gets the vote of the $i$<sup>th</sup> citizen.

**Constraints**

- $1 \leq M \leq 10^3$
- Each name consists of $1$ to $10$ lowercase English letters.
- Citizens can only vote for existing candidates.

## Output Format

First and only line of output: the name (in lowercase English letters) of the winning candidate.

## Sample Tests

### Test 1

```
5
jack
john
jake
john
john
```

### Test 2

```
john
```
