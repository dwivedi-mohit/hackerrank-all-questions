# Time Conversion

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 100
- **Success Ratio:** 0.9483965322276668
- **Total Submissions:** 331625
- **Solved Count:** 314512
- **URL:** https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion

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

Complete the *timeConversion* function in the editor below.  It should return a new string representing the input time in 24 hour format.  

timeConversion has the following parameter(s):

- *string s*: a time in $12$ hour format  

**Returns**

- *string*: the time in $24$ hour format

## Input Format

A single string $s$ that represents a time in $12$-hour clock format (i.e.: $\text{hh:mm:ssAM}$ or $\text{hh:mm:ssPM}$).

## Constraints

- All input times are valid

## Sample Input

07:05:45PM

## Sample Output

19:05:45

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
