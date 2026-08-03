# The Fundraising problem 

---

| Field | Value |
|---|---|
| **Slug** | `charity` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 30 |
| **Contest** | hack-the-interview-global |
| **URL** | https://www.hackerrank.com/challenges/charity |

---

## Preview

Maximum amount that can be collected by students from the guests in a charity event, if collection must be done under some constraints.

## Problem Statement

A university has organized a charity event to raise funds. Each guest has been secretly assigned a $generosity$ factor. The university students have been divided into $m$ groups of $n$ students each, to collect donations from the guests. Each student has a $charm$ factor. 

The rules of collecting donations from guests are as follows: 

1. Each table must be approached by exactly one group of students, but a particular group can approach more than one table.

2. Each guest must be approached by exactly one student once, but a student can approach more than one guest.

3. A student can approach at most $k$ guests throughout the duration of the event.

The donation collected by student $i$ from guest $j$ is $c[i]$ * $g[j]$, where $c[i]$ is the charm of the $ith$ student, and $g[j]$ is the generosity of the $jth$ guest.

Total donation collected by a student is the sum of donations collected by him/her from all guests he/she approached during the event. Total donation raised from the charity event is the sum of total donations collected by each individual student.

Find the maximum possible total donation that can be raised during the event.

## Input Format

The first line of input contains a single integer $tc$ denoting the number of test cases. Input format for each test case is given below.

- First line of each test case cotains three integers $m$, $n$ and $t$ denoting the number of groups, the number of students in each group, and the total number of tables for the guests respectively.
- The next $m$ lines represent a particular student group, and the $jth$ student in the $ith$ line denotes the charm of the $jth$ student in the $ith$ group.

- The next $t$ lines each begin with an integer $x$, denoting the number of guests sitting at the $ith$ table. Then $x$ integers follow, representing the generosity of the guests sitting at the $ith$ table. 
- The last line of each test case contains an integer $k$ denoting the maximum number of guests that a student can approach.

## Output Format

Print a single integer on a new line for each test case, which is the maximum possible donation that can be raised during the event, or print -1 if at least one of the rules for collecting donation from guests cannot be followed.

## Constraints

- $1 \le tc \le 10$

- $1 \le n,m,t,x,k \le 15$

- $0 \le charm, generosity \le 1000000$

- The sum of $m$ over all cases in each input is at most 15

## Sample Tests

### Test 1

```
4
3 3 3
1 2 3
4 5 6
7 8 9
3 10 20 30
3 40 50 60
3 70 80 90
3
3 3 3
1 2 3
4 5 6
7 8 9
2 100 200
1 500
2 30 30
1
3 3 3
1 2 3
4 5 6
7 8 9
1 200
2 500 500
3 30 30 30
1
3 3 3
1 2 3
4 5 6
7 8 9
1 200
2 500 500
4 30 30 30 30
1
```

### Test 2

```
3780
7130
10350
-1
```
