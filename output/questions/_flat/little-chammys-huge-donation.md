# Little Ashish's Huge Donation

---

| Field | Value |
|---|---|
| **Slug** | `little-chammys-huge-donation` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/little-chammys-huge-donation |

---

## Preview

Help Ashish calculate donations.

## Problem Statement

Little Ashish is doing internship at multiple places. Instead of giving parties to his friends he decided to donate candies to children. He likes solving puzzles and playing games. Hence he plays a small game. Suppose there are $N$ children. The rules of the game are:


1. The $i^{th}$ child gets $i^{2}$ candies ($1 \le i \le N$).


2. The $y^{th}$ child cannot get a candy until and unless all the children before him ($1 \le i \lt y$) gets candies according to rule number $1$.


One of his jealous friends, Pipi, asks him "Given $X$ (the number of candies) how many children will you be able to serve?". Little Ashish fears calculations and cannot solve this problem so he leaves this problem to the worthy programmers of the world. Help little Ashish in finding the solution.


**Input Format**

The first line contains $T$ i.e. number of test cases.

$T$ lines follow, each line containing an integer $X$.


**Output Format**

For each testcase, print the output that little Ashish wants in one line. 


**Constraints**

$1 \le T \le 10000$

$1 \le X \le 10^{16}$


**Note: If the $i^{th}$ child doesn't get $i^{2}$ number of candies then it's not counted as a successful donation**


**Sample Input**


    3
    1
    5
    13

**Sample Output**


    1

    2

    2


**Explanation**


1. For $X = 1$. Only the $1^{st}$ child can get the candy (i.e. $1^{2}$ candy) and no other child.

2. For $X = 5$. Both the $1^{st}$($1^{2}$ candies) and the $2^{nd}$($2^{2}$ candies) children can get the candies.

3. For $X = 13$. Since the $3^{rd}$ child will get only 8 candies following the rule it won't be counted as a successful donation. Only the $1^{st}$ and the $2^{nd}$ children can get 1 and 4 candies respectively.

## Sample Tests

### Test 1

```
3
1
5
13
```

### Test 2

```
1 
2 
2
```
