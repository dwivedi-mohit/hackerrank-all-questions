# Devu and a Journey on Metro

---

| Field | Value |
|---|---|
| **Slug** | `devu-and-a-journey-in-a-metro` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 80 |
| **Contest** | 101hack25 |
| **URL** | https://www.hackerrank.com/challenges/devu-and-a-journey-in-a-metro |

---

## Preview

Help Devu calculate the expected cost of his journey on the metro.

## Problem Statement

Delhi metro has $n$ stations connected by roads between them. The underlying network of roads between the stations has a tree structure. For each road $u, v$, there is a fare for going from station $u$ to station $v$.

Devu wants to travel by metro, so he is currently at station $1$. In a single step, he can uniformly randomly go to any of the neighbouring stations of the current station. 

The metro charges you based on the starting and ending station regardless of the actual distance you might have travelled. So the fare charged from you for a journey will be the total fare of roads on the path from start to end station.

Find out the expected fare of his journey having a total of $k$ steps.

## Input Format

-	The first line contains an integer $T$, that is the number of test cases.
-	For each test case
	-	The first line contains two space-separated integers, $n, k$, as defined in the problem statement.
    -	In the next $n - 1$ lines, each line contains three space-separted integers $u, v, w$ denoting that there is a road between station $u$ to $v$ with fare equal to $w$.

## Output Format

For each test case, print a real number having absolute or relative error of 1e-6.

**Constraints** 


-	$1 \leq T \leq 50$
-	$2 \leq n, k \leq 50$
-	$1 \leq w \leq 10^9$
-	$1 \leq u, v \leq n$ 
-	It is guaranteed that there is no multi-edge and self-loop in the given input.

## Sample Tests

### Test 1

```
2
2 1
1 2 4
2 2
1 2 4
```

### Test 2

```
4.000000
0.000000
```
