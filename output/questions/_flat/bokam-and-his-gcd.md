# Subset GCD

---

| Field | Value |
|---|---|
| **Slug** | `bokam-and-his-gcd` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 30 |
| **Contest** | adobe-hackathon |
| **URL** | https://www.hackerrank.com/challenges/bokam-and-his-gcd |

---

## Preview

Find the number of subsets with gcd = Ai.

## Problem Statement

You are given an array $A$ with $N$ elements. $A$<sub>i</sub> represents the $i$<sup>th</sup> element of the array.
The greatest common divisor (gcd) of two or more integers is the largest positive integer, not including zero, that divides the numbers without a remainder. For example, the gcd of 8 and 12 is 4.<br>
**Your task:** Print $N$ space-separated integers where the $i$<sup>th</sup> integer represents the number of subsets with gcd $A_i$%$1000000007$.

**Note**: The gcd(B<sub>1</sub>, B<sub>2</sub>,…,B<sub>m</sub>) is the greatest common divisor of {B<sub>1</sub>, B<sub>2</sub>,…,B<sub>m</sub>}.

## Input Format

The first line contains the integer $N$.<br>
The second line contains $N$ space-separated integers, representing the elements of the array.

**Constraints**

$1 \le N \le 10^6$

$1 \le A_i \le N$

## Output Format

Output $N$ space-separated integers. The $i$<sup>th</sup> integer represents the number of subsets with gcd $A_i$%$1000000007$.<br><br>

## Sample Tests

### Test 1

```
3
2 2 3
```

### Test 2

```
3 3 1
```
