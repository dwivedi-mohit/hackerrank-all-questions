# Beautiful 3 Set

- **Domain:** shell
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.6230641592920354
- **Total Submissions:** 3616
- **Solved Count:** 2253
- **URL:** https://www.hackerrank.com/challenges/beautiful-3-set

## Problem Statement

You are given an integer $n$. A set, $S$, of triples $(x_i, y_i, z_i)$ is *beautiful* if and only if:

- $0 \le x_i, y_i, z_i$
- $x_i + y_i + z_i = n, \forall i : 1 \le i \le |S|$
- Let $X$ be the set of different $x_i$'s in $S$, $Y$ be the set of different $y_i$'s in $S$, and $Z$ be the set of different $z_i$ in $S$. Then $|X| = |Y| = |Z| = |S|$.

The third condition means that all $x_i$'s are pairwise distinct. The same goes for $y_i$ and $z_i$.

Given $n$, find any *beautiful* set having a maximum number of elements. Then print the [cardinality](https://en.wikipedia.org/wiki/Cardinality) of $S$ (i.e., $|S|$) on a new line, followed by $|S|$ lines where each line contains $3$ space-separated integers describing the respective values of $x_i$, $y_i$, and $z_i$.

## Input Format

A single integer, $n$.

## Output Format

On the first line, print the cardinality of $S$ (i.e., $|S|$).		
For each of the $|S|$ subsequent lines, print three space-separated numbers per line describing the respective values of $x_i$, $y_i$, and $z_i$ for triple $i$ in $S$.

## Constraints

- $1 \le n \le 300$  

## Sample Output

0 1 2
2 0 1
1 2 0

## Explanation

In this case, . We need to construct a set, , of non-negative integer triples () where .  has the following triples:

-

-

-

We then print the cardinality of this set, , on a new line, followed by  lines where each line contains three space-separated values describing a triple in .
