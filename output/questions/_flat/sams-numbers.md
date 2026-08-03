# Sam's Numbers

---

| Field | Value |
|---|---|
| **Slug** | `sams-numbers` |
| **Contest** | hourrank-21 |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/sams-numbers |

---

## Problem Statement

Once, Sam started to write down numbers in a row. Let's call this list $A$.  

Each number was between $1$ and $m$, inclusive, and the *absolute difference* between any adjacent pair of numbers was at most $d$, i.e., $|A_i - A_{i-1}| \le d$ for all $1 < i \le \mathrm{length}(A)$. As soon as she stopped writing, she noticed that the sum of the numbers she wrote was $s$.  

For example, if $m = 6$, $d = 3$ and $s = 24$, then she could have written the list $[1, 3, 6, 5, 2, 3, 4]$. Notice that each number is between $1$ and $m = 6$, inclusive, the absolute difference between any adjacent pair is $\le d = 3$, and the sum is $s = 24$.  

![image](https://s3.amazonaws.com/hr-assets/0/1495799428-a8da0f0387-SamsNumbers.png)


She then started thinking how many different ways this could have happened, i.e., how many lists of numbers satisfy all the conditions above. Can you help her in calculating this number?

As the answer can be very large, apply a modulo $10^9 + 9$ on the result before printing it.

## Input Format

The first and only line of input contains three space-separated integers denoting $s$, $m$ and $d$ respectively.

## Output Format

Print a single line containing a single integer denoting the requested number modulo $10^9 + 9$.

## Constraints

- $1 \le s \le 10^{18}$  
- $1 \le m \le 10$  
- $0 \le d \lt m$  

**Subtasks**  

- For $20\%$ of the maximum score, $s \le 20$  
- For $40\%$ of the maximum score, $s \le 10^5$
