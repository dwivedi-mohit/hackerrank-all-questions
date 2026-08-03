# Lazy Sorting

---

| Field | Value |
|---|---|
| **Slug** | `lazy-sorting` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/lazy-sorting |

---

## Preview

How much time  will it take to sort a sequence?

## Problem Statement

Logan is cleaning his apartment. In particular, he must sort his old favorite sequence, $P$, of $N$ positive integers in nondecreasing order. He's tired from a long day, so he invented an easy way (in his opinion) to do this job. His algorithm can be described by the following pseudocode:

    while isNotSorted(P) do {	
        WaitOneMinute();
        RandomShuffle(P)
    }

Can you determine the expected number of minutes that Logan will spend waiting for $P$ to be sorted?

## Input Format

The first line contains a single integer, $N$, denoting the size of permutation $P$.		
The second line contains $N$ space-separated integers describing the respective elements in the sequence's current order, $P_0, P_1, \ldots, P_{N-1}$.

## Output Format

Print the expected number of minutes Logan must wait for $P$ to be sorted, correct to  $6$ decimal places.

## Constraints

- $2 \le N \le 18$
- $1 \le P_i \le 100$

## Sample Tests

### Test 1

```
while isNotSorted(P) do { 
 WaitOneMinute();
 RandomShuffle(P)
}
```

### Test 2

```
2
5 2
```

### Test 3

```
2.000000
```
