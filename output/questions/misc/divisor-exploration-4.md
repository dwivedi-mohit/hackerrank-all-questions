# Professor Numerico and the Divisors

---

| Field | Value |
|---|---|
| **Slug** | `divisor-exploration-4` |
| **Contest** | hourrank-3 |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/divisor-exploration-4 |

---

## Problem Statement

Professor Numerico is a number fanatic who loves to explore the properties of numbers. His apprentice, Dumdum, is your good friend, who you often help solve problems for Numerico. 
<hr>

The Professor is fed up with *Summation* and resolves to explore *Multiplication*. He tasks Dumdum with finding the product of a number $N$'s divisors, or $f(N)$ where $$f(N) = \prod_{d|N}d$$

For example, if $N = 12$, then $f(12) = 1 \times 2 \times 3 \times 4 \times 6 \times 12 = 1728$.

Dumdum proudly manages to calculate this himself. Determining the task is too easy, Professor Numerico decides to change the task by giving Dumdum a number, $X$, and asking him to find the smallest positive integer, $N$, whose product of divisor is $X$ (i.e.: find $N$ such that $f(N) = X$). Dumdum isn't sure how to solve this new problem. Can you help?

## Input Format

The first line contains a single positive integer, $T$, denoting the number of test cases. 	
The subsequent $T$ lines each contain a single positive integer, $X$.

**Constraints** <br>
$1 \leq T \leq 10^3$ <br>
$1 \leq X \leq 10^{18}$

**For 33.33% Points:** If $N$ exists, $1 \leq N \leq 10^6$. <br>
**For Full Points:** No additional constraints on result.

## Output Format

For each test case, print the smallest positive integer $N$ such that the product of $N$'s divisors is equal to $X$. If there is no such $N$, print $-1$.
