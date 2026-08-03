# Impressing the Boss

---

| Field | Value |
|---|---|
| **Slug** | `impressing-the-boss` |
| **Contest** | hourrank-27 |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/impressing-the-boss |

---

## Problem Statement

Given the consecutive years' sales data of a company as an array of integers: $a = [a_0, a_1, \ldots, a_{n-1}]$, with $a_i$ denoting the total sales during the $i^\text{th}$ year, your current task is to present the annual sales graph. 

Your boss would be most impressed if the sales graph showed that the total sales never decreased for every pair of consecutive years. For this, you are allowed to modify at most one element of the data array for the property to be true. (Any more and the change will be too obvious.)

Given $a$, determine if it is possible to do this task.

Complete the function `canModify` which takes in the integer array $a$ and returns the string `YES` or `NO` denoting whether it is possible to do the task.

## Input Format

The first line of input denotes $t$ denoting the number of scenarios. The following lines describe the scenarios.  

The first line of each scenario contains a single integer $n$ denoting the length of array $a$. The second line contains $n$ space-separated integers $a_0, a_1, \ldots, a_{n-1}$.

## Output Format

For each scenario, print a single line containing a single string: either `YES` or `NO` denoting whether it is possible to do the task.

## Constraints

- $1 \le t \le 20$  
- $1 \le n \le 20$  
- $1 \le a_i \le 2000$
