# Sum of the Maximums

- **Domain:** regex
- **Difficulty:** Advanced
- **Max Score:** 90
- **Success Ratio:** 0.6676624346527259
- **Total Submissions:** 2678
- **Solved Count:** 1788
- **URL:** https://www.hackerrank.com/challenges/little-alexey-and-sum-of-maximums

## Problem Statement

Alexey is playing with an array, $A$, of $n$ integers. His friend, Ivan, asks him to calculate the sum of the maximum values for all subsegments of $A$. More formally, he wants Alexey to find $F(A) = \sum\limits_{l=1}^{n}\sum\limits_{r=l}^n\ \max\limits_{l \le x \le r}\ A[x]$.

Alexey solved Ivan's challenge faster than expected, so Ivan decides to add another layer of difficulty by having Alexey answer $m$ queries. The $i^{th}$ query contains subsegment $[L_i, R_i]$, and he must calculate the sum of maximum values on all subsegments inside subsegment $[L_i, R_i]$. 

More formally, for each query $i$, Alexey must calculate the following function:

$F(A, L_i, R_i) = \sum\limits_{l = L_i}^{R_i}\sum\limits_{r = l}^{R_i}\max\limits_{l \le x \le r}\ A[x]$.

Can you help Alexey solve this problem?

## Input Format

The first line contains $2$ space-separated positive integers, $n$ (the length of array $A$) and $m$ (number of queries), respectively.		
The second line contains $n$ space-separated integers, $a_0, a_1, \ldots, a_{n-1}$ describing each element $a_j$ (where $0 \le j \lt n$) in array $A$.	
Each of the $m$ subsequent lines contains $2$ space-separated positive integers describing the respective values for $L_i$ and $R_i$ in query $i$ (where $0 \le i \lt m$).

## Output Format

For each query $i$ (where $0 \le i \lt m$), print its answer on a new line.

## Constraints

- $1 \le n, m \le 135000$
- $-10^9 \le a_i \le 10^9$
- $1 \le L_i \le R_i \le n$

## Sample Input

3 6
1 3 2
1 1
1 2
1 3
2 2
2 3
3 3

## Sample Output

7
15
3
8
2

## Explanation

The answer for the second query is shown below:

The answer for the third query is shown below:
