# Mutual Indivisibility

---

| Field | Value |
|---|---|
| **Slug** | `mutual-indivisibility` |
| **Contest** | hourrank-24 |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/mutual-indivisibility |

---

## Problem Statement

Jugnu has recently been appointed as the sports captain. The headmaster asked her to form a team for an upcoming table tennis tournament, subject to a few constraints. 

Each student of the school is assigned an integer denoting his/her skill level. The headmaster requests Jugnu to form an *indivisible* team of size $x$. The team is *indivisible* if it satisfies the following conditions.

- To make the team strong, each member of the team must have a skill level in the range $[a, b]$.
- The size of the team must be $x$.
- Let $g_1$ and $g_2$ be the skill levels of any two distinct players in the team. Then $g_1$ should not divide $g_2$. This is necessary to avoid clashes.

Can you help Jugnu form an indivisible team? Assume that for every $g$, Jugnu can always find a student with skill level $g$.

## Input Format

The first line contains a single integer $t$, the number of test cases. The descriptions of $t$ test cases follow.  

Each test case consists of a single line containing three space-separated integers $a$, $b$ and $x$.

## Output Format

For each test case, print a single line containing $x$ space-separated integers denoting the skill levels of the team members, or "$-1$" (without quotes) if it's impossible to build an indivisible team.

Make sure output of each testcase is followed by a new line.

You may output the elements in any order. Any valid solution will be accepted.

## Constraints

- $1 \le t \le 50$
- $1 \le a < b \le 10^{4}$
- $2 \le x \le b - a + 1$
