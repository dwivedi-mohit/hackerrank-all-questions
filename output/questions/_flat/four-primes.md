# Four Primes

---

| Field | Value |
|---|---|
| **Slug** | `four-primes` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 50 |
| **Contest** | 101hack30 |
| **URL** | https://www.hackerrank.com/challenges/four-primes |

---

## Preview

Figure out whether it is possible to represent an integer as a binary OR of four prime numbers.

## Problem Statement

Recently, Sergey read that any integer number, greater than 1 and less than $10$<sup>18</sup>, can be represented as the sum of no more than 4 prime numbers. His curiosity piqued, Sergey decided to research further. <br>

He has a list of integers and would like to see whether each of them can be represented as a [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR) of, **at most**, 4 [prime numbers](https://en.wikipedia.org/wiki/Prime_number). Can you help Sergey see if this is possible?

## Input Format

The first line of input contains a single integer $T$, denoting the number of integers in the list.

Each of the following $T$ lines contain a single integer $N_i$, denoting a number from the list.

**Constraints**

- $1 \leq T \leq 8000$
- $2 \leq N_i \leq 8000$
- In addition, $2 \leq N_i \leq 100$ for the smaller test cases (worth 50% of the points).

## Output Format

Output $T$ lines, where the $i$<sup>th</sup> line should be "YES" in case $N_i$ can be represented as a binary OR of 4 primes and "NO" otherwise.

## Sample Tests

### Test 1

```
2
4
15
```

### Test 2

```
NO
YES
```
