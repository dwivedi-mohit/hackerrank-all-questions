# Savita And Friends

---

| Field | Value |
|---|---|
| **Slug** | `savita-and-friends` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 90 |
| **URL** | https://www.hackerrank.com/challenges/savita-and-friends |

---

## Preview

Savita and Friends are meeting after a long time. Help Savita to organize the meeting.

## Problem Statement

After completing her final semester, Savita is back home. She is excited to meet all her friends. Her $N$ friends live in different houses spread across the city.  


There are $M$ roads connecting the houses. The road network formed is connected and does not contain self loops and multiple roads between same pair of houses. Savita and Friends decide to meet.


Savita wants to choose a point(not necessarily an integer) $P$ on the road numbered $K$, such that, the maximum of $dist(i)$ for all $1 \leq i \leq N$ is minimised,

where $dist(i)$ is the shortest distance between the $i$'<sup>th</sup> friend and $P$.  


If $K$'th road connects friend $A$ and friend $B$ you should print distance of chosen point from $A$. Also, print the $max(dist(i))$ for all $1 \leq i \leq N$. If there is more than one solution, print the one in which the point $P$ is closest to $A$.   


Note: 

+ Use scanf/printf instead of cin/cout. Large input files.
+ Order of $A$ and $B$ as given in the input must be maintained. If P is at a distance of 8 from $A$ and 2 from $B$, you should print 8 and not 2.

## Input Format

First line contain $T$, the number of testcases. 

T testcases follow.

First Line of each testcase contains 3 space separated integers $N, M, K$ .

Next $M$ lines contain description of the $i$<sup>th</sup> road : three space separated integers $A, B, C$, where $C$ is the length of road connecting $A$ and $B$.

## Output Format

For each testcase, print two space separated values in one line. The first value is the distance of $P$ from the point $A$ and the second value is the maximum of all the possible shortest paths between $P$ and all of Savita's and her friends' houses. Round both answers to $5$ decimal digits and print exactly $5$ digits after the decimal point.

## Constraints

$1 \leq T \leq 10$  

$2 \leq N, M \leq 10^{5}$  

$N-1 \leq M \leq N*(N-1)/2$   

$1 \leq A, B \leq N$   

$1 \leq C \leq 10^9$  

$1 \leq K \leq M$

## Sample Tests

### Test 1

```
2
2 1 1
1 2 10
4 4 1
1 2 10
2 3 10
3 4 1
4 1 5
```

### Test 2

```
5.00000 5.00000
2.00000 8.00000
```
