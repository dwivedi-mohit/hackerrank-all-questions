# Maximizing Mission Points

- **Domain:** mathematics
- **Difficulty:** Hard
- **Max Score:** 70
- **Success Ratio:** 0.5740620957309185
- **Total Submissions:** 6184
- **Solved Count:** 3550
- **URL:** https://www.hackerrank.com/challenges/maximizing-mission-points

## Problem Statement

Xander Cage has a list of cities he can visit on his new top-secret mission. He represents each city as a tuple of $(latitude, longitude, height, points)$. The values of $latitude$, $longitude$, and $height$ are distinct across all cities.

We define a mission as a sequence of cities, ${c_1, c_2, c_3, \cdots, c_k}$, that he visits. We define the total $points$ of such a mission to be the sum of the $points$ of all the cities in his mission list.

Being eccentric, he abides by the following rules on any mission:

- He can choose the number of cities he will visit (if any).
- He can start the mission from any city.
- He visits cities in order of strictly increasing $height$.
- The absolute difference in $latitude$ between adjacent visited cities in his mission must be *at most* $d_lat$.
- The absolute difference in $longitude$ between adjacent visited cities in his mission must be *at most* $d_long$.

Given $d\_lat$, $d\_long$, and the definitions for $n$ cities, find and print the maximum possible total $points$ that Xander can earn on a mission.

## Input Format

The first line contains three space-separated integers describing the respective values of $n$, $d\_lat$, and $d\_long$.  
Each line $i$ of the $n$ subsequent lines contains four space-separated integers denoting the respective $latitude$, $longitude$, $height$, and $points$ for a city.

## Output Format

Print a single integer denoting the maximum possible $points$ that Xander can earn on a mission.

## Constraints

- $1 \le n \le 2 \times 10^5$  
- $1 \le d\_lat, d\_long \le 2 \times 10^5$  
- $1 \le latitude, longitude, height \le 2 \times 10^5$  
- $-2 \times 10^5 \le points \le 2 \times 10^5$

## Sample Input

3 1 1
1 1 1 3
2 2 2 -1
3 3 3 3

## Sample Output

5

## Explanation

Xander can start at city , then go to city , and then go to city  for a maximum value of total

Note that he cannot go directly from city  to city  as that would violate his rules that the absolute difference in  between adjacent visited cities be  and the absolute difference in  between adjacent visited cities be . Because  and , he cannot directly travel between those cities.
