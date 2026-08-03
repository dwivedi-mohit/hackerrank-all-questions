# Fractions

---

| Field | Value |
|---|---|
| **Slug** | `fractions` |
| **Contest** | hourrank-2 |
| **Difficulty** | Easy |
| **Score** | 25 |
| **URL** | https://www.hackerrank.com/challenges/fractions |

---

## Problem Statement

You have an array of integers $A$ , indexed from $0$ to $N-1$. You need to find an array $B$ of positive integers where $\lfloor{A_i/B_i}\rfloor=\lfloor{A_{i+1}/B_{i+1}}\rfloor$ for each $0\le i<N-1$. 

If there are multiple solutions, minimize the summation of the numbers in $B$. Formally you have to minimize $s=\sum\limits_{i=0}^{n-1} B_{i}$. <br>

You don't need to print the array, we are only interested to know the minimum possible value of $s$.

*Note*:$\lfloor{X}\rfloor$ is the largest integer that isn't more than $X$. For example: $\lfloor{3.2}\rfloor=3$ and $\lfloor{5}\rfloor=5$. This is known as [Floor Function](http://mathworld.wolfram.com/FloorFunction.html).<br>

## Input Format

The first line contains $N$, the size of array $A$.<br>
The second line contains $N$ integers. Here, the $i^{th}$ integer is $A_i$.

**Constraints**<br>
$1 \le N \le 1000$<br>
$1 \le A_i \le 2000$<br>

## Output Format

Print one integer: The minimum possible value of $s$.
