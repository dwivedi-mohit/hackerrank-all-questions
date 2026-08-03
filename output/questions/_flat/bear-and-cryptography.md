# Bear And Cryptography

---

| Field | Value |
|---|---|
| **Slug** | `bear-and-cryptography` |
| **Domain** | mathematics |
| **Difficulty** | Advanced |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/bear-and-cryptography |

---

## Preview

Find the largest number in 1 to N having exactly K divisors.

## Problem Statement

Limak is a little bear who loves school. Today was his first lesson in cryptography, and the teacher assigned some difficult homework&mdash;to find any number with exactly $K$ divisors. Limak wants to go the extra mile and find the biggest possible number; however, his teacher explained that there are arbitrarily large numbers with this property. 

To give this little bear a more achievable challenge, the teacher advised him to consider only numbers not greater than $N$. 

Given $N$ and $K$, what is the largest number Limak can find?

## Input Format

The first line contains an integer, $T$ (the number of test cases).

The $T$ subsequent lines of test cases each contain two space-separated integers, $N$ and $K$, respectively.

## Output Format

For each test case, print the biggest number Limak can find on a new line. Print $-1$ if no such number exists.

## Constraints

* $1 \le T \le 50$

* $1 \le N \le 10^{12}$

* $1 \le K \le 40$

## Sample Tests

### Test 1

```
3
15 3
15 4
15 5
```

### Test 2

```
9
15
-1
```
