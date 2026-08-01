# Restaurant

- **Domain:** shell
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.8876684707630267
- **Total Submissions:** 37692
- **Solved Count:** 33458
- **URL:** https://www.hackerrank.com/challenges/restaurant

## Problem Statement

Martha is interviewing at Subway. One of the rounds of the interview requires her to cut a bread of size $l \times b$ into smaller identical pieces such that each piece is a square having maximum possible side length with no left over piece of bread.


## Input Format

The first line contains an integer $T$. $T$ lines follow. Each line contains two space separated integers $l$ and $b$ which denote length and breadth of the bread. 



## Output Format

$T$ lines, each containing an integer that denotes the number of squares of maximum size, when the bread is cut as per the given condition.

## Constraints

+ $1 \le T \le 1000$
+ $1 \le l, b \le 1000$

## Sample Input

2
2 2
6 9

## Sample Output

1
6

## Explanation

The 1st testcase has a bread whose original dimensions are , the bread is uncut and is a square. Hence the answer is 1.

The 2nd testcase has a bread of size . We can cut it into 54 squares of size , 6 of size . For other sizes we will have leftovers. Hence, the number of squares of maximum size that can be cut is 6.
