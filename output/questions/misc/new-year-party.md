# New Year Party

---

| Field | Value |
|---|---|
| **Slug** | `new-year-party` |
| **Contest** | hourrank-4 |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/new-year-party |

---

## Problem Statement

Aleksa is having a New Year's Eve party! His house has a magic doorway that only allows $1$ person to enter per $1$ second, and he knows $n$ people will show up. 

If two guests arrive at same time, *one guest must wait for the other to enter*. If two guests arrive at different times, the guest arriving first must enter first.

Given the arrival times for all $n$ guests, determine the *entry time* of the last guest.

## Input Format

The first line contains an integer, $n$, denoting the number of guests.		
The second line contains $n$ integers, $t_0, t_1,...,t_{n-1}$, where $t_i$ is the arrival time of $i^{th}$ guest.

**Constraints**

$1 \le n \le 10^5$<br>
$1 \le t_0 \le t_1 \le .... \le t_{n-1} \le 10^6$

## Output Format

Print the time that the last guest *enters* the magic doorway.

**Sample Input 1:**

	8
    2 2 2 2 4 4 4 6 

**Sample Output 1:**

	9
    
**Sample Input 2:**

    3
    2000 2015 2015

**Sample Output 2:**

	2016
