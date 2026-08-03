# Bit Array

---

| Field | Value |
|---|---|
| **Slug** | `bitset-1` |
| **Domain** | cpp |
| **Difficulty** | Hard |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/bitset-1 |

---

## Preview

Calculate the number of distinct integers created from the given code.

## Problem Statement

You are given four integers: $N$, $S$, $P$, $Q$. You will use them in order to create the sequence $a$ with the following pseudo-code.

	a[0] = S (modulo 2^31)
    for i = 1 to N-1
    	a[i] = a[i-1]*P+Q (modulo 2^31) 
    	
Your task is to calculate the number of distinct integers in the sequence $a$.

## Input Format

Four space separated integers on a single line, $N$, $S$, $P$, and $Q$ respectively.

## Output Format

A single integer that denotes the number of distinct integers in the sequence $a$.

**Constraints**


$1 \leq N \leq 10^8$<br></br>
$0 \leq S,P,Q < 2^{31}$<br></br>

## Sample Tests

### Test 1

```
a[0] = S (modulo 2^31)
for i = 1 to N-1
 a[i] = a[i-1]*P+Q (modulo 2^31)
```

### Test 2

```
3 1 1 1
```

### Test 3

```
3
```
