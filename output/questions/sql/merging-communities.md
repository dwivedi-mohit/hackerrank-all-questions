# Merging Communities 

- **Domain:** sql
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.8304825901038485
- **Total Submissions:** 19644
- **Solved Count:** 16314
- **URL:** https://www.hackerrank.com/challenges/merging-communities

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

## Constraints

   

## Sample Input

STDIN   Function
-----   --------
3 6     n = 3, q = 6
Q 1     print the size of the community containing person 1
M 1 2   merge the communities containing persons 1 and 2 ...
Q 2
M 2 3
Q 3
Q 2

## Sample Output

2
3
3

## Explanation

Initial size of each of the community is .
