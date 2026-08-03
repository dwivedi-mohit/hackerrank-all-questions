# Nested Logic

---

| Field | Value |
|---|---|
| **Slug** | `linkedin-practice-nested-logic` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/linkedin-practice-nested-logic |

---

## Preview

Test your understanding of layered logic by calculating a library fine!

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

## Sample Tests

### Test 1

```
9 6 2015
6 6 2015
```

### Test 2

```
45
```
