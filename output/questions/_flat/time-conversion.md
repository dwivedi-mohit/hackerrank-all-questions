# Time Conversion

---

| Field | Value |
|---|---|
| **Slug** | `time-conversion` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/time-conversion |

---

## Preview

Convert time from an AM/PM format to a 24 hour format.

## Problem Statement

Given a time in [$12$-hour AM/PM format](https://en.wikipedia.org/wiki/12-hour_clock), convert it to military (24-hour) time.


Note: 
- 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.

- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.


**Example**


- $\text{s = '12:01:00PM'}$ 


  Return '12:01:00'.

- $\text{s = '12:01:00AM'}$ 


  Return '00:01:00'.

**Function Description**


Complete the $timeConversion$ function with the following parameter(s):

- $string\ s$: a time in $12$ hour format


**Returns**

- $string$: the time in $24$ hour format

## Input Format

A single string $s$ that represents a time in $12$-hour clock format (i.e.: $\text{hh:mm:ssAM}$ or $\text{hh:mm:ssPM}$).

## Constraints

- All input times are valid

## Sample Tests

### Test 1

```
07:05:45PM
```

### Test 2

```
19:05:45
```
