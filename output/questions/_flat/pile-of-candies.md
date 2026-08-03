# Candy Piles

---

| Field | Value |
|---|---|
| **Slug** | `pile-of-candies` |
| **Contest** | hourrank-16 |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/pile-of-candies |

---

## Problem Statement

Alice is celebrating the New Year with $n$ piles of candies! Each pile $i$ contains $c_i$ candies, and she defines her *happiness factor* as the minimum number of candies in any pile. As this is a special day, Alice wants to *try to maximize her happiness factor* by choosing exactly one pile and doubling the number of candies in it. 

Find the following two values and print them as space-separated integers on a single line:

1. The maximum happiness factor Alice can achieve after doubling the number of candies in one of her piles.

2. The number of ways Alice can choose a pile to achieve the maximum happiness factor. In other words, this is **the total number of piles that still result in the same maximum happiness factor** if Alice chooses to double them.

## Input Format

The first line contains an integer $n$.			
The second line contains $n$ space-separated integers describing $c_0, c_1, c, \ldots, c_{n-1}$.

## Output Format

Print the following two space-separated integers on a single line:

1. The maximum happiness factor Alice can achieve after doubling the number of candies in one of her piles.
2. The number of ways Alice can choose a pile to achieve the maximum happiness factor.

## Constraints

* $1 \le n \le 100$
* $1 \le c_i \le 10^5$
