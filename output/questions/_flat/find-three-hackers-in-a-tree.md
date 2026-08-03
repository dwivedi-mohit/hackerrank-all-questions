# Find Three Hackers in a Tree

---

| Field | Value |
|---|---|
| **Slug** | `find-three-hackers-in-a-tree` |
| **Contest** | hourrank-18 |
| **Difficulty** | Hard |
| **Score** | 75 |
| **URL** | https://www.hackerrank.com/challenges/find-three-hackers-in-a-tree |

---

## Problem Statement

HackerLand is a tree consisting of $n$ cities connected by $n-1$ undirected roads where each road has length $1$. Ann, Bob, and Clara are whistleblowing citizens living in secret. You want to track them down for an interview using the following pieces of information:

* They live in three different cities expressed as some *unordered* triplet, $(u, v, w)$, where $u$, $v$, and $w$ are the three different cities where Ann, Bob, and Clara live.

	We consider two unordered triplets to be different if one triplet contains an integer not present in the other triplet. For example, $(1,5,2)$ and $(1,2,5)$ are the same because they both contain the same exact elements, but $(1,5,3)$ and $(1,5,2)$ are different because both triplets differ by one value.
* The distances between cities $u$, $v$, and $w$ form another unordered triplet, $(d_{u,v}, d_{u,w}, d_{v,w})$, that reduces to $(k \cdot A, k \cdot B, k \cdot C)$, where $A$, $B$, and $C$ are given values and $k$ is any *real* number.

For example, suppose $A=1$, $B=2$, $C=1$, and HackerLand looks like this:

![image](https://s3.amazonaws.com/hr-assets/0/1487414407-23e8d231e6-3friend3.png)

In this example, it's possible for Ann, Bob, and Clara to live in cities defined by the unordered triplet $(u, v, w) \Rightarrow (2, 3, 5)$, and we express the distances between these cities as $(d_{2,3}, d_{3,5}, d_{2,5}) \Rightarrow (2,2,4)$. If $k=2$, then we can rewrite $(2,2,4)$ as $(2 \cdot 1, 2 \cdot 1, 2 \cdot 2) \Rightarrow (k \cdot A, k \cdot C, k \cdot B)$; note that because these are unordered triplets, $(k \cdot A, k \cdot C, k \cdot B)$ is the same as $(k \cdot A, k \cdot B, k \cdot C)$. 

Given $A$, $B$, $C$, and a map of HackerLand, calculate and print the number of different unordered $(u, v, w)$ triplets that correspond to the possible locations of Ann, Bob, and Clara.

## Input Format

The first line contains four space-separated integers describing the respective values of $n$, $A$, $B$, and $C$. 		
Each of the $n-1$ subsequent lines contains two space-separated integers, $u$ and $v$, defining an undirected road connecting city $u$ to city $v$.

## Output Format

Print the number of different unordered $(u, v, w)$ triplets that correspond to the possible locations of Ann, Bob, and Clara.

## Constraints

- $ 3 \le n \le 2000$ 
- $ 1 \le u, v \le n$
- $ 1 \le A,B,C \le n$
- For $30\%$ of the test cases, $ n \le 50$.
- For $20\%$ of the test cases, $ n \le 200$.
- For $25\%$ of the test cases, $A + B = C$.
