# Coolguy and Two Subsequences

---

| Field | Value |
|---|---|
| **Slug** | `coolguy-and-two-subsequences` |
| **Domain** | data-structures |
| **Difficulty** | Advanced |
| **Score** | 120 |
| **URL** | https://www.hackerrank.com/challenges/coolguy-and-two-subsequences |

---

## Preview

What is the sum of the minimum elements of all unordered non-intersecting contiguous subsequence pairs?

## Problem Statement

Coolguy gives you a simple problem. Given a $1$-indexed array, $A$, containing $N$ elements, what will $ans$ be after this pseudocode is implemented and executed? Print $ans \ \% \ (10^9+7)$.

	//f(a, b) is a function that returns the minimum element in interval [a, b]
	
    ans = 0
  

    for a -> [1, n]
    	for b -> [a, n]
        	for c -> [b + 1, n]
            	for d -> [c, n]
                	ans = ans + min(f(a, b), f(c, d))

## Input Format

The first line contains $N$ (the size of array $A$).	
The second line contains $N$ space-separated integers describing $A$.

**Constraints**

- $1$ &le; $N$ &le; $2 \times 10^5$
- $1$ &le; $A_i$ &le; $10^9$

**Note:** $A$ is $1$-indexed (i.e.: $A = \{ A_1, A_2, \ldots, A_{N-1}, A_N \}$).

## Output Format

Print the integer result of $ans \ \% \ (10^9+7)$.

## Sample Tests

### Test 1

```
//f(a, b) is a function that returns the minimum element in interval [a, b]
ans = 0
for a -> [1, n]
 for b -> [a, n]
 for c -> [b + 1, n]
 for d -> [c, n]
 ans = ans + min(f(a, b), f(c, d))
```

### Test 2

```
3
3 2 1
```

### Test 3

```
6
```
