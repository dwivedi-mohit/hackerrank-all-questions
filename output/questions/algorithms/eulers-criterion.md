# Euler's Criterion

- **Domain:** algorithms
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.5713809206137425
- **Total Submissions:** 5996
- **Solved Count:** 3426
- **URL:** https://www.hackerrank.com/challenges/eulers-criterion

## Problem Statement

Your friend gives you an equation $A \equiv X^2 \pmod{M}$ and asks you to find an integer solution for $X$.  

However, you know your friend's mischievous nature and suspect that there is no solution to such an equation. Thus, you first want to find out whether there is a solution to it.  

You may find this link helpful: http://mathworld.wolfram.com/EulersCriterion.html

## Input Format

The first line contains the number of cases, $T$. $T$ lines follow, each containing two integers $A$ and $M$ separated by a single space.  


## Output Format

Output $T$ lines, each containing one word: `YES`, if a solution exists and `NO` otherwise.  


## Constraints

+ $0 < T \leq 10^5$  
+ $2 \leq M < 10^9$, $M$ is prime  
+ $0 \leq A < M$



## Sample Input

5 7
4 7

## Sample Output

NO
YES

## Explanation

In the second test case, we can take , as . Or we can take , as .

However there is no integer which gives  modulo  when squared.
