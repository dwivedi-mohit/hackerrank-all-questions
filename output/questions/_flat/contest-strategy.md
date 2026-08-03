# Contest Strategy

---

| Field | Value |
|---|---|
| **Slug** | `contest-strategy` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 80 |
| **Contest** | 101hack24 |
| **URL** | https://www.hackerrank.com/challenges/contest-strategy |

---

## Preview

Help Bidhan win the programming contest.

## Problem Statement

HackerRank is conducting a teamed programming contest. The rules of the contest are a bit different than usual:

1. A team consists of exactly $N$ members.
2. Problemset contains exactly $N$ problems and each team member must solve exactly $1$ problem.
3. Only one member from the team is allowed to read the problem statements before the contest start time.

Note that not everyone have read the problems at first. So, to solve problems a member needs to know the statements from some teammate who already knows them. After knowing problems once, a member is eligible to explain them to other teammates ( one teammate at a time ). You can assume that the explaining ( 1 or N problems ) will always take $D$ minutes. During explaining, none of the two involved members will be able to do anything else. 

Problems are of different difficulty levels. You can assume that it will take $T_{i}$ minutes to solve the $i^{th}$ problem, regardless of which member solves it.

Given a team's data, what is the minimum possible time in which they can solve all problems?

## Input Format

The first line will contain $T$, the number of test cases.

The first line of each test case will contain space-separated integers $N$ and $D$. The second line will contain $N$ space-separated integers, where the $i^{th}$ integer denotes $T_i$.



**Constraints**


$1\le T \le 20$

$1\le N \le 3 \times 10^3$

$1 \le T_i, D \le 10^9$

## Output Format

For each test case, output the minimum possible time in which the given team will be able to solve all problems in a separate line.

## Sample Tests

### Test 1

```
1
2 100
1 2
```

### Test 2

```
102
```
