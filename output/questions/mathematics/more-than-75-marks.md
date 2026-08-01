# Higher Than 75 Marks

- **Domain:** mathematics
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9905546704755627
- **Total Submissions:** 1365225
- **Solved Count:** 1352330
- **URL:** https://www.hackerrank.com/challenges/more-than-75-marks

## Problem Statement

Query the *Name* of any student in **STUDENTS** who scored higher than $75$ *Marks*. Order your output by the *last three characters* of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending *ID*.

## Input Format

The **STUDENTS** table is described as follows:
<img src="https://s3.amazonaws.com/hr-challenge-images/12896/1443815243-94b941f556-1.png" />
The *Name* column only contains uppercase (`A`-`Z`) and lowercase (`a`-`z`) letters.

## Sample Output

Ashley
Julia
Belvet

## Explanation

Only Ashley, Julia, and Belvet have Marks > . If you look at the last three characters of each of their names, there are no duplicates and 'ley' < 'lia' < 'vet'.
