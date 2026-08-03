# Aria's Loops

---

| Field | Value |
|---|---|
| **Slug** | `arias-loops` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 50 |
| **Contest** | 101hack41 |
| **URL** | https://www.hackerrank.com/challenges/arias-loops |

---

## Preview

Determine the result after the loops.

## Problem Statement

Aria's Computer Science professor gave her class the following pseudocode to implement:

<pre>
ans = 0
for i<sub>1</sub> = 1..n
    for i<sub>2</sub> = (i<sub>1</sub> + 1)..n
        for i<sub>3</sub> = (i<sub>2</sub> + 2)..n
            ...
                for i<sub>K</sub> = (i<sub>(k - 1)</sub> + (k - 1))..n
                    ans = ans + 1
print ans
</pre>
  

Can you help her check her work by determining what the value of $ans$ will be after all the loops finish? As this value may be quite large, print your answer modulo $(10^9 + 7)$.

## Input Format

A single line consisting of two space-separated integers describing the respective values of $n$ and $k$.

## Output Format

Print the value of $ans$ after all the loops finish. As this value may be quite large, print your answer modulo $(10^9 + 7)$.

## Constraints

- $1 \le n \le 2 \times 10^9$
- $1 \le k \le 3 \times 10^5$

## Sample Tests

### Test 1

```
ans = 0
for i
1
 = 1..n
 for i
2
 = (i
1
 + 1)..n
 for i
3
 = (i
2
 + 2)..n
 ...
 for i
K
 = (i
(k - 1)
 + (k - 1))..n
 ans = ans + 1
print ans
```

### Test 2

```
3 2
```

### Test 3

```
3
```
