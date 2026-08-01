# Day 6: JavaScript Dates

- **Domain:** data-structures
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9897067797154511
- **Total Submissions:** 62274
- **Solved Count:** 61633
- **URL:** https://www.hackerrank.com/challenges/js10-date

## Problem Statement

**Objective**

In this challenge, we learn about JavaScript *Dates*. Check out the attached tutorial for more details.

**Task**

Given a date string, $dateString$, in the format `MM/DD/YYYY`, find and return the day name for that date. Each day name must be one of the following strings: `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, or `Saturday`. For example, the day name for the date `12/07/2016` is `Wednesday`.

## Input Format

Locked stub code in the editor reads the following input from stdin:		
The first line contains an integer, $d$, denoting the number of dates to check.		
Each line $i$ of the $d$ subsequent lines contains a date in `MM/DD/YYYY` format; each date denotes some $dateString$ that is passed to the function.

## Output Format

The function must return a string denoting the day of the week corresponding to the date denoted by $dateString$.

## Constraints

- It is guaranteed that the input only consists of valid dates.

## Sample Input

2
10/11/2009
11/10/2010

## Sample Output

Sunday
Wednesday

## Explanation

The function is called for the following  dates:

- The date 10/11/2009 was a Sunday, so we return Sunday.

- The date 11/10/2010 was a Wednesday, so we return Wednesday.
