# Day 6: JavaScript Dates

---

| Field | Value |
|---|---|
| **Slug** | `js10-date` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/js10-date |

---

## Preview

Write a JavaScript function that retrieves the day of the week from a given date.

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

## Sample Tests

### Test 1

```
2
10/11/2009
11/10/2010
```

### Test 2

```
Sunday
Wednesday
```
