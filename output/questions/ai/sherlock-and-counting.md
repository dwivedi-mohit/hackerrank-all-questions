# Sherlock and Counting

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.4286984879928847
- **Total Submissions:** 3373
- **Solved Count:** 1446
- **URL:** https://www.hackerrank.com/challenges/sherlock-and-counting

## Problem Statement

Watson gives Sherlock two integers, $n$ and $k$, and asks him to count the number of positive integer $i$'s such that:   
$$i \cdot (n-i) \le n \cdot k, \text{ and } i < n$$  

Given $q$ queries where each query consists of some $n$ and $k$, print the number of possible $i$'s for each query on a new line.

## Input Format

The first line contains an integer, $q$, denoting the number of times Watson queries Sherlock. 		
Each of the $q$ subsequent lines contains two space-separated integers denoting the respective values of $n$ and $k$ for a query.

## Output Format

For each query, print the number of $i$'s satisfying the given formula on a new line.

## Constraints

- $1 \le q \le 10^5$   
- $1 \le n, k \le 10^9$

## Sample Input

5 1
5 2

## Sample Output

4

## Explanation

Sherlock performs the following  queries:

- The possible values of  satisfying Watson's formula for  and  are  and . Because there are two such values, we print  on a new line.

- The possible values of  satisfying Watson's formula for  and  are , , , and . Because there are four such values, we print  on a new line.
