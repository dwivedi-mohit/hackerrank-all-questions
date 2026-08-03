# Train Trip

---

| Field | Value |
|---|---|
| **Slug** | `train-trip` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 60 |
| **Contest** | 101hack51 |
| **URL** | https://www.hackerrank.com/challenges/train-trip |

---

## Preview

Find the minimum time for three people to reach a given place given that the cost of movement depends on the number of people doing it.

## Problem Statement

Leha and his two friends have formed a programming team and are going to this year's ACM ICPC which takes place in their home country. They decided to travel by train to the city where the contest takes place. And, they want to minimize the train trip expenses.


The railway system of the country is represented as an undirected connected graph of $n$ vertices numbered from $1$ to $n$ with $n - 1$ edges between them (vertices represent stations). Initially, Leha is in the vertex $v_1$. The two other members of his team are in $v_2$ and $v_3$ respectively (note that $v_1, v_2, v_3$ are not necessarily distinct). A person can move from their current vertex, say $v$, to vertex $u$ if there is an edge between $v$ and $u$ in the graph. The cost of travel is different depending on the number of people crossing the edge at the same time. If one person is crossing the edge, the cost is equal to $a$. If two people are crossing the same edge together, the cost is $b$. And if all three are crossing the same edge together, they have to pay $c$.


The contest takes place in vertex $1$. You have to help Leha's team find the minimal total cost that they have to pay for the tickets if Leha and his team move optimally.

## Input Format

The first line contains a single integer $t$ denoting the number of test cases.

The first line of each test case contains a single integer $n$ denoting the number of vertices in the graph.

The second line of each case contains three space-separated integers denoting the respective values of $a$, $b$, $c$.

The third line contains three space-separated integers denoting the respective values of $v_1$, $v_2$, $v_3$.

The $i$th of the $n - 1$ subsequent lines contain two space-separated integers denoting the values of $u_i, v_i$, the description of the $i$th edge.

## Output Format

For each test case, print a single integer denoting the team's minimal total cost of the trip.

## Constraints

- $1 \le t \le 60$

- $1 \le n \le 10^5$

- $0 \le a, b, c \le 10^9$

- $1 \le v_1, v_2, v_3 \le n$

- $1 \le v_i, u_i \le n$

- All edges connect different vertices.

- The sum of $n$ in a file is $\le 10^5$.

**Subtasks**

- For one third of the total score, the sum of $n$ in a file is $\le 100$.

## Sample Tests

### Test 1

```
2
5
2 1 1
4 5 3
1 2
1 3
2 4
2 5
5
2 2 2
4 5 3
1 2
1 3
2 4
2 5
```

### Test 2

```
7
8
```
