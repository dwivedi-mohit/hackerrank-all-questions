# Day 6: Bitwise Operators

- **Domain:** java
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9780995547711684
- **Total Submissions:** 49862
- **Solved Count:** 48770
- **URL:** https://www.hackerrank.com/challenges/js10-bitwise

## Problem Statement

**Objective**		

Today, we're practicing *bitwise operations*. Check the attached tutorial for more details.

**Task**	

We define $S$ to be a sequence of distinct sequential integers from $1$ to $n$; in other words, $S = \{1, 2, 3,\ldots, n\}$. We want to know the maximum bitwise AND value of any two integers, $a$ and $b$ (where $a \lt b$), in sequence $S$ that is also *less than a given integer*, $k$. 

Complete the function in the editor so that given $n$ and $k$, it returns the maximum $a \text{ & } b \lt k$.

**Note:** The $\text{&}$ symbol represents the [bitwise AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND) operator.

## Input Format

The first line contains an integer, $q$, denoting the number of function calls. 		
Each of the $q$ subsequent lines defines a dataset for a function call in the form of two space-separated integers describing the respective values of $n$ and $k$.

## Output Format

Return the maximum possible value of $a \text{ & } b \lt k$ for any $a \lt b$ in sequence $S$.

## Constraints

* $1 \le q \le 10^3$
* $2 \le n \le 10^3$
* $2 \le k \le n$

## Sample Input

3
5 2
8 5
2 2

## Sample Output

1
4
0

## Explanation

We perform the following  function calls:

- When  and , we have the following possible  and  values in set :

The maximum of any  that is also  is , so we return .

- When  and , the maximum of any  in set  is  (see table above), so we return .

- When  and , the maximum of any  in set  is  (see table above), so we return .
