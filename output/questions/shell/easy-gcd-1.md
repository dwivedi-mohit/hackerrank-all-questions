# Easy GCD

- **Domain:** shell
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.6656611362493715
- **Total Submissions:** 1989
- **Solved Count:** 1324
- **URL:** https://www.hackerrank.com/challenges/easy-gcd-1

## Problem Statement

We call a sequence of $n$ non-negative integers, $A$, *awesome* if there exists some positive integer $x \gt 1$ such that each element $a_i$ in $A$ (where $0 \le i \lt n$) is *evenly divisible* by $x$. Recall that $a$ evenly divides $b$ if there exists some integer $c$ such that $b = a \cdot c$.

Given an awesome sequence, $A$, and a positive integer, $k$, find and print the maximum integer, $l$, satisfying the following conditions:

1. $0 \le l \le k$
2. $A \cup \{l\}$ is also awesome.

## Input Format

The first line contains two space-separated positive integers, $n$ (the length of sequence $A$) and $k$ (the upper bound on answer $l$), respectively.		
The second line contains $n$ space-separated positive integers describing the respective elements in sequence $A$ (i.e., $a_0, a_1, \ldots, a_{n-1}$).

## Output Format

Print a single, non-negative integer denoting the value of $l$ (i.e., the maximum integer $\le k$ such that $A \cup \{l\}$ is awesome). As $0$ is evenly divisible by any $x \gt 1$, the answer will always exist. 

**Sample Input 0**

    3 5
	2 6 4

**Sample Output 0**

    4

**Explanation 0**		

The only common positive divisor of $2$, $6$, and $4$ that is $\gt 1$ is $2$, and we need to find $l$ such that $0 \le l \le 5$. We know $l \ne 5$ because $x=2$ would not evenly divide $5$. When we look at the next possible value, $l = 4$, we find that this is valid because it's evenly divisible by our $x$ value. Thus, we print $4$.


**Sample Input 1**

    1 5
	7


**Sample Output 1**

    0

**Explanation 1**	

Being prime, $7$ is the only possible value of $x \gt 1$. The only possible $l$ such that $0 \le l \le 5$ is $0$ (recall that $\frac{0}{7} = 0$), so we print $0$ as our answer.


## Constraints

- $1 \le n \le 10^5$
- $1 \le k \le 10^9$
- $1 \le a_i \le 10^9$

## Sample Input

3 5
2 6 4

## Sample Output

4

## Explanation

The only common positive divisor of , , and  that is  is , and we need to find  such that . We know  because  would not evenly divide . When we look at the next possible value, , we find that this is valid because it's evenly divisible by our  value. Thus, we print .
