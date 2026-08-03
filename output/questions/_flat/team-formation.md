# Team Formation

---

| Field | Value |
|---|---|
| **Slug** | `team-formation` |
| **Domain** | algorithms |
| **Difficulty** | Advanced |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/team-formation |

---

## Preview

Help Roy to form teams such that the smallest team is as large as possible.

## Problem Statement

For an upcoming programming contest, Roy is forming some teams from the students of his university. A team can have any number of contestants. 

Roy knows the skill level of each contestant. To make the teams work as a unit, he forms the teams based on some rules. Each of the team members must have a unique skill level for the team.  If a member's skill level is $x[i]$ where $0 \lt i$, there exists another team member whose skill level is $x[i]-1$. Note that a contestant can write buggy code and thus can have a negative skill level.

The more contestants on the team, the more problems they can attempt at a time so Roy wants to form teams such that the smallest team is as large as possible.

For example, there are $n=7$ contestants with skill levels $skills = [-1,0,1,2,2,3]$.  There are many ways teams could be formed, e.g. [-1], [0],...,[3].  At the other end of the spectrum, we could form $team1 = [-1,0,1,2,3]$ and $team2 = [2]$.  We're looking for the largest smaller team size though.  Two sets that meet the criteria are $team1 = [-1,0,1,2]$ and $team2 = [2,3]$.  The largest smaller team size possible is $2$.

**Note:** There is an edge case where $0$ contestants have registered.  As no teams are to be created, the largest team created will have $0$ members.

## Input Format

The first line contains an integer $t$, the number of test cases.
<br>

Each of the next $t$ lines contains a string of space-separated integers, $n$ followed by $n$ integers $x[i]$, a list of the contestants' skill levels.

## Output Format

For each test case, print the size of largest possible smallest team on a separate line.

## Constraints

$1 \le t \le 100$ 

$0 \le n \le 10^6$

$-10^5 \le x[i] \le 10^5$

## Sample Tests

### Test 1

```
4 
7 4 5 2 3 -4 -3 -5 
1 -4 
4 3 2 3 1 
7 1 -2 -3 -4 2 0 -1
```

### Test 2

```
3
1
1
7
```
