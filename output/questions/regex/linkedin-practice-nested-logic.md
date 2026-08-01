# Nested Logic

- **Domain:** regex
- **Difficulty:** Easy
- **Max Score:** 40
- **Success Ratio:** 0.8651524452629425
- **Total Submissions:** 4887
- **Solved Count:** 4228
- **URL:** https://www.hackerrank.com/challenges/linkedin-practice-nested-logic

## Problem Statement

Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:	

1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: $fine = 0)$.
2. If the book is returned after the expected return *day* but still within the same calendar month and year as the expected return date, $fine = 15 \text{ Hackos } \times \text{ (the number of days late)}$.	
3. If the book is returned after the expected return *month* but still within the same calendar year as the expected return date, the $fine = 500 \text{ Hackos } \times \text{ (the number of months late)}$.   
4. If the book is returned after the calendar *year* in which it was expected, there is a fixed fine of $10000 \text{ Hackos}$.

## Input Format

The first line contains $3$ space-separated integers denoting the respective $day$, $month$, and $year$ on which the book was *actually* returned.		
The second line contains $3$ space-separated integers denoting the respective $day$, $month$, and $year$ on which the book was *expected* to be returned (due date).

## Output Format

Print a single integer denoting the library fine for the book received as input.  

## Constraints

- $1 \le D \le 31$		
- $1 \le M \le 12$		
- $1 \le Y \le 3000$  
- $\text{It is guaranteed that the dates will be valid Gregorian calendar dates.}$  

## Sample Input

9 6 2015
6 6 2015

## Explanation

Given the following return dates:

Actual:

Expected:

Because , we know it is less than a year late.

Because , we know it's less than a month late.

Because , we know that it was returned late (but still within the same month and year).

Per the library's fee structure, we know that our fine will be . We then print the result of  as our output.
