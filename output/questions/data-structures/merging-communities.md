# Merging Communities 

---

| Field | Value |
|---|---|
| **Slug** | `merging-communities` |
| **Domain** | data-structures |
| **Difficulty** | Hard |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/merging-communities |

---

## Preview

Given N groups, answer two types of queries: merge two groups or print the group to which a person belongs to.

## Problem Statement

People connect with each other in a social network. A connection between Person $i$ and Person $j$ is represented as $\text{M i j}$. When two persons belonging to different communities connect, the net effect is the merge the communities which $i$ and $j$ belong to. 

At the beginning, there are $n$ people representing $n$ communities. Suppose person $1$ and $2$ connected and later $2$ and $3$ connected, then $1$,$2$, and $3$ will belong to the same community.

There are two types of queries:

1. $\text{M i j} \implies$ communities containing persons $i$ and $j$ are merged if they belong to different communities.

2. $\text{Q i} \implies$ print the size of the community to which person $i$ belongs.

## Input Format

The first line of input contains 2 space-separated integers $n$ and $q$, the number of people and the number of queries. 

The next $q$ lines will contain the queries. 


**Constraints** 


$1 \le n \le 10^5$ 

$1 \le q \le 2 \times 10^5$

## Output Format

The output of the queries.

## Sample Tests

### Test 1

```
1
2
3
3
```
