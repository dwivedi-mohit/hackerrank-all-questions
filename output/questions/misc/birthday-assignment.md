# Birthday Assignment

---

| Field | Value |
|---|---|
| **Slug** | `birthday-assignment` |
| **Contest** | hourrank-29 |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/birthday-assignment |

---

## Problem Statement

Nikita has a family tree $T$ consisting of $N$ members number from $1$ to $N$. Each of the $N-1$ edges in the tree represents a directed relationship. Basically if there is an edge from member $A$ to $B$, it means $B$ was born before $A$. Now, Nikita knows that these $N$ members were born in last $M$ days and only $1$ person was born on a single day, She is interested in calculating the number of ways to assign birthdays to each of the $N$ family members.


Since the required answer can be quite large, print it modulo $10^9+7$.

## Input Format

First line of input contains a single integer $T$ denoting the number of test cases.  
First line of each test case contains $2$ space separated integers denoting $N$ and $M$ respectively.  
Next $N-1$ lines of each test case contains $2$ space separated integers $A$ and $B$ denoting a direct relationship from $A$ to $B$.

## Output Format

Output consists of only $T$ line. For each line, Print required answer modulo $10^9+7$.

## Constraints

- $1 \le T \le 5$  
- $1 \le N \le 1000$  
- $1 \le A, B \le N$  
- $1 \le M \le 10^9$  

**Scoring**  

*  $1 \le N = M \le 9$ for $20\%$ test data.   
*  $1 \le N \le 100$ for $20\%$ test data.  
*  $1 \le N \le 1000$ for $60\%$ test data.
