# Coloring Grid

---

| Field | Value |
|---|---|
| **Slug** | `coloring-grid` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/coloring-grid |

---

## Preview

Can you calculate the number of ways to color an N * M grid using K colors? - 80 Points

## Problem Statement

Calculate the number of ways to color an N * M grid using K colors. Adjacent squares in the grid should have different colors. Squares are considered adjacent if they share an edge.

**Input Format**

The first line contains an integer T denoting the number of test-cases.
The next T lines contains integers N, M and K separated by a single space. 

**Output Format**

Output T lines, one for each test case containing the number of ways modulo 10<sup>9</sup>+7. 

**Constraints** 

1 <= T <= 10<sup>5</sup>  

1 <= N,M <= 8

1 <= K <= 10<sup>9</sup>  


**Sample Input**

    3
    3 3 2
    3 4 3
    1 1 1

**Sample Output** 

    2
    1122
    1

**Explanation**

For the first case, there are two ways to color the grid. The colorings are in a chessboard pattern with either color at the top right square.

**Timelimits**
Timelimits for this challenge can be seen [here](https://www.hackerrank.com/environment)

## Sample Tests

### Test 1

```
3
3 3 2
3 4 3
1 1 1
```

### Test 2

```
2
1122
1
```
