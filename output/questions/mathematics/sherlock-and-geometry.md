# Sherlock and Geometry

---

| Field | Value |
|---|---|
| **Slug** | `sherlock-and-geometry` |
| **Domain** | mathematics |
| **Difficulty** | Advanced |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/sherlock-and-geometry |

---

## Preview

Help Sherlock in the analysis of geometrical figures.

## Problem Statement

Watson gives a circle and a triangle in a 2-dimensional plane to Sherlock. Sherlock has to tell if they intersect/touch each other. 

The circle is centered at $(x_c,y_c)$ and has radius $R$. 


**Input Format**

The first line contains $T$, the number of test cases.

Each test case consists of $x_c$, $y_c$ and $R$ in one line.

The next three lines each contains $x_i, y_i$ denoting the vertices of the triangle. 


**Output Format** 

For each test case, print `YES` if the triangle touches or intersects the circle; otherwise, print `NO`. 


**Constraints**  

$1 \le T \le 30000$

$1 \le R \le 2000$

$-2000 \le x_c, y_c \le 2000$

$-5000 \le x_i, y_i \le 5000$  

**Note:** There will be no degenerate triangles (i.e. triangles with area 0)


**Sample Input**


	2
    0 0 10
    10 0
    15 0
    15 5
    0 0 10
    0 0
    5 0
    5 5
  

**Sample Output**  


	YES
    NO

**Explanation** 

![image](https://hr-challenge-images.s3.amazonaws.com/2538/2538a.jpg)
![image](https://hr-challenge-images.s3.amazonaws.com/2538/2538b.jpg)

In the first case, the triangle is touching the circle. In the second case, it neither touches nor intersects the circle.

## Sample Tests

### Test 1

```
2
0 0 10
10 0
15 0
15 5
0 0 10
0 0
5 0
5 5
```

### Test 2

```
YES
NO
```
