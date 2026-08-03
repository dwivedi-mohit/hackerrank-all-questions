# Grid Challenge

---

| Field | Value |
|---|---|
| **Slug** | `grid-challenge` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/grid-challenge |

---

## Preview

Find if it is possible to rearrange a square grid such that every 
row and every column is lexicographically sorted.

## Problem Statement

Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending.  Determine if the columns are also in ascending alphabetical order, top to bottom.  Return `YES` if they are or `NO` if they are not.

**Example** 

$grid = \text{['abc','ade','efg']}$ 


The grid is illustrated below.

    a b c
    a d e
    e f g
  

The rows are already in alphabetical order.  The columns `a a e`, `b d f` and `c e g` are also in alphabetical order, so the answer would be `YES`.  Only elements within the same row can be rearranged.  They cannot be moved to a different row.

**Function Description**


Complete the *gridChallenge* function in the editor below.


gridChallenge has the following parameter(s):


- *string grid[n]:* an array of strings


**Returns** 


- *string:* either `YES` or `NO`

## Input Format

The first line contains $t$, the number of testcases. 


Each of the next $t$ sets of lines are described as follows:

- The first line contains $n$, the number of rows and columns in the grid.

- The next $n$ lines contains a string of length $n$

## Output Format

For each test case, on a separate line print `YES` if it is possible to rearrange the grid alphabetically ascending in both its rows and columns, or `NO` otherwise.

## Constraints

$1 \leq t \leq 100$

$1 \leq n \leq 100$

*Each string consists of lowercase letters in the range ascii[a-z]*

## Sample Tests

### Test 1

```
a b c
a d e
e f g
```

### Test 2

```
STDIN Function
----- --------
1 t = 1
5 n = 5
ebacd grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
fghij
olmkn
trpqs
xywuv
```

### Test 3

```
YES
```

### Test 4

```
abcde
fghij
klmno
pqrst
uvwxy
```
