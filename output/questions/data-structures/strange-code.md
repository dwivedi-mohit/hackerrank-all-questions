# Strange Counter

- **Domain:** data-structures
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.8374903432292241
- **Total Submissions:** 90610
- **Solved Count:** 75885
- **URL:** https://www.hackerrank.com/challenges/strange-code

## Problem Statement

There is a *strange counter*. At the first second, it displays the number $3$. Each second, the number displayed by decrements by $1$ until it reaches $1$. In next second, the timer resets to $2 \times \text{the initial number for the prior cycle}$ and continues counting down. The diagram below shows the counter values for each time $t$ in the first three cycles:

<img src="https://s3.amazonaws.com/hr-challenge-images/22185/1469447349-bae87a5071-strange1.png" title="strange(1).png" />

Find and print the value displayed by the counter at time $t$.  

**Function Description**  

Complete the *strangeCounter* function in the editor below.  

strangeCounter has the following parameter(s):  

- *int t:* an integer   

**Returns**  

- *int:* the value displayed at time $t$  

## Input Format

A single integer, the value of $t$.

## Constraints

* $1 \le t \le 10^{12}$

**Subtask**

* $1 \le t \le 10^{5}$ for $60 \%$ of the maximum score.

## Explanation

Time  marks the beginning of the second cycle.  It is double the number displayed at the beginning of the first cycle:. This is shown in the diagram in the problem statement.
