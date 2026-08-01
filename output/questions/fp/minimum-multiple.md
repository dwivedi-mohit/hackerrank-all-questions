# Minimum Multiple

- **Domain:** fp
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.6376554174067496
- **Total Submissions:** 563
- **Solved Count:** 359
- **URL:** https://www.hackerrank.com/challenges/minimum-multiple

## Problem Statement

Calculi is Lambda's older brother. Lambda is mischievous and always annoys Calculi by asking silly questions. This time around, Lambda would like to surprise Calculi by asking a challenging and interesting question.  To that end, Lambda gives Calculi an array of $N$ integers, $A = \{a_0, a_1,\ldots, a_{N-1}\}$, followed by $K$ queries. Each query is of two types:


- $Q\ l\ r$: Find the minimum positive integer, $M$, such that each element in subarray $arr[l\ldots r]\ (\{a_l, a_{l+1},\ldots, a_r\})$ divides $M$.
- $U\ idx\ val$: Multiply the value at $idx$ by $val$. That is $a_{idx}' = a_{idx} \times val$, where $a'_{idx}$ is the updated value.

Your task is to help Calculi tackle this challenge. For each query of type $''Q\ l\ r''$, find the value of $M$. As this value can be very large, print the $M$ modulo $(10^9+7)$, i.e., $M \% (10^9+7)$. For query of type $''U\ idx\ val''$, update the required element.


## Input Format

The first line contains an integer, $N$, which represents the length of array, $A$.  
In second line, there are $N$ space-separated integers, $a_0, a_1,\ldots, a_{N-1}$, representing the elements of $A$.  
In third line, there is another integer, $K$, which is the count of queries to follow.   
Then follows $K$ lines, each representing a query of one of the types described above.  

## Output Format

For each query of type `Q l r`, print the value of $M \% (10^9+7)$ on a new line.

## Constraints

- $1 \le N \le 5\times10^4$  
- $1 \le a_i \le 100$, where $i \in [0, N-1]$
- $1 \le K \le 5\times10^4$
- $0 \le l \le r \lt N$
- $0 \le idx \lt N$
- $1 \le val \le 100$

## Sample Input

2 5 6 1 9
7
Q 0 4
U 1 2
Q 0 2
Q 3 4
Q 2 4
U 3 8
Q 2 3

## Sample Output

30
9
18
24

## Explanation

Query 1 (Q 0 4):   Calculi has to find  for (sub)array  which is 90.

Query 2 (U 1 2): . Now updated array is  .

Query 3 (Q 0 2):   for subarray  is .

Query 4 (Q 3 4):   for subarray  is .

Query 5 (Q 2 4):   for subarray   is .

Query 6 (U 3 8):  Updated array is .

Query 7 (Q 2 3):   for subarray  is .

Tested by Wanbo
