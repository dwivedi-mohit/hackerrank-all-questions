# Fun With Series

- **Domain:** ai
- **Difficulty:** Advanced
- **Max Score:** 75
- **Success Ratio:** 0.881578947368421
- **Total Submissions:** 76
- **Solved Count:** 67
- **URL:** https://www.hackerrank.com/challenges/fun-with-series

## Problem Statement

Julia found a series, $G$, defined as:
$$G_n = \begin{cases}0 &n = 0\\1 &n = 1\\a\times G_{n-1}+b\times G_{n-2} & n\gt 1 \text{ and } a, b \ge 1 \end{cases}$$

For some integer $p$ (where $p \gt 0$), she finds $p + 2$ integers, $c_0,\  c_1,\ c_2, \ldots,\ c_{p+1}$, such that $L(p, n) = 0$ holds for all integers $n$ (where $n \gt p$):
$$L(p,\ n) = \sum_{i = 0}^{p + 1} c_i \left(G_{n-i}\right)^p$$

She realized that the values of $c_i$ are not unique, so she only considers the tuple $(c_0,\ c_1, \ldots,\ c_{p+1})$ such that $c_0 \gt 0$ and $c_0$ is minimal. It is guaranteed that when $c_0 \gt 0$ and $c_0$ is minimal, there exists only one tuple $(c_0,\ c_1, \ldots,\ c_{p+1})$.

Next, she defines $S_1(p)$ and $S_2(p)$: 
$$S_1(p) = \left( \sum c_i \right) \% (10^9+7)\ \ \ \ \ \forall c_i > 0$$
$$S_2(p) = \left( \sum \left|c_i \right| \right) \% (10^9+7)\ \ \ \ \forall c_i < 0$$

She then finds the following interesting property of $c_i$:
$$\prod_{i=0}^{p+1} \left|c_i\right| = w \times \prod_{i=2}^{p+1}  G_i^{z_i}$$

where $w$ and $z_i$ are integers such that:

* $w \ne 0$
* $z_{2} + 2p = z_{p + 1} + 2$
* $\sum\limits_{i=2}^{p+1} z_i = p$
    
Julia wants you to answer $q$ queries in the following forms:

1. `1 l r`: Using $S_1(p)$ and $S_2(p)$, print three space-separated integers denoting the respective values of $Count_1$, $Count_2$, and $Count_3$ where:

    * $Count_1$ is the total number of possible values of $p$ (where $l \le p \le r$) such that $S_1(p) \gt S_2(p)$.
    * $Count_2$ is the total number of possible values of $p$ (where $l \le p \le r$) such that $S_1(p) \lt S_2(p)$.
    * $Count_3$ is the total number of possible values of $p$ (where $l \le p \le r$) such that $S_1(p) = S_2(p)$.

2. `2 p u v`: Find the value of $S$ modulo $\left(10^9+7\right)$:
	$$S = \left(\prod_{i=u}^{v}G_i\right)^{\left(w + \phi\right)} \text{, where } \phi=\left|\sum_{i=u}^{v} z_i\right|$$

## Input Format

The first line contains three space-separated integers describing the respective values of $a$, $b$, and $q$. 		
Each line $i$ of the $q$ subsequent lines contains three or four space-separated values denoting a query asked by Julia.

## Output Format

Print $q$ lines of output where each line $i$ denotes the answer to query $i$.

## Constraints

* $1 \le a,\ b \le 10^6$
* $1 \le q \le 5 \times 10^4$
* $1 \le l \le r \le 10^3$
* $1 \le p \le 10^6$
* $2 \le u \le v \le p + 1$

## Sample Input

1 1 2
1 1 2
2 1 2 2

## Sample Output

0 2 0
1

## Explanation

The first few terms of series  are , and:

-

-

Query 1 1 2:

The values of  and  are:

- For , , , and . So,  and .

- For , , , , and . So,  and .

So,

-

-

Now,

- , because for , no .

- , because for , each .

- , because for , no .

Thus, we print 0 2 0 (i.e., the respective values of , , and ) on a new line as the answer to Julia's query.

Query 2 1 2 2:

For , , , and :

because . So,  and  because for ,  holds true.

Finally, we can find the value of :

Thus, we print 1 on a new line as the answer to Julia's query.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
