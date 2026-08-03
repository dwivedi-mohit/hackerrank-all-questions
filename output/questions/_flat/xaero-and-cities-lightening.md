# Xaero And Lighting the Cities

---

| Field | Value |
|---|---|
| **Slug** | `xaero-and-cities-lightening` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 50 |
| **Contest** | 101hack29 |
| **URL** | https://www.hackerrank.com/challenges/xaero-and-cities-lightening |

---

## Problem Statement

Xaero is living in a country called **Hackland**. Hackland has the structure of a tree with $N$ cities connected by $N-1$ bidirectional roads. Each city has an index between $[1, N]$, and no two cities have the same index.

The president of Hackland thinks that traveling within a city is safe. However, traveling between cities, city $A$ to a different city $B$, is not safe due to the poor lighting conditions in Hackland.

In order to ensure safety for the people traveling from one city to another, the president of Hackland decided to install some lights in the country. Each city can have, at most, $1$ light installed in it. It is even possible that some cities already have lights installed. According to the president, traveling from one city $A$ to a different city $B$ is considered to be safe if there is at least $1$ city on that path with a light installed.

Xaero knows that the Hackland budget is very limited. Therefore, he wants to help his president by telling him the minimum number of lights to be installed such that traveling from each city to every other city has become safe.

## Input Format

First line of input contains an integer $T$ denoting the number of test cases. First line of each test case contains a single integer $N$ denoting the number of cities in the country called Hackland. Next line of each test case contains $N$ space separated integers denoting the initial configuration of country i.e a **'0'** at $i^{th}$ position denotes that no light is installed in $i^{th}$ city whereas a **'1'** at $i^{th}$ position denotes that a light is already installed in the $i^{th}$ city. Next $N-1$ lines of each test case contains a pair of integers $U$ and $V$ denoting that there exists a bidirectional road between city $U$ and city $V$. 

**Constraints**

$1 \le T \le 10^{5}$.

$1 \le N \le 5 * 10^{5}$.

$1 \le U, V \le N$.

$Configuration \in$ {0, 1}.

Sum of $N$ over all test cases does not exceed $5 * 10^{5}$.

## Output Format

For each test case, Print the required answer i.e. minimum number of lights needed to be installed in the country in order to ensure safety.

## Sample Tests

### Test 1

```
2
3
0 0 0
1 2
2 3
3
1 0 0
1 2
2 3
```

### Test 2

```
1
1
```
