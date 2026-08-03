# Concerts

---

| Field | Value |
|---|---|
| **Slug** | `concerts` |
| **Contest** | codeagon-2017 |
| **Difficulty** | Hard |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/concerts |

---

## Problem Statement

Irina loves music very much. She wants to visit several concerts in Cowmos and then go to St. Hackerburg and visit several concerts there. Irina choose $n$ days in order of time and for each day $i$ she knows that:

- There will be a concert with interest equal to $a_i$ in Cowmos.
- There will be a concert with interest equal to $b_i$ in St. Hackerburg.

When Irina decides to move from Cowmos to St. Hackerburg, she will do it instantly. She can go to St. Hackerburg on the first day. Also, she can choose not to go to St. Hackerburg at all. Note that Irina can visit no more than one concert in a day. Also, she cannot go back to Cowmos from St.Hackerburg.

Let $q_k$ be the maximal possible interest of concert with the minimum interest among visited concerts in case if Irina will visit exactly $k$ concerts. She wants to know the values of $q_1, q_2, ..., q_n$.

## Input Format

The first line contains a single integer denoting $n$.  
The second line contains $n$ space-separated integers describing the respective values of $a_1, a_2, ..., a_n$.  
The third line contains $n$ space-separated integers describing the respective values of $b_1, b_2, ..., b_n$.

## Output Format

Print $n$ space-separated integers describing the respective values of $q_1, q_2, ..., q_n$.

## Constraints

- $1 \leq n \leq 2 \cdot 10 ^ 5$
- $1 \leq a_i, b_i \leq 10 ^ 9$
