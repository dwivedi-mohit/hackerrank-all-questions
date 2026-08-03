# Mirko at the Construction Site

---

| Field | Value |
|---|---|
| **Slug** | `mirko-at-construction-site` |
| **Domain** | fp |
| **Difficulty** | Advanced |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/mirko-at-construction-site |

---

## Problem Statement

Mirko is monitoring a construction site. He monitors $N$ buildings enumerated from $1$ to $N$, starting from the left. For each building, he knows the current number of floors and the number of floors built on each day. He needs to know the answer to $Q$ queries. The answer to each query is the index of the tallest building after $T$ days, as defined by the query. Your task is to help Mirko find the answers to these queries.

## Input Format

The first line consists of the numbers $N$ and $Q$. The second line consists of $N$ integers, where the $i^{th}$ integer represents the initial height of the $i^{th}$ building. The third line consists of $N$ integers, where the $i^{th}$ integer represents the number of floors erected in one day for the $i^{th}$ building. The following $Q$ lines consist of the integer, $T$, representing the day in the query.

## Output Format

For each query, output one number which represents the index of the tallest building after $T$ days. If there is more than one building, output the building with the *greatest* index in the input array (with indexes starting at 1).

**Constraints**


- $ 1 \le N \le 10^5$

- $1 \le Q \le 10^5$ 

- Every other integer in the input will fit in a 32-bit signed integer. And they will be non-negative integers.

## Sample Tests

### Test 1

```
3 6
7 5 1
1 2 3
0
1
2
3
4
5
```

### Test 2

```
1
1
2
2
3
3
```
