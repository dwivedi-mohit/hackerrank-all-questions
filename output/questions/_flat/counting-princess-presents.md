# Counting Princess Presents

---

| Field | Value |
|---|---|
| **Slug** | `counting-princess-presents` |
| **Contest** | codeagon-2017 |
| **Difficulty** | Medium |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/counting-princess-presents |

---

## Problem Statement

King Bob is the ruler of HackerLand. He would like to give princess Alice, a part of his kingdom on the occasion of her birthday. 

HackerLand has $n$ cities and $n - 1$ roads. Therefore, any two cities $u$ and $v$ (where $u \ne v$) will be connected by at most one single road. 

However, not all roads are the same to Alice. There are $k$ roads which are _special_ to her. She will be happy only if she receives the part of the Kingdom that includes all these _special roads_. Also, if Bob includes the road between cities $u$ and $v$, he is also to include both cities $u$ and $v$. In addition, travel should still be possible between any two cities; so you need to ensure that the part of the kingdom in the birthday present is completely connected.

Your task is to calculate how many different birthday presents can king Bob offer to Alice and then print that number modulo $10^9 + 7$. Two presents are considered different if there exists at least one city in one present which is not included in the other one.

## Input Format

The first line contains an integer $t$, denoting the number of queries. 
The subsequent lines describe each query in the following format:

1. The first line contains a single integer $n$ denoting the number of cities.
2. Each of the $n - 1$ subsequent lines contain three space-separated integers, $u$, $v$ and $g$, describing an undirected road between cities $u$ and $v$. This road is special if and only if $g = 1$.

## Output Format

Print $t$ lines of output where each line $i$ contains the total possible number of presents for the $i^{th}$ query, modulo $10^9 + 7$.

## Constraints

- $1 \le t \le 5$
- $1 \le n \le 10^5$
- $1 \le u, v \le n$
- $0 \le g \le 1$
