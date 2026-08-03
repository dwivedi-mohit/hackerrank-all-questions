# Counting Perfect Subsequences

---

| Field | Value |
|---|---|
| **Slug** | `p-string` |
| **Contest** | hourrank-20 |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/p-string |

---

## Problem Statement

We call a string, $s$, consisting of the letters in the set $\{\text{a}, \text{b}, \text{c}, \text{d}\}$ a *perfect string* if both the conditions below are true:

$$\#_s(\text{a}) = \#_s(\text{b})$$
$$\#_s(\text{c}) = \#_s(\text{d})$$

where $\#_s(x)$ denotes the number of occurrences of character $x$ in $s$. For example, the diagram below demonstrates why $s = \texttt{"abacadbbcd"}$ is a perfect string:  

![image](https://s3.amazonaws.com/hr-assets/0/1493215386-8ce3a3f1c2-Pstring.png) 

Solve $q$ queries, where each query consists of a string, $s$. For each query, print the number of non-empty [subsequences](https://en.wikipedia.org/wiki/Subsequence) of $s$ that are perfect strings. As this number can be very large, print it modulo $10^9 + 7$.

## Input Format

The first line contains an integer, $q$, denoting the number of queries. 	
Each of the $q$ subsequent lines contains string $s$ for a query.

## Output Format

For each $s$, print the number of non-empty subsequences of $s$ that are perfect strings, modulo $10^9 + 7$, on a new line.

## Constraints

- $1 \le q \le 5$  
- $1 \le \operatorname{length}(s) \le 5\cdot 10^5$  
- String $s$ consists only of the following characters: `a`, `b`, `c`, and `d`.

**Subtask**  

- For $\text{40%}$ of the total score, $1 \le \operatorname{length}(s) \le 4000$.
