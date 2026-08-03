# Permutation of Natural Numbers

---

| Field | Value |
|---|---|
| **Slug** | `permutation-of-natural-numbers` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 50 |
| **Contest** | 101hack22 |
| **URL** | https://www.hackerrank.com/challenges/permutation-of-natural-numbers |

---

## Problem Statement

A string $S$ is of length $N-1$, and it consists only of the letters $I$ and $D$. You need to rearrange the numbers $[1,N]$ (from $1$ to $N$) and save it in array $X$ such that 

$$ \text{if} \hspace{2 mm} S[i] = D \implies X[i] > X[i+1]  $$
$$ \text{if} \hspace{2 mm} S[i] = I \implies X[i] < X[i+1]  $$

As there can be many such permutations, you need to print the lexicographically largest permutation. Permuation $a_{1},a_{2} \cdots , a_{n}$ will be said to be larger than $b_{1},b_{2} \cdots , b_{n}$ if $a_{1} = b_{1}, a_{2} = b_{2},... a_{k} = b_{k} \hspace{2 mm}and \hspace{2 mm}  a_{k+1} \gt b_{k+1} ,\text{where} \hspace{2mm }k \ge 0. $

## Input Format

The string $S$.


**Constraints**<br>
$1 \le length \hspace{2 mm} of \hspace{2 mm} the \hspace{2 mm} string \le 10^5$

## Output Format

A permutation of numbers in $[1, N]$; there should be a space between the two numbers.

## Sample Tests

### Test 1

```
IIIIID
```

### Test 2

```
2 3 4 5 6 7 1
```

### Test 3

```
2 3 4 5 6 7 1
```
