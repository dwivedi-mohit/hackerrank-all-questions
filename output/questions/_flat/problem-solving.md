# Problem solving

---

| Field | Value |
|---|---|
| **Slug** | `problem-solving` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/problem-solving |

---

## Preview

You need to complete problems which are sorted by difficulty and given numbered by variety. Each day you need to do the problems in increasing difficulty and with a minimum level of variety. What is the minimum number of days it can be completed in?

## Problem Statement

There are N problems numbered 1..N which you need to complete. You've arranged the problems in increasing difficulty order, and the i<sup>th</sup> problem has estimated difficulty level *i*. You have also assigned a rating *vi* to each problem. Problems with similar *vi* values are similar in nature. On each day, you will choose a subset of the problems and solve them. You've decided that each subsequent problem solved on the day should be tougher than the previous problem you solved on that day. Also, to make it less boring, consecutive problems you solve should differ in their *vi* rating by at least K. What is the least number of days in which you can solve all problems?

## Input Format

The first line contains the number of test cases T. T test cases follow. Each case contains an integer N and K on the first line, followed by integers v1,...,vn on the second line.

## Output Format

Output T lines, one for each test case, containing the minimum number of days in which all problems can be solved.

## Constraints

1 <= T <= 100

1 <= N <= 300

1 <= vi <= 1000

1 <= K <= 1000

## Sample Tests

### Test 1

```
2 
3 2 
5 4 7 
5 1 
5 3 4 5 6
```

### Test 2

```
2 
1
```
