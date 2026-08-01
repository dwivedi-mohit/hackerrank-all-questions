# Team Formation

- **Domain:** databases
- **Difficulty:** Advanced
- **Max Score:** 70
- **Success Ratio:** 0.5050788559208768
- **Total Submissions:** 7482
- **Solved Count:** 3779
- **URL:** https://www.hackerrank.com/challenges/team-formation

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

## Sample Input

7 4 5 2 3 -4 -3 -5
1 -4
4 3 2 3 1
7 1 -2 -3 -4 2 0 -1

## Sample Output

1
1
7

## Explanation

For the first case, Roy can form two teams: one with contestants with skill levels {-4,-3,-5} and the other one with {4,5,2,3}. The first group containing 3 members is the smallest.

In the second case, the only team is {-4}

In the third case, the teams are {3} , {1,2,3}, the size of the smaller group being 1.

In the last case, you can build one group containing all of the contestants. The size of the group equals the total number of contestants.

Time limits

Time limits for this challenge are given here

Note

If n = 0, print 0.
