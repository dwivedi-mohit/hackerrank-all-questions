# Coolguy and Two Subsequences

- **Domain:** data-structures
- **Difficulty:** Advanced
- **Max Score:** 120
- **Success Ratio:** 0.7958840823183536
- **Total Submissions:** 2381
- **Solved Count:** 1895
- **URL:** https://www.hackerrank.com/challenges/coolguy-and-two-subsequences

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

## Constraints

-  ≤  ≤

-  ≤  ≤

Note:  is -indexed (i.e.: ).

## Sample Input

3 2 1

## Explanation

We then sum these numbers () and print , which is .
