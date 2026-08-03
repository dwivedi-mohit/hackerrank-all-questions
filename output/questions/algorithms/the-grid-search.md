# The Grid Search

---

| Field | Value |
|---|---|
| **Slug** | `the-grid-search` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/the-grid-search |

---

## Preview

Given a 2D array of digits, try to find a given 2D grid pattern of digits within it.

## Problem Statement

Given an array of strings of digits, try to find the occurrence of a given pattern of digits. In the grid and pattern arrays, each string represents a row in the grid.  For example, consider the following grid:


<pre>
1234567890

09<strong>876543</strong>21

11<strong>111111</strong>11

11<strong>111111</strong>11

2222222222

</pre>

The pattern array is:

<pre>
876543

111111

111111
</pre>


The pattern begins at the second row and the third column of the grid and continues in the following two rows.  The pattern is said to be *present* in the grid.  The return value should be `YES` or `NO`, depending on whether the pattern is found.  In this case, return `YES`. 


**Function Description**


Complete the *gridSearch* function in the editor below.  It should return `YES` if the pattern exists in the grid, or `NO` otherwise.


gridSearch has the following parameter(s):


- *string G[R]:* the grid to search 
- *string P[r]:* the pattern to search for

## Input Format

The first line contains an integer $t$, the number of test cases. 


Each of the $t$ test cases is represented as follows:

The first line contains two space-separated integers $R$ and $C$, the number of rows in the search grid $G$ and the length of each row string.

This is followed by $R$ lines, each with a string of $C$ digits that represent the grid $G$.

The following line contains two space-separated integers, $r$ and $c$, the number of rows in the pattern grid $P$ and the length of each pattern row string.

This is followed by $r$ lines, each with a string of $c$ digits that represent the pattern grid $P$.


**Returns**


- *string:*  either `YES` or `NO`

## Constraints

$1 \le t \le 5$

$1 \le R,r,C,c \le 1000$  

$1 \le r \le R$

$1 \le c \le C$

## Sample Tests

### Test 1

```
1234567890 
09
876543
21 
11
111111
11 
11
111111
11 
2222222222
```

### Test 2

```
876543 
111111 
111111
```

### Test 3

```
2
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
15 15
400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160
2 2
99
99
```

### Test 4

```
YES
NO
```

### Test 5

```
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
```

### Test 6

```
7283455864 
6731158619 
8988242643 
3830589324 
222
9505
813 
563
3845
374 
647
3530
293 
7053106601 
0834282956 
4607924137
```

### Test 7

```
15 15
400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160
2 2
99
99
```

### Test 8

```
99
99
```
