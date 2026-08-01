# Day 9: Multiple Linear Regression

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.9647810372362781
- **Total Submissions:** 11897
- **Solved Count:** 11478
- **URL:** https://www.hackerrank.com/challenges/s10-multiple-linear-regression

## Problem Statement

**Objective**		
In this challenge, we practice using *multiple linear regression*. Check out the [Tutorial](/challenges/s10-multiple-linear-regression/tutorial) tab for learning materials!

**Task**		
Andrea has a simple equation:
$$Y = a + b_{1} \cdot f_{1} + b_{1} \cdot f_{2} + \ldots + b_{m} \cdot f_{m}$$
for $(m + 1)$ real constants ($a$, $f_{1}$, $f_{2}$, $\dots$, $f_{m}$). We can say that the value of $Y$ depends on $m$ features. Andrea studies this equation for $n$ different feature sets $(f_{1}, f_{2}, f_{3}, \ldots, f_{m})$ and records each respective value of $Y$. If she has $q$ new feature sets, can you help Andrea find the value of $Y$ for each of the sets?

**Note:** You are not expected to account for bias and variance trade-offs.

## Input Format

The first line contains $2$ space-separated integers, $m$ (the number of observed features) and $n$ (the number of feature sets Andrea studied), respectively.		
Each of the $n$ subsequent lines contain $m + 1$ space-separated decimals; the first $m$ elements are features $(f_{1}, f_{2}, f_{3}, \ldots, f_{m})$, and the last element is the value of $Y$ for the line's feature set.<br>
The next line contains a single integer, $q$, denoting the number of feature sets Andrea wants to query for.		
Each of the $q$ subsequent lines contains $m$ space-separated decimals describing the feature sets.

## Output Format

For each of the $q$ feature sets, print the value of $Y$ on a new line (i.e., you must print a total of $q$ lines).

## Constraints

- $1 \le m \le 10$  
- $5 \le n \le 100$
- $0 \le x_i \le 1$  
- $0 \le Y \le 10^6$ 
- $1 \le q \le 100$

**Scoring**<br>
For each feature set in one test case, we will compute the following:

- $ d_i' = \large \frac{\left|\texttt{Computed value of Y - Expected value of Y}\right|}{\texttt{Expected value of Y}}$
- $d_{i} = \texttt{max($d_i'$ - 0.1, 0)}$. We will permit up to a $\pm 10\%$ margin of error.  
- $s_{i} = \texttt{max(1.0 - $d_{i}$, 0)}$

The normalized score for each test case will be: $S = \large \frac{\sum_{i = 1}^{q}s_{i}}{q}$. If the challenge is worth $C$ points, then your score will be $S \times C$.


## Sample Input

2 7
0.18 0.89 109.85
1.0 0.26 155.72
0.92 0.11 137.66
0.07 0.37 76.17
0.85 0.16 139.75
0.99 0.41 162.6
0.87 0.47 151.77
4
0.49 0.18
0.57 0.83
0.56 0.64
0.76 0.18

## Sample Output

105.22
142.68
132.94
129.71

## Explanation

We're given , so . We're also given , so we determine that Andrea studied the following feature sets:

-

-

-

-

-

-

-

We use the information above to find the values of , , and . Then, we find the value of  for each of the  feature sets.
