# Mutual Recurrences

- **Domain:** regex
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.6936776491540516
- **Total Submissions:** 1123
- **Solved Count:** 779
- **URL:** https://www.hackerrank.com/challenges/mutual-recurrences

## Problem Statement

Since you know [how to compute large Fibonacci numbers quickly](https://www.hackerrank.com/contests/infinitum10/challenges/fibonacci-finding-easy) using *matrix exponentiation*, let's take things to the next level.  

Let $a$, $b$, $c$, $d$, $e$, $f$, $g$ and $h$ be positive integers. We define two bi-infinite sequences
$$(\ldots, x_{-2}, x_{-1}, x_0, x_1, x_2, \ldots)$$
and
$$(\ldots, y_{-2}, y_{-1}, y_0, y_1, y_2, \ldots)$$
as follows:  

$$x_n = \begin{cases}
x_{n-a} + y_{n-b} + y_{n-c} + n\cdot d^n & \text{if $n \ge 0$} \\\
1 & \text{if $n < 0$}
\end{cases}$$

and  

$$y_n = \begin{cases}
y_{n-e} + x_{n-f} + x_{n-g} + n\cdot h^n & \text{if $n \ge 0$} \\\
1 & \text{if $n < 0$}
\end{cases}$$

Given $n$ and the eight integers above, find $x_n$ and $y_n$. Since these values can be very large, output them modulo $10^9$.  

This link may help you get started: http://fusharblog.com/solving-linear-recurrence-for-programming-contest/


## Input Format

The first line of input contains $T$, the number of test cases.  
Each test case consists of a single line containing nine space separated integers: $a$, $b$, $c$, $d$, $e$, $f$, $g$, $h$ and $n$, respectively.  

**Constraints**  
$1 \leq T \leq 100$  
$1 \leq a,b,c,d,e,f,g,h < 10$  
$1 \leq n \leq 10^{18}$  



## Output Format

For each test case, output a single line containing two space separated integers, $x_n \bmod 10^9$ and $y_n \bmod 10^9$.  

## Sample Input

1 2 3 1 1 2 3 1 10
1 2 3 2 2 1 1 4 10
1 2 3 4 5 6 7 8 90

## Sample Output

1910 1910
909323 11461521
108676813 414467031

## Explanation

In the second test case, the following is a table of values  and  for :

- -

Remember that  if .

One can verify this table by using the definition above. For example:
