# Constructing a Number

- **Domain:** mathematics
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9193105649537184
- **Total Submissions:** 15665
- **Solved Count:** 14401
- **URL:** https://www.hackerrank.com/challenges/constructing-a-number

## Problem Statement

Manipulating numbers is at the core of a programmer's job. To test how well you know their properties, you are asked to solve the following problem.

You are given $n$ non-negative integers $a_1$, $a_2$, ..., $a_n$. You want to know whether it's possible to construct a new integer using all the digits of these numbers such that it would be divisible by $3$. You can reorder the digits as you want. The resulting number can contain leading zeros.

For example, consider the numbers $50, 40, 90$ from which you have to construct a new integer as described above. Numerous arrangements of digits are possible; but we have illustrated one below. 


![image](https://s3.amazonaws.com/hr-assets/0/1514370322-1398c77ec5-number_cons1.png)


Complete the function `canConstruct` which takes an integer array as input and return "`Yes`" or "`No`" based on whether or not the required integer can be formed.


## Input Format

The first line contains a single integer $t$ denoting the number of queries. The following lines describe the queries.

Each query is described in two lines. The first of these lines contains a single integer $n$. The second contains $n$ space-separated integers $a_1$, $a_2$, ..., $a_n$.

## Output Format

For each query, print a single line containing "`Yes`" if it's possible to construct such integer and "`No`" otherwise.

## Constraints

- $1 \leq t \leq 100$
- $1 \leq n \leq 100$
- $1 \leq a_i \leq 10^9$

**Subtasks**

For 33.33% of the total score:

- $n = 1$
- $1 \leq a_1 \leq 10 ^ 6$

## Sample Input

3
1
9
3
40 50 90
2
1 4

## Sample Output

Yes
Yes
No

## Explanation

In the first example,  is divisible by , so the answer is "Yes".

In the second example you can construct the number  which is divisible by , so the answer is "Yes". Note that there may be other numbers you can construct, some of which are shown in the challenge statement.

In the third example, the only possible numbers are  and , but both of them are not divisible by , so the answer is "No".
