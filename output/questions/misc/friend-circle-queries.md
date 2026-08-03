# Friend Circle Queries

---

| Field | Value |
|---|---|
| **Slug** | `friend-circle-queries` |
| **Domain** |  |
| **Difficulty** | Medium |
| **Score** | 45 |
| **URL** | https://www.hackerrank.com/challenges/friend-circle-queries |

---

## Preview

Process the queries and after each query print the number of people largest friend circle.

## Problem Statement

The population of HackerWorld is $10^{9}$. Initially, none of the people are friends with each other. In order to start a friendship, two persons $a$ and $b$ have to shake hands, where $1 \leq a, b \leq 10^{9}$. The friendship relation is transitive, that is if $a$ and $b$ shake hands with each other, $a$ and friends of $a$ become friends with $b$ and friends of $b$.     



You will be given $q$ queries. After each query, you need to report the size of the largest friend circle (the largest group of friends) formed after considering that query.

  

For example, your list of queries is:


    1 2
    3 4
    2 3
  

First, $1$ and $2$ shake hands, forming a circle of $2$.  Next, $3$ and $4$ do the same.  Now there are two groups of $2$ friends.  When $2$ and $3$ become friends in the next query, both groups of friends are added together to make a circle of $4$ friends.  We would print

    2
    2
    4
  

**Function Description**

Complete the function *maxCircle* in the editor below.  It must return an array of integers representing the size of the maximum circle of friends after each query.



maxCircle has the following parameter(s):

-  *queries*: an array of integer arrays, each with two elements indicating a new friendship

## Input Format

The first line contains an integer, $q$, the number of queries to process.  

Each of the next $q$ lines consists of two space-separated integers denoting the 2-D array $queries$.

## Output Format

Return an integer array of size $q$, whose value at index $i$ is the size of largest group present after processing the $i^{th}$ query.

## Constraints

- $1 \leq q \leq 10^{5}$

- $1 \leq queries[i][0], queries[i][1]\leq 10^{9}$ for $0 \leq i \lt q$
- $queries[i][0] \neq queries[i][1]$

## Sample Tests

### Test 1

```
1 2
3 4
2 3
```

### Test 2

```
2
2
4
```

### Test 3

```
2
1 2
1 3
```

### Test 4

```
2
3
```

### Test 5

```
4
1000000000 23
11 3778
7 47
11 1000000000
```

### Test 6

```
2
2
2
4
```

### Test 7

```
6
1 2
3 4
1 3
5 7
5 6
7 4
```

### Test 8

```
2
2
4
4
4
7
```

### Test 9

```
1 [1,2]
2 [1,2],[3,4]
3 [1,2,3,4]
4 [1,2,3,4],[5,7]
5 [1,2,3,4],[5,7,6]
6 [1,2,3,4,5,6,7]
```
