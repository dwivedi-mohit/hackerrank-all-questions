# Extremely Dangerous Virus

- **Domain:** mathematics
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.651356993736952
- **Total Submissions:** 1916
- **Solved Count:** 1248
- **URL:** https://www.hackerrank.com/challenges/extremely-dangerous-virus

## Problem Statement

A recent lab accident resulted in the creation of an extremely dangerous virus that replicates so rapidly it's hard to predict exactly how many cells it will contain after a given period of time. However, a lab technician made the following observations about its growth per millisecond:

- The probability of the number of virus cells growing by a factor of $a$ is $0.5$.
- The probability of the number of virus cells growing by a factor of $b$ is $0.5$. 

Given $a$, $b$, and knowing that initially there is only a single cell of virus, calculate the *expected number* of virus cells after $t$ milliseconds. As this number can be very large, print your answer modulo $(10^9 + 7)$.

## Input Format

A single line of three space-separated integers denoting the respective values of $a$ (the first growth factor), $b$ (the second growth factor), and $t$ (the time you want to know the expected number of cells for).

## Output Format

Print the expected number of virus cells after $t$ milliseconds modulo $(10^9 + 7)$.

## Constraints

- $1 \leq t \leq 10^{18}$  
- $1 \leq a, b \leq 100$  
- it is guaranteed that expected value is integer

## Sample Input

2 4 1

## Explanation

Initially, the virus has one cell. After a millisecond, with probability , its size is doubled and, with probability of the other  in the sample space, its size grows by  times. Thus, the expected number of virus cell after  millisecond is . Thus, we print  on a new line.
