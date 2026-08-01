# Company Retreat

- **Domain:** cpp
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.8175914994096812
- **Total Submissions:** 1694
- **Solved Count:** 1385
- **URL:** https://www.hackerrank.com/challenges/company-retreat

## Problem Statement

The *LRT Company* has $n$ employees. Each employee has a unique ID number from $1$ to $n$, where the director's ID is number $1$. Every employee in the company has *exactly one* immediate supervisor &mdash; except the director, who has no supervisor. The company's employee hierarchy forms a tree of employee IDs that's rooted at employee number $1$ (the director).

The director decides to have a retreat lasting $m$ days. Each day, the employees will be assigned to different groups for team building exercises. Groups are constructed in the following way:

- An employee can invite their immediate supervisor (the director has no supervisor and, thus, doesn't invite anyone). If employee $a$ is invited by employee $b$, then $a$ and $b$ are considered to be in the same group.
- Once an employee is invited to be in a group, they are in that group. This means that if two employees have the same immediate supervisor, only one of them can invite that supervisor to be in their group.  
- Every employee must be in a group, even if they are the only employee in it.

The venue where *LRT* is hosting the retreat has different pricing for each of the $m$ days of the retreat. For each day $j$, there is a cost of $d_j$ dollars per group and a per-group size limit of $p_j$ (i.e., the maximum number of people that can be in any group on that day).

Help the director find optimal groupings for each day so the cost of the $m$-day retreat is minimal, then print the total cost of the retreat. As this answer can be quite large, your answer must be modulo $10^9+7$.

## Input Format

The first line contains two space-separated integers denoting the respective values of $n$ (the number of employees) and $m$ (the retreat's duration in days).		
The next line contains $n-1$ space-separated integers where each integer $i$ denotes $s_i$ ($1 \lt i \leq n$), which is the ID number of employee $i$'s direct supervisor.			
Each line $j$ of the $m$ subsequent lines contain two space-separated integers describing the respective values of $d_j$ (the cost per group in dollars) and $p_j$ (the maximum number of people per group) for the $j^{th}$ day of the retreat.

## Output Format

Print a single integer denoting the minimum total cost for the $m$-day retreat. As this number can be quite large, print your answer modulo $10^9+7$.

## Constraints

- $1 \leq n, m \leq 10^5$
- $1 \le s_i \le n$
- $1 \le d_j, p_j \le 10^9$

**Subtask**			

* $1 \leq n, m\leq 2000$ for $\text{40%}$ of the maximum possible score.

## Sample Input

7 3
1 1 3 4 2 4
5 3
6 2
1 1

## Explanation

In the Sample Case above, the company has  employees and the retreat goes on for  days. The hierarchy looks like this:

On the first day, the cost per group is  dollars and each group has a maximum size of . The employees split into the following three groups:

- Employee  invites their manager, employee . Employee  then invites their manager, employee  (the director).

- Employee  invites their manager, employee . Employee  then invites their manager, employee .

- Employee 's manager is already in another group, so they are in a group by themself.

These groupings are demonstrated in the following image where each group has a different pattern:

In other words, the final groups are , , and . This means the total cost for the first day is  dollars.

On the second day, they split into  groups with a maximum size of  at a total cost of  dollars. On the third day, they split into  groups of size  at a total cost of  dollars. When we sum the costs for all three days, we get  as our answer.
