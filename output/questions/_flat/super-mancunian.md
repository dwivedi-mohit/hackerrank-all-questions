# Super Mancunian

---

| Field | Value |
|---|---|
| **Slug** | `super-mancunian` |
| **Contest** | hourrank-22 |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/super-mancunian |

---

## Problem Statement

Nowadays, the kids are playing Super Mancunian, a modern reinvention of a classical game.  

The main character of the game is, as you may have guessed, Mancunian. She is currently located at level $1$. There are $n$ levels in the game and she is required to visit each of them at least once. Note that it is not necessary to visit the levels in order; she can visit the levels in any order she chooses to.  

There are certain bidirectional pathways in the game connecting some pairs of levels. Each pathway connects two (not necessarily distinct) levels and each pair of levels have at most one pathway between them. Using pathways is the only way to travel between levels, but it is guaranteed that she can travel from any level to any other level using some number of pathways. To use a particular pathway, you need to pay a particular amount as cost. But it is a one-time payment; once that pathway is unlocked, you can use it as many times as you wish at no additional cost.  

Like the rest of her clan, Mancunian also possesses a special power. She can reduce the cost of exactly one pathway in the game to $0$.  

Mancunian starts at level $1$. What is the minimum cost she needs to pay to visit all the levels? Also, *how many pathways* can she choose to reduce to $0$ so that she can visit all the levels at the minimum cost?

## Input Format

The first line of input contains two space-separated integers $n$ and $m$, the number of levels in the game and the number of pathways respectively.  

Each of the next $m$ lines contains three space-separated integers $a$, $b$ and $w$ indicating that there is a bidirectional pathway between the levels $a$ and $b$ having cost $w$.

## Output Format

Print two space-separated integers, the first of which is the minimum cost incurred and the second is the number of possible pathways she can use her superpower on to achieve the minimum possible total cost. See the sample explanation for more details.

## Constraints

- $1 \le n \le 100000$  
- $1 \le m \le 200000$  
- $1 \le w \le 10^{9}$  
- $1 \le a, b \le n$  

**Subtask**  

- For 45% of the maximum points, $1 \le n \le 5000$ and $1 \le m \le 10000$
