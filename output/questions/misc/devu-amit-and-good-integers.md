# Devu, Amit, and Good Integers

---

| Field | Value |
|---|---|
| **Slug** | `devu-amit-and-good-integers` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 30 |
| **Contest** | 101hack25 |
| **URL** | https://www.hackerrank.com/challenges/devu-amit-and-good-integers |

---

## Preview

Help Devu and Amit in playing with good integers

## Problem Statement

One day Devu found an array $A$ consisting of $n$ integers. His friend, Amit, came to play with Devu and said "I call an integer $good$ if it lies in the range $[L, R]$ (i.e. $L \le x \le R$). Also, I want that if I select any $k$ integers from the array $A$, at least one of them should be a $good$ integer." 

For achieving this, in a single operation, Devu is allowed to increase/decrease any element of the array by one. What will be the minimum number of operations Devu will need for a fixed $k$?"

## Input Format

-	The first line of the input contains a single integer, $T$, corresponding to the number of test cases.
-	For each test case,
	-	the first line will contain three space-separated integers $n, L, R$ as given in the problem.
	-	the next line will contain $n$ space-separated integers denoting array $A$.

## Output Format

For each test case, print $n$ space-separated integers denoting the answer of the problem for $k = 1$ to $n$.

**Constraints**


-	$1 \leq T, n\leq 10^5$   

-	$-10^9 \leq L, R, A[i] \leq 10^9$
-	$L \leq R$
-	Sum of $n$ over all test cases is $\leq 5 * 10^5$

## Sample Tests

### Test 1

```
2
3 1 3
1 2 3
3 1 2
1 3 3
```

### Test 2

```
0 0 0
2 1 0
```
