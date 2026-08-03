# Unfriendly Numbers

---

| Field | Value |
|---|---|
| **Slug** | `unfriendly-numbers` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/unfriendly-numbers |

---

## Preview

How many numbers divide the 'friendly number' but not the other numbers?

## Problem Statement

Given $1$ *friendly* number and $n$ *unfriendly* numbers, determine how many numbers are divisors of the friendly number but *not* the unfriendly numbers.

## Input Format

The first line contains $2$ space-separated integers, $n$ (the number of unfriendly numbers) and $f$ (the friendly number), respectively. 
The second line contains $n$ space-separated unfriendly numbers.

## Output Format

Print the the number of unique divisors of $f$ (i.e.: divisors that are not shared with those of the unfriendly numbers) as a single integer.

## Constraints

- $1 \le n \le 10^6$
- $1 \le f \le 10^{13}$
- $1 \le \textit{unfriendly numbers} \le 10^{18}$

## Sample Tests

### Test 1

```
8 16
2 5 7 4 3 8 3 18
```

### Test 2

```
1
```
