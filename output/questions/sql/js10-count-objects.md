# Day 4: Count Objects

- **Domain:** sql
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9963335370257208
- **Total Submissions:** 90005
- **Solved Count:** 89675
- **URL:** https://www.hackerrank.com/challenges/js10-count-objects

## Problem Statement

**Objective**

In this challenge, we learn about iterating over objects. Check the attached tutorial for more details.

**Task**

Complete the function in the editor. It has one parameter: an array, $a$, of objects. Each object in the array has two integer properties denoted by $x$ and $y$. The function must return a count of all such objects $o$ in array $a$ that satisfy $o.x == o.y$.

## Input Format

The first line contains an integer denoting $n$.		
Each of the $n$ subsequent lines contains two space-separated integers describing the values of $x$ and $y$.

## Output Format

Return a count of the total number of objects $o$ such that $o.x == o.y$. Locked stub code in the editor prints the returned value to STDOUT.

## Constraints

- $5 \le n \le 10$
- $1 \le x, y \le 100$

## Sample Input

5
1 1
2 3
3 3
3 4
4 5

## Sample Output

2

## Explanation

There are  objects in the  array:

-

-

-

-

-

Because we have two objects  that satisfy  (i.e.,  and ), we return  as our answer.
