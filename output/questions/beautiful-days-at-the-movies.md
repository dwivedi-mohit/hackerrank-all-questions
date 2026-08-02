# Beautiful Days at the Movies

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9658761161722564
- **Total Submissions:** 276727
- **Solved Count:** 267284
- **URL:** https://www.hackerrank.com/challenges/beautiful-days-at-the-movies

## Problem Statement

Lily likes to play games with integers.  She has created a new game where she determines the difference between a number and its reverse.  For instance, given the number $12$, its reverse is $21$.  Their difference is $9$.  The number $120$ reversed is $21$, and their difference is $99$.

She decides to apply her game to decision making.  She will look at a numbered range of days and will only go to a movie on a *beautiful day*.

Given a range of numbered days, $[i \ldots j]$ and a number $k$, determine the number of days in the range that are *beautiful*.  Beautiful numbers are defined as numbers where $|i \text{-} reverse(i)|$ is evenly divisible by $k$.  If a day's value is a beautiful number, it is a beautiful day.  Return the number of beautiful days in the range.

**Function Description**  

Complete the *beautifulDays* function in the editor below.   

beautifulDays has the following parameter(s):  

- *int i:* the starting day number  
- *int j:* the ending day number  
- *int k:* the divisor  

**Returns**  

- *int:* the number of beautiful days in the range  

## Input Format

A single line of three space-separated integers describing the respective values of $i$, $j$, and $k$.

## Constraints

- $1 \le i \le j \le 2 \times 10^6$
- $1 \le k \le 2 \times 10^9$

## Sample Input

20 23 6

## Explanation

Lily may go to the movies on days , , , and . We perform the following calculations to determine which days are beautiful:

- Day  is beautiful because the following evaluates to a whole number:

- Day  is not beautiful because the following doesn't evaluate to a whole number:

- Day  is beautiful because the following evaluates to a whole number:

- Day  is not beautiful because the following doesn't evaluate to a whole number:

Only two days,  and , in this interval are beautiful. Thus, we print  as our answer.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
