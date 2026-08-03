# Count Triangles

---

| Field | Value |
|---|---|
| **Slug** | `count-triangles` |
| **Domain** | mathematics |
| **Difficulty** | Advanced |
| **Score** | 200 |
| **URL** | https://www.hackerrank.com/challenges/count-triangles |

---

## Preview

How many pairs of triangles have the same area?

## Problem Statement

You are given a regular N-gon with vertices at (cos(2πi / N), sin(2πi / N)), ∀ i ∈ [0,N-1]. Some of these vertices are blocked and all others are unblocked. We consider triangles with vertices at the vertices of N-gon and with at least one vertex at unblocked point. Can you find how many *pairs* of such triangles have equal area?

**Input Format**

The first line of input contains single integer T - number of testcases. 2T lines follow.

Each testcase has two lines.

The first line of testcase contains a single integer N - the number of vertices in N-gon. The second line contains string S with length N. If S[j] equals '1' it means that the vertex (cos(2πj / N), sin(2πj / N)) is unblocked, and if S[j] equals '0' it means that the vertex (cos(2πj / N), sin(2πj / N)) is blocked.

**Output Format**

For each testcase output single line with an answer.

**Constraints** 

1 <= T <= 100

3 <= N <= 10<sup>4</sup>  


There will be no more than 50 blocked vertices in each of the testcase.


**Sample Input**


    1
    4
    1111
  

**Sample Output**


    6

**Explanation**

The testcase given is a square and there are 4 triangles that have the same area. So, the number of pairs are 4C2 = 6.

## Sample Tests

### Test 1

```
1
4
1111
```

### Test 2

```
6
```
