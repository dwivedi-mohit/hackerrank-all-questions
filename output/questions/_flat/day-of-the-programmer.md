# Day of the Programmer

---

| Field | Value |
|---|---|
| **Slug** | `day-of-the-programmer` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/day-of-the-programmer |

---

## Preview

Given year, determine date of the 256th day of the year.

## Problem Statement

Marie invented a [Time Machine](https://en.wikipedia.org/wiki/Time_machine) and wants to test it by time-traveling to visit Russia on the [Day of the Programmer](https://en.wikipedia.org/wiki/Day_of_the_Programmer) (the 256th day of the year) during a year in the inclusive range from 1700 to 2700. 

From 1700 to 1917, Russia's official calendar was the [Julian calendar](https://en.wikipedia.org/wiki/Julian_calendar); since 1919 they used the [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar) system. The transition from the Julian to Gregorian calendar system occurred in 1918, when the next day after January 31st was February 14th. This means that in 1918, February 14th was the 32nd day of the year in Russia.

In both calendar systems, February is the only month with a variable amount of days; it has 29 days during a *leap year*, and 28 days during all other years. In the Julian calendar, leap years are divisible by 4; in the Gregorian calendar, leap years are either of the following:

- Divisible by 400.
- Divisible by 4 and *not* divisible by 100.

Given a year, $y$, find the date of the 256th day of that year *according to the official Russian calendar during that year*. Then print it in the format `dd.mm.yyyy`, where `dd` is the two-digit day, `mm` is the two-digit month, and `yyyy` is $y$.

For example, the given $year$ = 1984.  1984 is divisible by 4, so it is a leap year.  The 256th day of a leap year after 1918 is September 12, so the answer is $\texttt{12.09.1984}$.


**Function Description**


Complete the *dayOfProgrammer* function in the editor below.  It should return a string representing the date of the 256th day of the year given.


dayOfProgrammer has the following parameter(s):


- *year*: an integer

## Input Format

A single integer denoting year $y$.

## Output Format

Print the full date of *Day of the Programmer* during year $y$ in the format `dd.mm.yyyy`, where `dd` is the two-digit day, `mm` is the two-digit month, and `yyyy` is $y$.

## Constraints

- 1700 \le y \le 2700

## Sample Tests

### Test 1

```
2017
```

### Test 2

```
13.09.2017
```

### Test 3

```
2016
```

### Test 4

```
12.09.2016
```

### Test 5

```
1800
```

### Test 6

```
12.09.1800
```
